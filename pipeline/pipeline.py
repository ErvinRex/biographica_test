"""
Python script that extracts, transforms and loads
gene information to a tab-separated file
"""

from extract import get_gff_data
from transform import get_gene_rows
from load import download_tsv

def main():
    """
    Run whole pipeline and return genes and metadata
    """

    metadata, gff_data = get_gff_data('current', 'beta_vulgaris')

    if not metadata.empty and not gff_data.empty:

        filtered_gff_df = get_gene_rows(gff_data)

        download_tsv(filtered_gff_df, 'beta_vulgaris_current_genes')

        download_tsv(metadata, 'beta_vulgaris_current_metadata')

if __name__ == "__main__":
    main()