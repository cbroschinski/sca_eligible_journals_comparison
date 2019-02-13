



<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
<link rel="stylesheet" type="text/css" href="DataTables/datatables.min.css"/>
<script type="text/javascript" src="DataTables/datatables.min.js"></script>
</head>

<body>
<script>
$(document).ready(function () {
    var table = $('table').last();
    table.children('thead').append('<tr class="name_row"></tr>');
    table.children('thead').each(function () {
        $(this).children('tr').first().attr('class', 'search_row');
    })
    $('.search_row th').each(function() {
        $(this).parent().siblings('.name_row').append($(this).clone());
        var col_text = $(this).text();
        var width = $(this).css('width');
        $th = '<div style="width: ' + width + '"><input type="text" placeholder="'+col_text+'" data-column-name="' + col_text + '"></div>';
        $(this).html($th);
    });
    var data_table = table.DataTable();
    data_table.columns().every(function () {
        var column = this;
        var header_text = $(column.header()).text();
        var $input = $('input[data-column-name="' + header_text + '"]');
        if ($('.FixedHeader_Cloned').length) {
            var $input = $('.FixedHeader_Cloned input[data-column-name="' + header_text + '"]');
        }
        $input.off('keyup change');
        $input.on('keyup change', function() {
            column.search($input.val()).draw();
        });
    });
});
</script>

<div class="container-fluid">




# Comparison of journal eligibility lists for Springer Compact Agreements (SCA)

## 1. Introduction

