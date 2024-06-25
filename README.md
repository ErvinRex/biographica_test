# TASK

As an example of the type of data transformations we face at Biographica, we ask you to download and process plant genome data from one of the public repositories.

In this case, GFF files downloaded from the [Ensembl Plant Genomes FTP site](https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/). GFF files are the canonical data format for describing what are known as ‘genome builds’ - descriptions of the gene content in an organism. A description of the GFF file format can be found [here](https://www.ensembl.org/info/website/upload/gff.html).

**Create a script, module or application to perform ETL of GFF files from Ensembl Plants.**

The app should take as an input an Ensembl release version and the name of an organism and return a table or tabular file listing the genes of the given organism, ready for downstream consumption. Please include relevant information about each gene and potentially any relevant metadata.

In your solution, please consider the following aspects which would be relevant in a larger, production-ready version of this kind of application:

- Reproducibility
- Traceability
- Data lineage
- Scalability
- Documentation

## Pipeline

In this repository you will find the full pipeline and testing scripts that perform the above tasks.