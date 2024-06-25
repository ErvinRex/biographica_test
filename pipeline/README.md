# Biographica Technical Interview Pipeline Instructions

## Problem Statement

The ETL pipeline should take as an input an Ensembl release version and the name of an organism and return a tabular file listing the genes of the given organism, ready for downstream consumption. Alongside relevant information about each gene in the same file and any relevant metadata in a separate tabular file (TSV).

## Assumption

- GTF files = GFFv2 files and are seen in all release versions - so these were selected over GFF3 (version 3).
- The `feature` column is used to distinguish if a row is related to a gene or not.

## Overview

### Functions

1. **Extract**: Scrapes the Ensembl website to access the URLs of GFF/GTF files, then return a pandas data frame for the requested release version and organism. The correct GTF/GFF file is extracted using a regex statement to locate it and create a data frame from the given file link. A meta data data frame is also created for each pipeline run.

2. **Transform**: Filters the data frame for rows that match the 'gene' key feature. Resets the index so it can be easily wrangled.

3. **Load**: Loads the pandas data frame on to a tab-separated (TSV) file to be used for further research/downstream consumption.

## Data Cleaning

After the pipeline is complete, running `filtered_gff_df.isnull().values.any()` inside the `main` function of `pipeline.py`, has always returned False, therefore the dataset consists of no `NAN` values without further delving in to more specific cleaning methods.

## Pipeline Testing

### How to Test
In order to test the files, you firstly must make sure that you `pip install -r requirements.txt` in order to have access to `pytest`. Once this has been done you can run:
- `pytest test_xxxx` -> This will run the pytest on the specific file itself.
- `pytest` -> This will run pytest on every test file within the directory you are currently in.
- `pytest --cov . --cov-report term-missing` -> This will show overall test coverage of the system, as well as whats missing and needs to be tested.

## Improvements

- Downloading of files just to access metadata seems unnecessary, an alternative method of accessing it using pandas should be explored, however pandas for now is raising errors due to comment (`#`) handling.
- Avoided exploration with pandas because the `comment` parameter in the `extract.py` script was clean and efficient at removing the first `X` rows of metadata.
- Improve coverage of tests, check rows all have `gene` as their feature, etc.