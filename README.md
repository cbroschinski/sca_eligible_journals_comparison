## About

This repository contains scripts, source data and dynamic documents supporting an evaluation on journals eligible for the [Springer Compact Agreements](https://www.springer.com/de/open-access/springer-open-choice/springer-compact). 
Find the resulting report [here](https://cbroschinski.github.io/sca_eligible_journals_comparison/).

## Report generation

The HTML report is generated via a python/R Markdown/pandoc toolchain. Additional R packages might be required.

```

python preprocessing.py
R -e "knitr::knit('index.Rmd')"
pandoc -f gfm -t html5 index.md -o index.html

```

