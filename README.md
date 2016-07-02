<h1 align="center">
    <br>
        doc-diff
    <br>
  <h4 align="center">Generate the diff data between two files</h4>
</h1>

<p align="center">
  <a href="https://github.com/Renien/doc-diff/blob/master/LICENSE">
    <img src="https://img.shields.io/npm/l/express.svg?maxAge=2592000&style=flat-square"
         alt="License">
  </a>
  <a href="https://travis-ci.org/Renien/doc-diff">
    <img src="https://travis-ci.org/Renien/doc-diff.svg?branch=master"
         alt="Travis Build">
  </a>
</p>

## Summary

Implementation was started mainly focusing as a support app for **Data Science** work. The current implementation helps to analyse recommendations ‘CSV’ files. (i.e If you need to analyse two algorithm results this lib will be very handy)

## Recommendation Format
The CSV file contains list of **key-value** in each line. The key is product (productCode/porductID) and the value is list of recommended products (productCode/porductID). The product code and the recommendation list is separated with _**‘TAB’**_.

```
Sample Recommendation 
---------------------
1098808	1597549,1974410,1850731
1161889	1095554
1706909	2078866
1815368	2215327
1847624	2179582,2085753
```

## Installation
```
$ pip install doc-diff
```

## Features
- Generate the following comparison reports 
    - common_in_doc1-and-doc2-%Y-%m-%d.csv  
    - common_key_with_diff_values-%Y-%m-%d.csv  
    - exclusive_in_doc1-%Y-%m-%d.csv
    - exclusive_in_doc2-%Y-%m-%d.csv
- Compare two files and return following **'dicts(prodCode, recommendation)'**
    - common_in_doc1_and_doc2_list = dicts()
    - common_key_with_diff_values_list = dicts()
    - exclusive_in_doc1_list = dicts()
    - exclusive_in_doc2_list = dicts()

## Usage

- Allow to generate the evaluation result files
- Able to extract the comparsion results as key-value list 
    - Using the diifferent dictionary objects you can present the results as you like (i.e Graphs, Venn diagram) 

## Comparison Report Format 

- In CSV file each line contains the product code and the corresponding recommendation. The product code and the recommendation list is separated with **‘TAB’**.
- In **‘common_key_with_diff_values-%Y-%m-%d.csv’** file the result format is slightly different. To show the un-matching recommendation in each line after product code TAB separation you will find the result of **‘A’ algorithm** and the **‘B' algorithm** result separated with two pipes **‘||’**.

```
Sample common_key_with_diff_values-%Y-%m-%d.csv 
------------------------------------------------
c36623	2256360,2398464,2503472,c27214||2256360,2398464,2503472,c27214,c79033
c973955	1965886,c340951,c752950,c973951||1965886,c24224,c340951,c752950,c906950,c973951
c25749	c25982||c205950,c25982,c65977
```

## Package Directory Layout

```
doc-diff
├── LICENSE                         # Contains License Agreement file
├── README.md                       # Contains the details of doc-diff lib
├── doc_diff                        # Root package 
│   ├── Diff.py                     # Diff class
│   ├── __init__.py                 # Package declaration 
├── setup.py                        # Setup file for packaging 
└── test                            # Test module (Includes the useage)
    ├── __init__.py                 # Package declaration 
    ├── data                        # Sample data
    │   ├── a-priori.csv            # A-Priori algo results
    │   └── pfp.csv                 # FP-Growth algo results
    └── doc_diff_app.py             # Main method file 
```

## Contribute
NEED TO CHANGE !!
For any problem/question or if you think a feature that could make doc-diff lib more useful, do not hesitate to open an issue.

## License
MIT © [Renien](https://twitter.com/RenienJoseph)