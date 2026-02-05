from pathlib import Path
import pandas as pd


def get_promotions_data():
    """Load and transform promotion data for camera products.

    Returns a DataFrame with columns: Product, Category, Quarter, Price, DiscountPercent
    """
    DATA_FILENAME = Path(__file__).parent / 'data' / 'promotions.csv'
    raw_df = pd.read_csv(DATA_FILENAME)

    # Melt quarterly prices into rows
    promo_df = raw_df.melt(
        id_vars=['Product', 'Category', 'BasePrice'],
        value_vars=['Q1', 'Q2', 'Q3', 'Q4'],
        var_name='Quarter',
        value_name='PromoPrice',
    )

    # Calculate discount percentage
    promo_df['DiscountPercent'] = (
        (promo_df['BasePrice'] - promo_df['PromoPrice']) / promo_df['BasePrice'] * 100
    ).round(1)

    # Calculate savings
    promo_df['Savings'] = (promo_df['BasePrice'] - promo_df['PromoPrice']).round(2)

    return promo_df
