import pandas as pd
from gdp_loader import get_gdp_data


def test_get_gdp_data_basic():
    df = get_gdp_data()
    # Basic shape and columns
    assert not df.empty
    assert 'Country Code' in df.columns
    assert 'Year' in df.columns
    assert 'GDP' in df.columns


def test_get_gdp_data_year_range():
    df = get_gdp_data()
    years = df['Year'].dropna().unique()
    assert years.min() >= 1960
    assert years.max() <= 2022


def test_gdp_types():
    df = get_gdp_data()
    assert pd.api.types.is_numeric_dtype(df['GDP'])
    assert pd.api.types.is_integer_dtype(df['Year']) or pd.api.types.is_numeric_dtype(df['Year'])
