from pathlib import Path
import pandas as pd


def get_gdp_data():
    """Load and pivot GDP data into a tidy DataFrame.

    Returns a DataFrame with columns: Country Code, Year, GDP
    """
    DATA_FILENAME = Path(__file__).parent / 'data' / 'gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df
