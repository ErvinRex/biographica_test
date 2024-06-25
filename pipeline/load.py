"""
Python script responsible for loading data in to a TSV format
"""

import logging

import pandas as pd

from extract import get_gff_data
from transform import get_gene_rows

def download_tsv(dataframe: pd.DataFrame, filename: str) -> None:
    """
    Download a pandas dataframe as a tab-separated file
    """

    dataframe.to_csv(f'data/{filename}.tsv', sep='\t')

    logging.info('TSV file created successfully.')


if __name__ == "__main__":
    
    metadata, gff_data = get_gff_data('current', 'beta_vulgaris')

    filtered_gff_df = get_gene_rows(gff_data)

    download_tsv(filtered_gff_df, 'beta_vulgaris_current_genes')

    download_tsv(metadata, 'beta_vulgaris_current_genes_metadata')

