




|journal list  |count |
|:-------------|:-----|
|Catalogue     |1996  |
|MPG           |1812  |
|Netherlands   |1843  |
|UK            |1820  |
|Austria       |1838  |
|Sweden        |1844  |
|Finland       |1844  |
|Hungary       |1844  |
|Poland        |1844  |
|Combined list |2015  |

```
#> # A tibble: 357 x 10
#>    Title Catalogue MPG   Netherlands UK    Austria Sweden Finland Hungary
#>    <chr> <lgl>     <lgl> <lgl>       <lgl> <lgl>   <lgl>  <lgl>   <lgl>  
#>  1 Adap… TRUE      TRUE  FALSE       TRUE  TRUE    TRUE   TRUE    TRUE   
#>  2 ADHD… TRUE      TRUE  TRUE        TRUE  TRUE    FALSE  FALSE   FALSE  
#>  3 Air … TRUE      TRUE  TRUE        TRUE  FALSE   TRUE   TRUE    TRUE   
#>  4 Amer… TRUE      TRUE  TRUE        TRUE  TRUE    FALSE  FALSE   FALSE  
#>  5 Anna… TRUE      TRUE  TRUE        TRUE  FALSE   TRUE   TRUE    TRUE   
#>  6 Apop… TRUE      TRUE  FALSE       TRUE  TRUE    TRUE   TRUE    TRUE   
#>  7 Appl… FALSE     TRUE  TRUE        TRUE  TRUE    TRUE   TRUE    TRUE   
#>  8 Appl… TRUE      TRUE  TRUE        TRUE  TRUE    FALSE  FALSE   FALSE  
#>  9 Arch… TRUE      TRUE  TRUE        TRUE  FALSE   TRUE   TRUE    TRUE   
#> 10 Arch… TRUE      TRUE  FALSE       TRUE  TRUE    TRUE   TRUE    TRUE   
#> # ... with 347 more rows, and 1 more variable: Poland <lgl>
```

![plot of chunk unnamed-chunk-3](/figure/unnamed-chunk-3-1.png)

Common Journals: 1658

## 1. Introduction

It is known that portfolios of eligible journals for the [Springer Compact Agreements](https://www.springer.com/de/open-access/springer-open-choice/springer-compact) (SCA) differ between consortional partners. This evaluation is meant to analyse those differences and also relate them to the full catalogue of hybrid Springer journals ("Open Choice").

## 2. Data origins

Springer provides individual lists of eligible journals for all participants on its web site, those can be [downloaded in PDF Format](https://www.springer.com/de/open-access/springer-open-choice/springer-compact/agreements-dutch-authors) ("Click here for a list of Open Choice eligible subscription-based journals covered by the Open Access agreement with Dutch universities and Academy institutes"). 
The according files have been obtained for all consortional partners (Netherlands, UK, Sweden, Austria, Finland, Poland, Hungary and the Max Planck Society (MPG)) and can be found [here](raw_pdf_lists).
Springer also provides a full catalogue of published journals as an Excel spreadsheet which can be found [here](https://www.springernature.com/de/librarians/licensing/journals-price-list) ("2019 Springer Nature Journals including Open Access").

## 3. Data preprocessing

Our goal was to compile a full list of Springer hybrid journals, with a set of binary variables to indicate if a journal is present in a specific sub list. This was done via the following steps:

### 3.1 PDF extraction

Since the SCA journal lists were only available in PDF format, a machine-readable variant had to be extracted first. This was done using the [Tabula](https://tabula.technology/) toolkit, the resulting CSV files are to be found [here](extracted_csvs).

### 3.2 Catalogue filtering

The full Springer journal catalogue contains both fully OA and hybrid journals. Since only the latter are relevant to the SCA programme, 

