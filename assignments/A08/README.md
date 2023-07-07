# Assignment 08 - Fast Api with Covid Data
### Patrick Mitchell
### Description:

Create a RESTful API using FastAPI that provides access to COVID-19 data. The API will fetch the data from a publicly available data source and expose endpoints to retrieve various statistics related to COVID-19 cases.
### Files

|   #   | File                 | Description                             |
| :---: | -------------------- | --------------------------------------- |
|   1   | [data.csv](data.csv) | A csv file that contains the CoVid data |
|   2   | [api.py](api.py)     | Code for creating FastAPI               |



### Imported methods:

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv


### Instructions

Run api.py this builds an API using FastAPI. In the terminal is the local host where this is running.
This runs using uvicorn on your browser at the following url: http://127.0.0.1:5000 
This may vary with your system. In your terminal the url will be displayed. 
Control+click on the url and it will take you to the API.

Instructions are given for each method. Click the down arrow for the method you want to run. Hit the Try this out button. If parameters are needed you will be prompted. 

### EndPoints and usage.

### /countries/
    - List of countries in the data

### /whos/
    - Lists the World Health Organization codes for the data

### /casesByRegion/
    -Returns the number of cases by region

### /deaths/
    - This method will return the total number of death

### /deaths_by_country_year/
    - This method will return a total death count for a country and year

    -Params:

      - country (str) : A country name
      - year (int) : A 4 digit number
    -Returns:

    -(int) : Total number of deaths in that country during that year

### /deaths_by_country/
    - Returns the number of deaths in a particular country

### /cases_by_country/
    - Returns the number of cases in a particular country

### /deaths_by_region/
    - This method will return a total death count for a WHO region

### /deaths_by_region_year/
    - This method will return a total death count for a region and year

        -Params:

          - WHO_region (str) : A 4 letter region code
          - year (int) : A 4 digit number
        -Returns:

            -(int) : Total number of deaths in that region during that year

### /max_death
    - This gives the country with the maximum deaths in the data

### /min_death
    - This give the country with the minimum deaths in the data

### /death_country_daterange
    - This method will return a total deaths in a country for the time period given

        -Params:

            - Country (str) : Name of the country
            - minYear (int) : Format YYYYMMDD
            - maxYear (int) : Format YYYYMMDD

        -Returns:

            -(int) : Total number of deaths in that country during the period minYear to maxYear

### /max_death_RY
    -This method will return the country with the maximum deaths for the time period given

        -Params:

            - minYear (int) : Format YYYYMMDD
            - maxYear (int) : Format YYYYMMDD
        -Returns:

            -(int) : The country with the maximum deaths in the period minYear to maxYear

 ###  /mort_rate_country  
    -This method will return the mortality rate for a particular country.

        -Params:

            -country (str) : Country name
        -Returns:

            - decimal : the number of deaths divided by the number of cases      