It is known that portfolios of eligible journals for the [Springer Compact Agreements](https://www.springer.com/de/open-access/springer-open-choice/springer-compact) (SCA) differ between consortional partners. 
This evaluation is meant to analyse those differences and also relate them to the full catalogue of hybrid Springer journals ("Open Choice"). Results are expected to be useful for further analyses on the effects and impacts of SCAs, like the [Coverage Analysis](https://openapc.github.io/general/openapc/2018/03/22/offsetting-coverage/) conducted by our [OpenAPC](https://github.com/OpenAPC/openapc-de) project or the impact estimations made by Jisc.

## 2. Data origins

Springer provides individual lists of eligible journals for all participants on its web site, those can be [downloaded in PDF Format](https://www.springer.com/de/open-access/springer-open-choice/springer-compact/agreements-dutch-authors) ("Click here for a list of Open Choice eligible subscription-based journals covered by the Open Access agreement with Dutch universities and Academy institutes"). 
The according files have been obtained for all consortional partners (Netherlands, UK, Sweden, Austria, Finland, Poland, Hungary and the Max Planck Society (MPG)) and can be found [here](https://github.com/cbroschinski/sca_eligible_journals_comparison/tree/master/raw_pdf_lists).
Springer also provides a full catalogue of published journals as an Excel spreadsheet which can be found [here](https://www.springernature.com/de/librarians/licensing/journals-price-list) ("2019 Springer Nature Journals including Open Access").

## 3. Data processing

Our goal was to compile a full list of Springer hybrid journals, with a set of binary variables to indicate if a journal is present in a specific sub list. The following steps were carried out:

### 3.1 PDF extraction

Since the SCA journal lists were only available in PDF format, a machine-readable variant had to be extracted first. This was done using the [Tabula](https://tabula.technology/) toolkit, the resulting CSV files can be found [here](https://github.com/cbroschinski/sca_eligible_journals_comparison/tree/master/extracted_csvs).

### 3.2 Catalogue filtering

The full Springer journal catalogue contains both fully OA and hybrid journals. Since only the latter are relevant to the SCA programme, the table was filtered, keeping only those entries with the value "Hybrid (Open Choice)" in the "open access" column. The spreadsheet was then exported to CSV (Catalogue.csv).

### 3.3 Creation of a combined list

A python [preprocessing script](https://github.com/cbroschinski/sca_eligible_journals_comparison/blob/master/preprocessing.py) creates a [combined, duplicate-free list](https://github.com/cbroschinski/sca_eligible_journals_comparison/blob/master/combined_list.csv) of all journals appearing in any of the created CSV files. 
The column "product_id" serves as primary key to find matching journals, other identifiers like title or ISSNs turned out to be inconsistent between the lists. The script notifies of such cases, an attached [log file](https://github.com/cbroschinski/sca_eligible_journals_comparison/blob/master/preprocessing_log.txt) shows the output.

### 4. Analysis

The following table shows the number of journals contained in each list:


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

Out of these 2015 total entries, 1658 are common journals - they appear in all the SCA eligibility lists and also in the catalogue. This means that there's a set of 357 journals which are missing in at least one of the lists. The following interactive table shows those journals and the list they are (not) part of. 
The list may be filtered to certain combinations by entering TRUE oder FALSE into the search fields above the column headers. The entry in the product_id column links to the journal landing page on SpringerLink for easy reference.


|Title                                                                                      |product_id                                       |Catalogue |MPG   |Netherlands |UK    |Austria |Sweden |Finland |Hungary |Poland |
|:------------------------------------------------------------------------------------------|:------------------------------------------------|:---------|:-----|:-----------|:-----|:-------|:------|:-------|:-------|:------|
|Adaptive Human Behavior and Physiology                                                     |[40750](https://link.springer.com/journal/40750) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|ADHD Attention Deficit and Hyperactivity Disorders                                         |[12402](https://link.springer.com/journal/12402) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Air Quality, Atmosphere & Health                                                           |[11869](https://link.springer.com/journal/11869) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|American Journal of Criminal Justice                                                       |[12103](https://link.springer.com/journal/12103) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Annals of Nuclear Medicine                                                                 |[12149](https://link.springer.com/journal/12149) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Apoptosis                                                                                  |[10495](https://link.springer.com/journal/10495) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Applied Biological Chemistry                                                               |[13765](https://link.springer.com/journal/13765) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Applied Composite Materials                                                                |[10443](https://link.springer.com/journal/10443) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Archaeologies                                                                              |[11759](https://link.springer.com/journal/11759) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Archives of Gynecology and Obstetrics                                                      |[404](https://link.springer.com/journal/404)     |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Archives of Virology                                                                       |[705](https://link.springer.com/journal/705)     |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|The Asia-Pacific Education Researcher                                                      |[40299](https://link.springer.com/journal/40299) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Augmented Human Research                                                                   |[41133](https://link.springer.com/journal/41133) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Behavior Genetics                                                                          |[10519](https://link.springer.com/journal/10519) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Biogerontology                                                                             |[10522](https://link.springer.com/journal/10522) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Biologia Plantarum                                                                         |[10535](https://link.springer.com/journal/10535) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|BioNanoScience                                                                             |[12668](https://link.springer.com/journal/12668) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Boletín de la Sociedad Matemática Mexicana                                                 |[40590](https://link.springer.com/journal/40590) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Building Simulation                                                                        |[12273](https://link.springer.com/journal/12273) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Cambridge Journal of Evidence- Based Policing                                              |[41887](https://link.springer.com/journal/41887) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Cardiovascular Engineering and Technology                                                  |[13239](https://link.springer.com/journal/13239) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|CCF Transactions on Networking                                                             |[42045](https://link.springer.com/journal/42045) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Child Indicators Research                                                                  |[12187](https://link.springer.com/journal/12187) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Chinese Journal of Academic Radiology                                                      |[42058](https://link.springer.com/journal/42058) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Chinese Journal of Polymer Science                                                         |[10118](https://link.springer.com/journal/10118) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Clinical Social Work Journal                                                               |[10615](https://link.springer.com/journal/10615) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Cognitive Processing                                                                       |[10339](https://link.springer.com/journal/10339) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Colloid and Polymer Science                                                                |[396](https://link.springer.com/journal/396)     |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Conservation Genetics                                                                      |[10592](https://link.springer.com/journal/10592) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Contemporary Family Therapy                                                                |[10591](https://link.springer.com/journal/10591) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Contributions to Mineralogy and Petrology                                                  |[410](https://link.springer.com/journal/410)     |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Current Clinical Microbiology Reports                                                      |[40588](https://link.springer.com/journal/40588) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Current Environmental Health Reports                                                       |[40572](https://link.springer.com/journal/40572) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Current Hepatology Reports                                                                 |[11901](https://link.springer.com/journal/11901) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Current Psychology                                                                         |[12144](https://link.springer.com/journal/12144) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Current Sexual Health Reports                                                              |[11930](https://link.springer.com/journal/11930) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Current Treatment Options in Oncology                                                      |[11864](https://link.springer.com/journal/11864) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Deutsche Vierteljahrsschrift für Literaturwissenschaft und Geistesgeschichte               |[41245](https://link.springer.com/journal/41245) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Der Diabetologe                                                                            |[11428](https://link.springer.com/journal/11428) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|e & i Elektrotechnik und Informationstechnik                                               |[502](https://link.springer.com/journal/502)     |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Ecological Research                                                                        |[11284](https://link.springer.com/journal/11284) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Economic Theory Bulletin                                                                   |[40505](https://link.springer.com/journal/40505) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Ecosystems                                                                                 |[10021](https://link.springer.com/journal/10021) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Endocrine                                                                                  |[12020](https://link.springer.com/journal/12020) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Environmental and Ecological Statistics                                                    |[10651](https://link.springer.com/journal/10651) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|EURO Journal on Transportation and Logistics                                               |[13676](https://link.springer.com/journal/13676) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|European Food Research and Technology                                                      |[217](https://link.springer.com/journal/217)     |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|European Journal of Ageing                                                                 |[10433](https://link.springer.com/journal/10433) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|The European Physical Journal B                                                            |[10051](https://link.springer.com/journal/10051) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|European Surgery                                                                           |[10353](https://link.springer.com/journal/10353) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Evolutionary Ecology                                                                       |[10682](https://link.springer.com/journal/10682) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Food Engineering Reviews                                                                   |[12393](https://link.springer.com/journal/12393) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Food Science and Biotechnology                                                             |[10068](https://link.springer.com/journal/10068) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Foundations of Chemistry                                                                   |[10698](https://link.springer.com/journal/10698) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Genes & Genomics                                                                           |[13258](https://link.springer.com/journal/13258) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Geometric and Functional Analysis                                                          |[39](https://link.springer.com/journal/39)       |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Health Care Analysis                                                                       |[10728](https://link.springer.com/journal/10728) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Heart and Vessels                                                                          |[380](https://link.springer.com/journal/380)     |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Hyperfine Interactions                                                                     |[10751](https://link.springer.com/journal/10751) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Indian Journal of Gastroenterology                                                         |[12664](https://link.springer.com/journal/12664) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Indian Journal of Hematology and Blood Transfusion                                         |[12288](https://link.springer.com/journal/12288) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Information Systems Frontiers                                                              |[10796](https://link.springer.com/journal/10796) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Internal and Emergency Medicine                                                            |[11739](https://link.springer.com/journal/11739) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal of Automation and Computing                                          |[11633](https://link.springer.com/journal/11633) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|International Journal of Diabetes in Developing Countries                                  |[13410](https://link.springer.com/journal/13410) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|International Journal of Early Childhood                                                   |[13158](https://link.springer.com/journal/13158) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal of Historical Archaeology                                            |[10761](https://link.springer.com/journal/10761) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|International Journal of Mental Health and Addiction                                       |[11469](https://link.springer.com/journal/11469) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|International Journal of Plant Production                                                  |[42106](https://link.springer.com/journal/42106) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal of the Sociology of Leisure                                          |[41978](https://link.springer.com/journal/41978) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|International Review of Economics                                                          |[12232](https://link.springer.com/journal/12232) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Iran Journal of Computer Science                                                           |[42044](https://link.springer.com/journal/42044) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Israel Journal of Mathematics                                                              |[11856](https://link.springer.com/journal/11856) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Agricultural, Biological and Environmental Statistics                           |[13253](https://link.springer.com/journal/13253) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Applied Mathematics and Computing                                               |[12190](https://link.springer.com/journal/12190) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal für Ästhetische Chirurgie                                                          |[12631](https://link.springer.com/journal/12631) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Bionic Engineering                                                              |[42235](https://link.springer.com/journal/42235) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Chinese Political Science                                                       |[11366](https://link.springer.com/journal/11366) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Classification                                                                  |[357](https://link.springer.com/journal/357)     |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Computational Social Science                                                    |[42001](https://link.springer.com/journal/42001) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Developmental and Life Course Criminology                                       |[40865](https://link.springer.com/journal/40865) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Developmental and Physical Disabilities                                         |[10882](https://link.springer.com/journal/10882) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Elasticity                                                                      |[10659](https://link.springer.com/journal/10659) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Fetal Medicine                                                                  |[40556](https://link.springer.com/journal/40556) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Food Measurement and Characterization                                           |[11694](https://link.springer.com/journal/11694) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of General Plant Pathology                                                         |[10327](https://link.springer.com/journal/10327) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Heuristics                                                                      |[10732](https://link.springer.com/journal/10732) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Immigrant and Minority Health                                                   |[10903](https://link.springer.com/journal/10903) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Inherited Metabolic Disease                                                     |[10545](https://link.springer.com/journal/10545) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Insect Behavior                                                                 |[10905](https://link.springer.com/journal/10905) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Iron and Steel Research International                                           |[42243](https://link.springer.com/journal/42243) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Marine Science and Application                                                  |[11804](https://link.springer.com/journal/11804) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Mathematical Biology                                                            |[285](https://link.springer.com/journal/285)     |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Micro-Bio Robotics                                                              |[12213](https://link.springer.com/journal/12213) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Neurology                                                                       |[415](https://link.springer.com/journal/415)     |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Nuclear Cardiology                                                              |[12350](https://link.springer.com/journal/12350) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Paleolimnology                                                                  |[10933](https://link.springer.com/journal/10933) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Population Ageing                                                               |[12062](https://link.springer.com/journal/12062) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Productivity Analysis                                                           |[11123](https://link.springer.com/journal/11123) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Rational-Emotive & Cognitive-Behavior Therapy                                   |[10942](https://link.springer.com/journal/10942) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Statistical Physics                                                             |[10955](https://link.springer.com/journal/10955) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|The Journal of Supercomputing                                                              |[11227](https://link.springer.com/journal/11227) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Ultrasound                                                                      |[40477](https://link.springer.com/journal/40477) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Lasers in Dental Science                                                                   |[41547](https://link.springer.com/journal/41547) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Lettera Matematica                                                                         |[40329](https://link.springer.com/journal/40329) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Letters in Spatial and Resource Sciences                                                   |[12076](https://link.springer.com/journal/12076) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Managementforschung                                                                        |[41113](https://link.springer.com/journal/41113) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Maritime Studies                                                                           |[40152](https://link.springer.com/journal/40152) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Maternal and Child Health Journal                                                          |[10995](https://link.springer.com/journal/10995) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Mathematical Physics, Analysis and Geometry                                                |[11040](https://link.springer.com/journal/11040) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Metallurgical and Materials Transactions B                                                 |[11663](https://link.springer.com/journal/11663) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Metascience                                                                                |[11016](https://link.springer.com/journal/11016) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Meteorology and Atmospheric Physics                                                        |[703](https://link.springer.com/journal/703)     |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Motivation and Emotion                                                                     |[11031](https://link.springer.com/journal/11031) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Multidimensional Systems and Signal Processing                                             |[11045](https://link.springer.com/journal/11045) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Multimedia Systems                                                                         |[530](https://link.springer.com/journal/530)     |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Networks and Spatial Economics                                                             |[11067](https://link.springer.com/journal/11067) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Neurochemical Research                                                                     |[11064](https://link.springer.com/journal/11064) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|neurogenetics                                                                              |[10048](https://link.springer.com/journal/10048) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Ocean Dynamics                                                                             |[10236](https://link.springer.com/journal/10236) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Operational Research                                                                       |[12351](https://link.springer.com/journal/12351) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Optical Review                                                                             |[10043](https://link.springer.com/journal/10043) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Organizational Design and Enterprise Engineering                                           |[41251](https://link.springer.com/journal/41251) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Parasitology Research                                                                      |[436](https://link.springer.com/journal/436)     |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Pediatric Radiology                                                                        |[247](https://link.springer.com/journal/247)     |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Photosynthetica                                                                            |[11099](https://link.springer.com/journal/11099) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Plant Biotechnology Reports                                                                |[11816](https://link.springer.com/journal/11816) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Polar Biology                                                                              |[300](https://link.springer.com/journal/300)     |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Population Ecology                                                                         |[10144](https://link.springer.com/journal/10144) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Population Research and Policy Review                                                      |[11113](https://link.springer.com/journal/11113) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Proceedings of the National Academy of Sciences, India Section A: Physical Sciences        |[40010](https://link.springer.com/journal/40010) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|psychopraxis. neuropraxis                                                                  |[739](https://link.springer.com/journal/739)     |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Qualitative Theory of Dynamical Systems                                                    |[12346](https://link.springer.com/journal/12346) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Quantum Studies: Mathematics and Foundations                                               |[40509](https://link.springer.com/journal/40509) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Raumforschung und Raumordnung &#124;  Spatial Research and Planning                        |[13147](https://link.springer.com/journal/13147) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Review of Agricultural, Food and Environmental Studies                                     |[41130](https://link.springer.com/journal/41130) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Review of Industrial Organization                                                          |[11151](https://link.springer.com/journal/11151) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|rheuma plus                                                                                |[12688](https://link.springer.com/journal/12688) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|La Rivista Italiana della Medicina di Laboratorio - Italian Journal of Laboratory Medicine |[13631](https://link.springer.com/journal/13631) |FALSE     |TRUE  |TRUE        |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Science China Physics, Mechanics & Astronomy                                               |[11433](https://link.springer.com/journal/11433) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Silicon                                                                                    |[12633](https://link.springer.com/journal/12633) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Socio-Ecological Practice Research                                                         |[42532](https://link.springer.com/journal/42532) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Sophia                                                                                     |[11841](https://link.springer.com/journal/11841) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Strahlentherapie und Onkologie                                                             |[66](https://link.springer.com/journal/66)       |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Surveys in Geophysics                                                                      |[10712](https://link.springer.com/journal/10712) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Systematic Parasitology                                                                    |[11230](https://link.springer.com/journal/11230) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Theory in Biosciences                                                                      |[12064](https://link.springer.com/journal/12064) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Topoi                                                                                      |[11245](https://link.springer.com/journal/11245) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Trauma und Berufskrankheit                                                                 |[10039](https://link.springer.com/journal/10039) |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Der Urologe                                                                                |[120](https://link.springer.com/journal/120)     |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Virologica Sinica                                                                          |[12250](https://link.springer.com/journal/12250) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Wiener klinisches Magazin                                                                  |[740](https://link.springer.com/journal/740)     |TRUE      |TRUE  |TRUE        |TRUE  |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|Zeitschrift für Arbeitswissenschaft                                                        |[41449](https://link.springer.com/journal/41449) |TRUE      |TRUE  |FALSE       |TRUE  |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Zeitschrift für Energiewirtschaft                                                          |[12398](https://link.springer.com/journal/12398) |TRUE      |TRUE  |TRUE        |TRUE  |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Advances in Therapy                                                                        |[12325](https://link.springer.com/journal/12325) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Algebra universalis                                                                        |[12](https://link.springer.com/journal/12)       |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|American Journal of Cardiovascular Drugs                                                   |[40256](https://link.springer.com/journal/40256) |TRUE      |FALSE |FALSE       |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|American Journal of Clinical Dermatology                                                   |[40257](https://link.springer.com/journal/40257) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Annals of Solid and Structural Mechanics                                                   |[12356](https://link.springer.com/journal/12356) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Applied Health Economics and Health Policy                                                 |[40258](https://link.springer.com/journal/40258) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Archive for Mathematical Logic                                                             |[153](https://link.springer.com/journal/153)     |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Astrodynamics                                                                              |[42064](https://link.springer.com/journal/42064) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|BioDrugs                                                                                   |[40259](https://link.springer.com/journal/40259) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Biology and Fertility of Soils                                                             |[374](https://link.springer.com/journal/374)     |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Bulletin of the Iranian Mathematical Society                                               |[41980](https://link.springer.com/journal/41980) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Canadian Journal of Anesthesia/Journal canadien d'anesthésie                               |[12630](https://link.springer.com/journal/12630) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Cell and Tissue Banking                                                                    |[10561](https://link.springer.com/journal/10561) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Clean Technologies and Environmental Policy                                                |[10098](https://link.springer.com/journal/10098) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Clinical Drug Investigation                                                                |[40261](https://link.springer.com/journal/40261) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Clinical Pharmacokinetics                                                                  |[40262](https://link.springer.com/journal/40262) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|CNS Drugs                                                                                  |[40263](https://link.springer.com/journal/40263) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Computational Brain & Behavior                                                             |[42113](https://link.springer.com/journal/42113) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Criminal Law Forum                                                                         |[10609](https://link.springer.com/journal/10609) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Current Hypertension Reports                                                               |[11906](https://link.springer.com/journal/11906) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Current Treatment Options in Neurology                                                     |[11940](https://link.springer.com/journal/11940) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Digestive Diseases and Sciences                                                            |[10620](https://link.springer.com/journal/10620) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Drug Safety                                                                                |[40264](https://link.springer.com/journal/40264) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Drugs                                                                                      |[40265](https://link.springer.com/journal/40265) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Drugs & Aging                                                                              |[40266](https://link.springer.com/journal/40266) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Drugs & Therapy Perspectives                                                               |[40267](https://link.springer.com/journal/40267) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Dysphagia                                                                                  |[455](https://link.springer.com/journal/455)     |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Emergent Materials                                                                         |[42247](https://link.springer.com/journal/42247) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Ethical Theory and Moral Practice                                                          |[10677](https://link.springer.com/journal/10677) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|European Journal of Drug Metabolism and Pharmacokinetics                                   |[13318](https://link.springer.com/journal/13318) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|European Journal of Pediatrics                                                             |[431](https://link.springer.com/journal/431)     |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Feminist Legal Studies                                                                     |[10691](https://link.springer.com/journal/10691) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Frontiers of Information Technology & Electronic Engineering                               |[11714](https://link.springer.com/journal/11714) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Gold Bulletin                                                                              |[13404](https://link.springer.com/journal/13404) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Hernia                                                                                     |[10029](https://link.springer.com/journal/10029) |TRUE      |FALSE |FALSE       |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|High Blood Pressure & Cardiovascular Prevention                                            |[40292](https://link.springer.com/journal/40292) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Hormones                                                                                   |[42000](https://link.springer.com/journal/42000) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Indian Journal of Plant Physiology                                                         |[40502](https://link.springer.com/journal/40502) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Intensive Care Medicine                                                                    |[134](https://link.springer.com/journal/134)     |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|International Economics and Economic Policy                                                |[10368](https://link.springer.com/journal/10368) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|International Journal of Economic Policy Studies                                           |[42495](https://link.springer.com/journal/42495) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|International Journal for Philosophy of Religion                                           |[11153](https://link.springer.com/journal/11153) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Inventiones mathematicae                                                                   |[222](https://link.springer.com/journal/222)     |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal d'Analyse Mathématique                                                             |[11854](https://link.springer.com/journal/11854) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Business Ethics                                                                 |[10551](https://link.springer.com/journal/10551) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Computers in Education                                                          |[40692](https://link.springer.com/journal/40692) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Electronic Materials                                                            |[11664](https://link.springer.com/journal/11664) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Genetic Counseling                                                              |[10897](https://link.springer.com/journal/10897) |FALSE     |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Insect Conservation                                                             |[10841](https://link.springer.com/journal/10841) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Mathematical Chemistry                                                          |[10910](https://link.springer.com/journal/10910) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|The journal of nutrition, health & aging                                                   |[12603](https://link.springer.com/journal/12603) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|The Journal of Primary Prevention                                                          |[10935](https://link.springer.com/journal/10935) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Journal of Statistical Theory and Practice                                                 |[42519](https://link.springer.com/journal/42519) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Landslides                                                                                 |[10346](https://link.springer.com/journal/10346) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Manuelle Medizin                                                                           |[337](https://link.springer.com/journal/337)     |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Medizinische Klinik - Intensivmedizin und Notfallmedizin                                   |[63](https://link.springer.com/journal/63)       |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Modeling Earth Systems and Environment                                                     |[40808](https://link.springer.com/journal/40808) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Molecular Diagnosis & Therapy                                                              |[40291](https://link.springer.com/journal/40291) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Natural Hazards                                                                            |[11069](https://link.springer.com/journal/11069) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Nexus Network Journal                                                                      |[4](https://link.springer.com/journal/4)         |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Organic Agriculture                                                                        |[13165](https://link.springer.com/journal/13165) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Osteoporosis International                                                                 |[198](https://link.springer.com/journal/198)     |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|The Patient - Patient-Centered Outcomes Research                                           |[40271](https://link.springer.com/journal/40271) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Pediatric Drugs                                                                            |[40272](https://link.springer.com/journal/40272) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Pharmaceutical Medicine                                                                    |[40290](https://link.springer.com/journal/40290) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |FALSE  |FALSE   |FALSE   |FALSE  |
|PharmacoEconomics                                                                          |[40273](https://link.springer.com/journal/40273) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|PharmacoEconomics Spanish Research Articles                                                |[40277](https://link.springer.com/journal/40277) |FALSE     |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Photosynthesis Research                                                                    |[11120](https://link.springer.com/journal/11120) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Prävention und Gesundheitsförderung                                                        |[11553](https://link.springer.com/journal/11553) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Quality & Quantity                                                                         |[11135](https://link.springer.com/journal/11135) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Results in Mathematics                                                                     |[25](https://link.springer.com/journal/25)       |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Der Schmerz                                                                                |[482](https://link.springer.com/journal/482)     |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Social Indicators Research                                                                 |[11205](https://link.springer.com/journal/11205) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Studia Logica                                                                              |[11225](https://link.springer.com/journal/11225) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Supportive Care in Cancer                                                                  |[520](https://link.springer.com/journal/520)     |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Targeted Oncology                                                                          |[11523](https://link.springer.com/journal/11523) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Theory and Society                                                                         |[11186](https://link.springer.com/journal/11186) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|User Modeling and User-Adapted Interaction                                                 |[11257](https://link.springer.com/journal/11257) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|ZDM                                                                                        |[11858](https://link.springer.com/journal/11858) |TRUE      |FALSE |TRUE        |FALSE |TRUE    |TRUE   |TRUE    |TRUE    |TRUE   |
|Acta Mathematica Scientia                                                                  |[10473](https://link.springer.com/journal/10473) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Acta Neuropathologica                                                                      |[401](https://link.springer.com/journal/401)     |TRUE      |FALSE |TRUE        |FALSE |FALSE   |TRUE   |TRUE    |TRUE    |TRUE   |
|Acta Pharmacologica Sinica                                                                 |[41401](https://link.springer.com/journal/41401) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Acta Politica                                                                              |[41269](https://link.springer.com/journal/41269) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Advanced Fiber Materials                                                                   |[42765](https://link.springer.com/journal/42765) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Aerotecnica Missili & Spazio                                                               |[42496](https://link.springer.com/journal/42496) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|American Journal of Cultural Sociology                                                     |[41290](https://link.springer.com/journal/41290) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Asian Business & Management                                                                |[41291](https://link.springer.com/journal/41291) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Behavior and Social Issues                                                                 |[42822](https://link.springer.com/journal/42822) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Biochar                                                                                    |[42773](https://link.springer.com/journal/42773) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|BioSocieties                                                                               |[41292](https://link.springer.com/journal/41292) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Bone Marrow Transplantation                                                                |[41409](https://link.springer.com/journal/41409) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Brazilian Journal of Microbiology                                                          |[42770](https://link.springer.com/journal/42770) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|British Dental Journal                                                                     |[41415](https://link.springer.com/journal/41415) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|British Journal of Cancer                                                                  |[41416](https://link.springer.com/journal/41416) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|British Politics                                                                           |[41293](https://link.springer.com/journal/41293) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Canadian Studies in Population                                                             |[42650](https://link.springer.com/journal/42650) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Cancer Gene Therapy                                                                        |[41417](https://link.springer.com/journal/41417) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Carbon Letters                                                                             |[42823](https://link.springer.com/journal/42823) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Cell Death & Differentiation                                                               |[41418](https://link.springer.com/journal/41418) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Cell Research                                                                              |[41422](https://link.springer.com/journal/41422) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Cellular & Molecular Immunology                                                            |[41423](https://link.springer.com/journal/41423) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Chemistry Africa                                                                           |[42250](https://link.springer.com/journal/42250) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Clays and Clay Minerals                                                                    |[42860](https://link.springer.com/journal/42860) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Comparative Economic Studies                                                               |[41294](https://link.springer.com/journal/41294) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Comparative European Politics                                                              |[41295](https://link.springer.com/journal/41295) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Contemporary Political Theory                                                              |[41296](https://link.springer.com/journal/41296) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Crime Prevention and Community Safety                                                      |[41300](https://link.springer.com/journal/41300) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Digital Finance                                                                            |[42521](https://link.springer.com/journal/42521) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|East Asian Community Review                                                                |[42215](https://link.springer.com/journal/42215) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|European Journal of Clinical Nutrition                                                     |[41430](https://link.springer.com/journal/41430) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|The European Journal of Development Research                                               |[41287](https://link.springer.com/journal/41287) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|European Journal of Human Genetics                                                         |[41431](https://link.springer.com/journal/41431) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|European Political Science                                                                 |[41304](https://link.springer.com/journal/41304) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Eye                                                                                        |[41433](https://link.springer.com/journal/41433) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|French Politics                                                                            |[41253](https://link.springer.com/journal/41253) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Gene Therapy                                                                               |[41434](https://link.springer.com/journal/41434) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Genes & Immunity                                                                           |[41435](https://link.springer.com/journal/41435) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Genetics in Medicine                                                                       |[41436](https://link.springer.com/journal/41436) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|The Geneva Papers on Risk and Insurance - Issues and Practice                              |[41288](https://link.springer.com/journal/41288) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|The Geneva Risk and Insurance Review                                                       |[10713](https://link.springer.com/journal/10713) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Heredity                                                                                   |[41437](https://link.springer.com/journal/41437) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Hypertension Research                                                                      |[41440](https://link.springer.com/journal/41440) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Interest Groups & Advocacy                                                                 |[41309](https://link.springer.com/journal/41309) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal on Child Maltreatment: Research, Policy and Practice                 |[42448](https://link.springer.com/journal/42448) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal of Community Well-Being                                              |[42413](https://link.springer.com/journal/42413) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal of Disclosure and Governance                                         |[41310](https://link.springer.com/journal/41310) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal of Global Business and Competitiveness                               |[42943](https://link.springer.com/journal/42943) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal of Impotence Research                                                |[41443](https://link.springer.com/journal/41443) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal of Obesity                                                           |[41366](https://link.springer.com/journal/41366) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal of Tropical Insect Science                                           |[42690](https://link.springer.com/journal/42690) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|International Politics                                                                     |[41311](https://link.springer.com/journal/41311) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|The ISME Journal                                                                           |[41396](https://link.springer.com/journal/41396) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|JMST Advances                                                                              |[42791](https://link.springer.com/journal/42791) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|The Journal of Antibiotics                                                                 |[41429](https://link.springer.com/journal/41429) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Arid Land                                                                       |[40333](https://link.springer.com/journal/40333) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Asset Management                                                                |[41260](https://link.springer.com/journal/41260) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Banking and Financial Technology                                                |[42786](https://link.springer.com/journal/42786) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Banking Regulation                                                              |[41261](https://link.springer.com/journal/41261) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Biosystems Engineering                                                          |[42853](https://link.springer.com/journal/42853) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Brand Management                                                                |[41262](https://link.springer.com/journal/41262) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Electrical Engineering & Technology                                             |[42835](https://link.springer.com/journal/42835) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Exposure Science & Environmental Epidemiology                                   |[41370](https://link.springer.com/journal/41370) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Financial Services Marketing                                                    |[41264](https://link.springer.com/journal/41264) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Human Genetics                                                                  |[10038](https://link.springer.com/journal/10038) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Human Hypertension                                                              |[41371](https://link.springer.com/journal/41371) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of International Business Policy                                                   |[42214](https://link.springer.com/journal/42214) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of International Business Studies                                                  |[41267](https://link.springer.com/journal/41267) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Marketing Analytics                                                             |[41270](https://link.springer.com/journal/41270) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Oceanology and Limnology                                                        |[343](https://link.springer.com/journal/343)     |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Parasitic Diseases                                                              |[12639](https://link.springer.com/journal/12639) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Pediatric Endoscopic Surgery                                                    |[42804](https://link.springer.com/journal/42804) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Peridynamics and Nonlocal Modeling                                              |[42102](https://link.springer.com/journal/42102) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Perinatology                                                                    |[41372](https://link.springer.com/journal/41372) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Plant Biochemistry and Biotechnology                                            |[13562](https://link.springer.com/journal/13562) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Proteins and Proteomics                                                         |[42485](https://link.springer.com/journal/42485) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Public Health Policy                                                            |[41271](https://link.springer.com/journal/41271) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Revenue and Pricing Management                                                  |[41272](https://link.springer.com/journal/41272) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Rubber Research                                                                 |[42464](https://link.springer.com/journal/42464) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Soil Science and Plant Nutrition                                                |[42729](https://link.springer.com/journal/42729) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal of Transatlantic Studies                                                           |[42738](https://link.springer.com/journal/42738) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|KN - Journal of Cartography and Geographic Information                                     |[42489](https://link.springer.com/journal/42489) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Laboratory Investigation                                                                   |[41374](https://link.springer.com/journal/41374) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Latino Studies                                                                             |[41276](https://link.springer.com/journal/41276) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Leukemia                                                                                   |[41375](https://link.springer.com/journal/41375) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Maritime Economics & Logistics                                                             |[41278](https://link.springer.com/journal/41278) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Materials Circular Economy                                                                 |[42824](https://link.springer.com/journal/42824) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Modern Pathology                                                                           |[41379](https://link.springer.com/journal/41379) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Molecular Psychiatry                                                                       |[41380](https://link.springer.com/journal/41380) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Mucosal Immunology                                                                         |[41385](https://link.springer.com/journal/41385) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Neuropsychopharmacology                                                                    |[41386](https://link.springer.com/journal/41386) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Oncogene                                                                                   |[41388](https://link.springer.com/journal/41388) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Pediatric Research                                                                         |[41390](https://link.springer.com/journal/41390) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|The Pharmacogenomics Journal                                                               |[41397](https://link.springer.com/journal/41397) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Physiology and Molecular Biology of Plants                                                 |[12298](https://link.springer.com/journal/12298) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Place Branding and Public Diplomacy                                                        |[41254](https://link.springer.com/journal/41254) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Polymer Journal                                                                            |[41428](https://link.springer.com/journal/41428) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|postmedieval                                                                               |[41280](https://link.springer.com/journal/41280) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Proceedings of the Zoological Society                                                      |[12595](https://link.springer.com/journal/12595) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Prostate Cancer and Prostatic Diseases                                                     |[41391](https://link.springer.com/journal/41391) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Psychometrika                                                                              |[11336](https://link.springer.com/journal/11336) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Psychotherapie Forum                                                                       |[729](https://link.springer.com/journal/729)     |TRUE      |FALSE |FALSE       |TRUE  |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Research on Biomedical Engineering                                                         |[42600](https://link.springer.com/journal/42600) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Risk Management                                                                            |[41283](https://link.springer.com/journal/41283) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Security Journal                                                                           |[41284](https://link.springer.com/journal/41284) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|SN Applied Sciences                                                                        |[42452](https://link.springer.com/journal/42452) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|SN Comprehensive Clinical Medicine                                                         |[42399](https://link.springer.com/journal/42399) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Social Theory & Health                                                                     |[41285](https://link.springer.com/journal/41285) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Soil Ecology Letters                                                                       |[42832](https://link.springer.com/journal/42832) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Spinal Cord                                                                                |[41393](https://link.springer.com/journal/41393) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Spinal Cord Series and Cases                                                               |[41394](https://link.springer.com/journal/41394) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Subjectivity                                                                               |[41286](https://link.springer.com/journal/41286) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Sugar Tech                                                                                 |[12355](https://link.springer.com/journal/12355) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|URBAN DESIGN International                                                                 |[41289](https://link.springer.com/journal/41289) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Vegetos                                                                                    |[42535](https://link.springer.com/journal/42535) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|VirusDisease                                                                               |[13337](https://link.springer.com/journal/13337) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Waste Disposal & Sustainable Energy                                                        |[42768](https://link.springer.com/journal/42768) |TRUE      |FALSE |FALSE       |FALSE |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Zoomorphology                                                                              |[435](https://link.springer.com/journal/435)     |TRUE      |FALSE |FALSE       |TRUE  |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Helgoland Marine Research                                                                  |[10152](https://link.springer.com/journal/10152) |FALSE     |FALSE |FALSE       |TRUE  |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Genes & Nutrition                                                                          |[12263](https://link.springer.com/journal/12263) |FALSE     |FALSE |FALSE       |TRUE  |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Journal for Labour Market Research                                                         |[12651](https://link.springer.com/journal/12651) |FALSE     |FALSE |FALSE       |TRUE  |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|International Journal of Educational Technology in Higher Education                        |[41239](https://link.springer.com/journal/41239) |FALSE     |FALSE |FALSE       |TRUE  |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Gynecological Surgery                                                                      |[10397](https://link.springer.com/journal/10397) |FALSE     |FALSE |FALSE       |TRUE  |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |
|Environmental Health and Preventive Medicine                                               |[12199](https://link.springer.com/journal/12199) |FALSE     |FALSE |FALSE       |TRUE  |FALSE   |FALSE  |FALSE   |FALSE   |FALSE  |

### 5. Results

Key insights from the filtering table are:

- There are significant differences both between the eligibility lists and the catalogue. 
- The combined list consists of 2015 entries, which is surprising, as the list of hybrid journals filtered from the Springer catalogue only contains 1996 entries - there are 19 journals which appear in some of the SCA eligibility lists, but not in the official catalogue. 
A closer investigation reveals that a lot of those cases are related to journals having been transferred to other publishers in the beginning of 2019. This indicates that the eligibility lists are not updated frequently (or not at all?).
- The Swedish, Hungarian, Polish and Finnish eligibilty lists are identical. While the latter cases can be explained with a common start date (They all came into effect in 2019), it is unclear why they are identical to the Swedish list, with the corresponding SCA already running since 2016. It seems as if the Swedish list was used as a template for the new SCAs.

</div>
</body>
</html>
