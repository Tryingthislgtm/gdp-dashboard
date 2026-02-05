import pandas as pd
from pathlib import Path
from pricing_plans_loader import get_pricing_plans


def test_core_plan_present():
    plans = get_pricing_plans()
    assert 'Core' in plans['PlanName'].values


def test_core_flat_price_for_five_lenses():
    plans = get_pricing_plans()
    core = plans[plans['PlanName'] == 'Core'].iloc[0]
    base_per_lens = float(core['BasePrice'])
    total = base_per_lens * 5
    assert abs(total - 29.0) < 0.01


def test_core_addons_calculation():
    path = Path(__file__).parent.parent / 'data' / 'core_addons.csv'
    df = pd.read_csv(path)
    optional = df[df['Included'] == False]
    # pick Priority Support and Extra Storage (15 and 10)
    selected = ['Priority Support', 'Extra Storage']
    prices = optional.set_index('AddonName')['Price'].to_dict()
    per_lens_extra = sum(prices[name] for name in selected)
    total_extra = per_lens_extra * 5
    assert per_lens_extra == 25
    assert total_extra == 125
