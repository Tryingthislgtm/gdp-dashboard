# Google Sheets — Promotion Impact prototype

This folder contains a small Google Apps Script prototype that previews and applies promotion discounts to a numeric range in Google Sheets. It's intended as a starting point for a Workspace Add-on your teams can use when modeling promotions and their billing impact.

Quick setup

Option A — use the Apps Script editor

- Open Google Sheets and go to Extensions → Apps Script.
- Create a new project and copy the files from this folder (`Code.gs`, `sidebar.html`, `appsscript.json`) into the editor.
- Save the project. The script will request authorization when first used.
- Reload your spreadsheet; use the `Promotions` menu → `Open Promotion Tool`.

Option B — use `clasp` (command line)

1. Install clasp: `npm install -g @google/clasp`
2. Login: `clasp login`
3. Create a project locally or push these files to an Apps Script project. See https://github.com/google/clasp` for details.

How it works

- Select a numeric range in your sheet (prices, invoice lines, etc.).
- Open the sidebar and set a promotion: percentage or flat discount.
- Click `Preview impact` to see original total, new total, and delta.
- Click `Apply promotion to sheet` to overwrite the selected cells with discounted values.

Next steps (suggestions)

- Add support for tiered promotions, per-product rules, or minimum quantities.
- Add logging and an audit sheet to keep original values before applying promotions.
- Turn this into a published Workspace Add-on and configure domain installation.
