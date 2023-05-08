# auto-ria scraper to csv
![python](https://img.shields.io/badge/python-3.7~3.11-blue?style=flat-square)
![pandas](https://img.shields.io/badge/pandas-1.5.3%20-orange?style=flat-square)
![pydantic](https://img.shields.io/badge/pydantic-^1.10.7%20-orange?style=flat-square)
![bs4](https://img.shields.io/badge/bs4-4.11.2%20-orange?style=flat-square)
![environs](https://img.shields.io/badge/environs-9.5.0%20-orange?style=flat-square)
![requests](https://img.shields.io/badge/requests-2.28.2%20-orange?style=flat-square)
![flake8](https://img.shields.io/badge/flake8-6.0.0%20-yellow?style=flat-square)
![isort](https://img.shields.io/badge/isort-^5.12.0%20-yellow?style=flat-square)


<img width="1200" src="https://user-images.githubusercontent.com/106741554/236930320-957f8b9d-b975-4a58-acb2-3ae5062e39f1.gif"></img>

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project was made for analyzing different cars in different categories from [website](https://auto.ria.com/)
to help my friend pick up a new a car with definite settings. <br> 
> In the end I gained valueable experience with setting deadlines properly :)

## Technologies
During this project I used `pandas` for exporting scraped data to csv format, `environs` to store my secrets, `requests` to get responses from the website, `bs4` for convenient scrapping, `pydantic` for validation and convenient interaction with environmet variables.I used `flake8` and `isort` for refactoring as well.

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
#### To install dev dependencies 
```bash
$ poetry install --with dev
```
To edit configuration of the app you need to change ".env" file
