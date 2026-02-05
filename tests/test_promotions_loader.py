import pandas as pd
from promotions_loader import get_promotions_data


def test_get_promotions_data_basic():
    df = get_promotions_data()
    # Basic shape and columns
    assert not df.empty
    assert 'Product' in df.columns
    assert 'Quarter' in df.columns
    assert 'BasePrice' in df.columns
    assert 'PromoPrice' in df.columns
    assert 'DiscountPercent' in df.columns


def test_get_promotions_data_quarters():
    df = get_promotions_data()
    quarters = df['Quarter'].unique()
    assert set(quarters).issubset({'Q1', 'Q2', 'Q3', 'Q4'})


def test_discount_calculations():
    df = get_promotions_data()
    # Verify discount percent is calculated correctly
    for idx, row in df.iterrows():
        expected_discount = (row['BasePrice'] - row['PromoPrice']) / row['BasePrice'] * 100
        assert abs(row['DiscountPercent'] - round(expected_discount, 1)) < 0.01


def test_promo_price_less_than_base():
    df = get_promotions_data()
    # Promotional prices should be <= base price
    assert (df['PromoPrice'] <= df['BasePrice']).all()
