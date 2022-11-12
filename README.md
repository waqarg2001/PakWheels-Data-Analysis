<p align='center'>
<img src='https://github.com/waqarg2001/PakWheels-Data-Analysis/blob/7b23ca6ab3df0c13053a73f5a91e5544becd2ff0/resources/Sales%20Data.png' width=600 height=250 >
</p>

---

<h4 align='center'> Application of ETL process on raw <a href='https://www.amazon.com/' target='_blank'>Aamazon</a> sales data along with its analysis using <a href='jupyter.org' target='_blank'>Jupyter</a> Notebook and <a href='tableau.com' target='_blank'>Tableau</a> for a dashboard. </h4>

<p align='center'>
<img src="https://i.ibb.co/KxfMMsP/built-with-love.png" alt="built-with-love" border="0">
<img src="https://i.ibb.co/MBDK1Pk/powered-by-coffee.png" alt="powered-by-coffee" border="0">
<img src="https://i.ibb.co/CtGqhQH/cc-nc-sa.png" alt="cc-nc-sa" border="0">
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#tools">Tools</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#demo">Demo</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
</p>


## Overview

<p><a href='Amazon.com' target='_blank'>Amazon</a> is the world's largest eCommerce website. It was originally launched as a book-selling website and sold its first book in 1995.</p>

This project involves Extract Transform Load(ETL) process on fictious raw sales data of Amazon. Exploratory Data Analysis(EDA) is performed on it using Jupyter Notebook to extract key insights about the sales and later on an executive's sales dashbaord is produced using Tableau.

The repository directory structure is as follows:

```
├── LICENSE 
├── README.md          <- The top-level README for developers using this project. 
| 
├── run.py             <- Python script to start ETL process. 
| 
├── data
│   ├── interim        <- Intermediate data that has been transformed using ETL process.
│   ├── processed      <- The final, canonical data set for analysis.
│   └── raw            <- The original, immutable data dump. 
│ 
│ 
│ 
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-mwg-initial-data-exploration`. 
│
│ 
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt` 
| 
│ 
├── src                <- Source code for use in this project. 
│   ├── __init__.py    <- Makes src a Python module. 
│   │ 
│   ├── data           <- Scripts to perform ETL. 
│       ├── make_dataset.py 
|       └── multiple_files_to_single_excel_file.py 
| 
| 
├── dashboard          <- Dashboard created using transformed data. 
|   └── Sales Dashboard.twbx 
| 
├── resources          <- Resources for this readme file. 
```

## Tools 

To build this project, following tools and packages were used:

- Python
- Python packages mentioned in [requirements.txt](https://github.com/waqarg2001/Amazon-Sales-Data-Analysis/blob/master/requirements.txt).
- PyCharm
- Github
- Jupyter Notebook
- Tableau Desktop

## Architecture

The architecture of this project is straightforward which can be understood by the following diagram.

<p align='center'>
  <img src='https://github.com/waqarg2001/PakWheels-Data-Analysis/blob/7b23ca6ab3df0c13053a73f5a91e5544becd2ff0/resources/architecture.gif' height=280 width=900>
</p>  

According to the diagram we first create a python script which performs ETL for us on the raw dataset. The output of this process is clean data which is then used for exploratory analysis in jupyter Notebook and to create a dashboard in Python.


## Demo

The figure below shows a snapshot of ETL process being conducted through terminal. Type run.py (raw data directory). In my case I typed run.py data/raw.
(figure may take few seconds to load)

<p align='center'>
  <img src='https://github.com/waqarg2001/PakWheels-Data-Analysis/blob/b195a77dc208fe9c668df46433f213108ae63008/resources/pakwheels%20etl.gif' width=800 height=400>
</p>  




## Support

If you have any doubts, queries or, suggestions then, please connect with me on any of the following platforms:

[![Linkedin Badge][linkedinbadge]][linkedin] 
[![Gmail Badge][gmailbadge]][gmail]


## License

<a href = 'https://creativecommons.org/licenses/by-nc-sa/4.0/' target="_blank">
    <img src="https://i.ibb.co/mvmWGkm/by-nc-sa.png" alt="by-nc-sa" border="0" width="88" height="31">
</a>

This license allows reusers to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution is given to the creator. If you remix, adapt, or build upon the material, you must license the modified material under identical terms.



<!--Profile Link-->
[linkedin]: https://www.linkedin.com/in/waqargul
[gmail]: mailto:waqargul6@gmail.com

<!--Logo Link -->
[linkedinbadge]: https://img.shields.io/badge/waqargul-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[gmailbadge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
