# auto-ria scraper to csv
![python](https://img.shields.io/badge/python-3.7~3.11-blue?style=flat-square)
![pandas](https://img.shields.io/badge/pandas-1.5.3%20-orange?style=flat-square)
![bs4](https://img.shields.io/badge/bs4-4.11.2%20-orange?style=flat-square)
![bs4](https://img.shields.io/badge/environs-9.5.0%20-orange?style=flat-square)
![bs4](https://img.shields.io/badge/requests-2.28.2%20-orange?style=flat-square)


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project was made for analyzing different cars in different categories from [website](https://auto.ria.com/)
to help my friend pick up a new a car with definite settings. <br> 
> In the end I gained valueable experience with setting deadlines properly :)

## Technologies
During this project I used `pandas` for exporting scraped data to csv format, `environs` to store my secrets, `requests` to get responses from the website and `bs4` for convenient scrapping. 

## Setup
To run this project, install it locally using pip or any other package managers such as pipenv, poetry etc.:

### Install using `pip`
```bash
$ git clone https://github.com/surgeonofdeaths/auto-ria-parser-to-excel.git
$ cd auto-ria-parser-to-excel
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```
### Install using `poetry`
```bash
$ git clone https://github.com/surgeonofdeaths/auto-ria-parser-to-excel.git
$ cd auto-ria-parser-to-excel
$ poetry shell
$ poetry install
```
To edit configuration of the app you need to change ".env" file
