function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Promotions')
    .addItem('Open Promotion Tool', 'showSidebar')
    .addToUi();
}

function showSidebar() {
  const html = HtmlService.createHtmlOutputFromFile('sidebar')
    .setTitle('Promotion Impact');
  SpreadsheetApp.getUi().showSidebar(html);
}

/**
 * calculateImpact
 * promo: { type: 'percentage'|'flat', value: number }
 * Returns summary of impact on the currently selected range.
 */
function calculateImpact(promo) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const range = sheet.getActiveRange();
    const values = range.getValues();
    let originalTotal = 0;
    let newTotal = 0;
    const perCell = [];

    for (let r = 0; r < values.length; r++) {
      for (let c = 0; c < values[0].length; c++) {
        const v = parseFloat(values[r][c]);
        if (isNaN(v)) continue;
        originalTotal += v;
        let newValue = v;
        if (promo.type === 'percentage') {
          newValue = v * (1 - promo.value / 100);
        } else if (promo.type === 'flat') {
          newValue = Math.max(0, v - promo.value);
        }
        newTotal += newValue;
        perCell.push({row: range.getRow() + r, col: range.getColumn() + c, original: v, newValue: newValue});
      }
    }
    const delta = newTotal - originalTotal;
    return {originalTotal: originalTotal, newTotal: newTotal, delta: delta, perCell: perCell};
  } catch (e) {
    throw new Error('Error calculating impact: ' + e.toString());
  }
}

function applyPromotionToRange(promo) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const range = sheet.getActiveRange();
  const values = range.getValues();

  for (let r = 0; r < values.length; r++) {
    for (let c = 0; c < values[0].length; c++) {
      const v = parseFloat(values[r][c]);
      if (isNaN(v)) continue;
      let newValue = v;
      if (promo.type === 'percentage') {
        newValue = v * (1 - promo.value / 100);
      } else if (promo.type === 'flat') {
        newValue = Math.max(0, v - promo.value);
      }
      values[r][c] = newValue;
    }
  }
  range.setValues(values);
  return true;
}
