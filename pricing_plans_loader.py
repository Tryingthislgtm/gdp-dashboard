from pathlib import Path
import pandas as pd


def get_pricing_plans():
    """Load pricing plans data.

    Returns a DataFrame with columns: PlanName, PlanType, BasePrice, Description, Features
    """
    DATA_FILENAME = Path(__file__).parent / 'data' / 'pricing_plans.csv'
    plans_df = pd.read_csv(DATA_FILENAME)
    return plans_df
