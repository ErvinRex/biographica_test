"""
Python script for testing transform functions
"""

import pandas as pd
from io import StringIO

from transform import get_gene_rows

data = """seqname\tsource\tfeature\tstart\tend\tscore\tstrand\tframe\tattribute
chr1\tRefSeq\tgene\t1300\t1500\t.\t+\t0\tID=gene1
chr1\tRefSeq\texon\t1500\t1550\t.\t+\t0\tID=exon1;Parent=gene1
chr1\tRefSeq\tgene\t3000\t3500\t.\t+\t0\tID=gene2
chr1\tRefSeq\tCDS\t1500\t1550\t.\t+\t0\tID=cds1;Parent=gene1
"""

def test_get_gene_rows_returns_dataframe():

    gff_df = pd.read_csv(StringIO(data), sep='\t')
    result_df = get_gene_rows(gff_df)

    assert isinstance(result_df, pd.DataFrame)
