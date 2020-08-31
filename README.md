# Code for building Sankey or alluvial flow diagrams for genome contamination

See [charcoal #132](https://github.com/dib-lab/charcoal/issues/132) and [a twitter thread](https://twitter.com/BioMickWatson/status/1299365876421062656).

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/ctb/2020-charcoal-sankey/render?filepath=index.ipynb)

Note, the above binder is built off of the `render` branch.

## Some static diagrams

In the diagrams below, paths represent the lineage of contigs
aggregated to each taxonomic rank, scaled by approximate contig size.
The blue path is the path that matches the known genome lineage of the
full genome.

You can download
[sankey-diagrams.html](https://github.com/ctb/2020-charcoal-sankey/blob/latest/sankey-diagrams.html)
to get this in an interactive format.

### Contaminated genomes

This first GenBank genome is a mix of Archaea and Bacteria!

![GCA_001421185](static-images/GCA_001421185.1_genomic.fna.gz.png)

A mixture of firmicute and proteobacterial sequence in a GenBank genome.

![GCF_000763125](static-images/GCF_000763125.1_genomic.fna.gz.png)

Minimal phylum level mismatches, but lots of genus level mismatches in a
Genbank genome.

![GCF_001078575](static-images/GCF_001078575.1_genomic.fna.gz.png)

Bacterial contamination in a euk from some TARA MAGs.

![TARA_ANW_MAG_00083](static-images/TARA_ANW_MAG_00083.fa.png)

Multiple different phyla in a single MAG (TARA).

![TARA_PON_MAG_00067](static-images/TARA_PON_MAG_00067.fa.png)

Bacterial AND Archaeal contamination in a Euk (TARA).

![TARA_RED_MAG_00116](static-images/TARA_RED_MAG_00116.fa.png)
