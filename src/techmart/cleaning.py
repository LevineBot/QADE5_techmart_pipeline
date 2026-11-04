"""Data cleaning for the TechMart pipeline."""

import os

def remove_duplicates(df, subset=None):
    """Remove duplicate rows from a DataFrame."""
    return df.drop_duplicates(subset=subset)
