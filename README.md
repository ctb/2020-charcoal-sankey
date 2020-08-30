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

### An example MAG with minimal contamination

![LoombaR_2017__SID1050_bax__bin.11](static-images/LoombaR_2017__SID1050_bax__bin.11.fa.gz.png)

### Contaminated genbank genomes

This first genome is a mix of Archaea and Bacteria!

![GCA_001421185](static-images/GCA_001421185.1_genomic.fna.gz.png)

Oh, hey, another mixture of archaea and bacteria!

![GCF_000492175](static-images/GCF_000492175.1_genomic.fna.gz.png)

Mixed phyla...

![GCA_003220225](static-images/GCA_003220225.1_genomic.fna.gz.png)

Mixed phyla again...

![GCA_003221985](static-images/GCA_003221985.1_genomic.fna.gz.png)

Mixed phyla again...

![GCA_003222275](static-images/GCA_003222275.1_genomic.fna.gz.png)

Mixed phyla again...

![GCA_003222535](static-images/GCA_003222535.1_genomic.fna.gz.png)

Mixed phyla...

![GCF_001078575](static-images/GCF_001078575.1_genomic.fna.gz.png)

Hmm, this looks suspicious...

![GCF_001184205](static-images/GCF_001184205.1_genomic.fna.gz.png)

Mixed phyla.

![GCF_001408335](static-images/GCF_001408335.1_genomic.fna.gz.png)

Mixed phyla...

![GCF_001672295](static-images/GCF_001672295.1_genomic.fna.gz.png)

Mixed phyla...

![GCF_001683825](static-images/GCF_001683825.1_genomic.fna.gz.png)

Mixed phyla...

![GCF_000763125](static-images/GCF_000763125.1_genomic.fna.gz.png)

Maybe a teensy bit of contamination?

![GCF_001749745](static-images/GCF_001749745.1_genomic.fna.gz.png)

More teensy bit of contamination.

![GCF_002154655](static-images/GCF_002154655.1_genomic.fna.gz.png)

Even more teensy bit of contamination.

![GCF_002901805](static-images/GCF_002901805.1_genomic.fna.gz.png)

Even yet more teensy bit of contamination.

![GCF_900016235](static-images/GCF_900016235.2_genomic.fna.gz.png)




