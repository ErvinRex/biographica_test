"""
Python script for standardising and cleaning pandas dataframes,
and transforming to only return gene feature rows.
"""

import logging

import pandas as pd

from extract import get_gff_data

def get_gene_rows(gff_df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a data frame that only consists of gene feature rows 
    """

    gene_gff_df =gff_df[gff_df['feature'] == 'gene']

    gene_gff_df.reset_index(inplace=True, drop=True)

    logging.info('Gene features filtered and stored successfully.')

    return gene_gff_df

if __name__ == "__main__":

    metadata, gff_data = get_gff_data('current', 'beta_vulgaris')

    filtered_gff_df = get_gene_rows(gff_data)

    print(filtered_gff_df.head(5))