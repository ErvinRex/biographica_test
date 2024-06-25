"""
Python script for extracting GFF files from Ensembl
"""

import gzip
import logging
import re
import os
from typing import Union

from bs4 import BeautifulSoup
import requests
import pandas as pd

logging.basicConfig(filename="logs.log", filemode="w",
                    format="%(name)s → %(levelname)s: %(message)s", level=logging.INFO)

def get_gff_file_link(release_version: Union[int, str], org_name: str) -> str:
    """
    Requests and returns queried GFF file from Ensembl website
    """

    if isinstance(release_version, int):
        url = f"https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/release-{release_version}/gtf/{org_name}"

    else:
        url = f"https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/{release_version}/gtf/{org_name}"

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            temp = link.get('href')
            if re.search(r'\d(.gtf.gz)' ,temp):
                gff_link = f"{url}/{temp}"
                logging.info("GFF link acquired successfully.")
                return gff_link
    except requests.RequestException as error:
        logging.error(f"Error fetching URL: {error}")
        return []
    
def download_gff_file(gff_link) -> None:
    """
    Downloads a gff from the Ensembl url
    """

    try:
        response = requests.get(gff_link, timeout=10)
        with open(f"temp_gff.gz", "wb") as f:
            f.write(response.content)
            logging.info("GFF file downloaded successfully.")
        return
    except (requests.exceptions.MissingSchema, requests.exceptions.ReadTimeout) as error:
        logging.error(f"Error fetching URL: {error}")

def get_meta_data(gff_filepath: str):
    """
    Return the metadata for a given gff file
    """

    with gzip.open(gff_filepath, 'rt') as file:
        lines = file.readlines()

    pattern = re.compile(r'^#!(.+)$')
    data = {}

    for line in lines:
        match = pattern.match(line)
        if match:
            part = match.group(1).split(' ')
            if len(part) == 2:
                name, value = part
                data[name] = value

    header_df = pd.DataFrame([data])

    logging.info("Metadata data frame acquired successfully.")

    return header_df


def get_gff_data(release_version: int, org_name: str) -> pd.DataFrame:
    """
    Run the extract script and return a gff file in pandas format with metadata
    """

    file = get_gff_file_link(release_version, org_name)

    if file:
        download_gff_file(file)
        meta_df = get_meta_data('temp_gff.gz')
        os.remove('temp_gff.gz')
        df = pd.read_csv(file, sep='\t', comment='#')
        df.columns = ['seqname', 'source', 'feature', 'start',
                      'end', 'score', 'strand', 'frame', 'attribute']
        return meta_df, df
    else:
        logging.error('Organism could not be found in this release.')

if __name__ == "__main__":

    metadata, gff_data = get_gff_data('current', 'beta_vulgaris')

    if metadata and gff_data:
        print(metadata['genome-build'].iloc[0])
        print(gff_data.head())