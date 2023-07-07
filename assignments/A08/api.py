
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv



description = """🚀
## 4883 Software Tools
### Where awesomeness happens
"""


app = FastAPI(

    description=description,

)

db = []

# Open the CSV file
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    i = 0
    # Read each row in the CSV file
    for row in reader:
        if i == 0:
            i += 1
            continue
        db.append(row)

#writing function

def getdeath():
    global db
    deaths = 0
    for row in db:
        deaths += int(row[6])
    return deaths


def getdeathCY(country=None,year=None):
    global db
    deaths = 0 
    for row in db:
        if country.lower()==row[2].lower() and int(year)==int(row[0][:4]):
            deaths += int(row[6])


    return deaths
    #work on function

def getdeathC(country=None):
    global db
    deaths = 0 
    for row in db:
        if country.lower()==row[2].lower():
            deaths += int(row[6])

    return deaths

def getcasesC(country=None):
    global db
    deaths = 0 
    for row in db:
        if country.lower()==row[2].lower():
            deaths += int(row[4])          

    return deaths

def getdeathR(WHO_region=None):
    global db
    deaths = 0 
    for row in db:
        if WHO_region==row[3]:
            deaths += int(row[6])
    return deaths

def getdeathRY(WHO_region=None,year=None):
    global db
    deaths = 0 
    for row in db:
        if WHO_region==row[3] and int(year)==int(row[0][:4]):
            deaths += int(row[6])
    return deaths

def getMaxDeaths():
  countries = getUniqueCountries()
  maxCountry = None
  maxDeaths = 0

  for country in countries:
    deaths = getdeathC(country)
    if deaths > maxDeaths:
      maxDeaths = deaths
      maxCountry = country 

  return (maxCountry, maxDeaths)





def getMinDeaths():
  countries = getUniqueCountries()
  minCountry = None
  minDeaths = 7922  #this is the number of deaths in Afghanistan, could just use call first element

  for country in countries:
    deaths = getdeathC(country)
    if deaths < minDeaths:
      minDeaths = deaths
      minCountry = country 

  return (minCountry, minDeaths)





#Needs work below

def getdeathsCYR(country=None,minYear=None,maxYear=None):
    global db
    deaths=0
    
    for row in db:

        #f.write(f"if {country.lower()}=={row[2].lower()} and {int(minYear)} <= {int(row[0].replace('-',''))} and {int(maxYear)} >= {int(row[0].replace('-',''))}\n")
        if country.lower()==row[2].lower() and int(minYear) <= int(row[0].replace('-','')) and int(maxYear) >= int(row[0].replace('-','')):
            
            deaths += int(row[6])
                

    return deaths


def getMaxDeathsRY(minYear=None,maxYear=None):
  countries = getUniqueCountries()
  maxCountry = None
  maxDeaths = 0

  for country in countries:
    deaths = getdeathsCYR(country,minYear,maxYear)
    if deaths > maxDeaths:
      maxDeaths = deaths
      maxCountry = country 

  return (maxCountry, maxDeaths)


def getUniqueCountries():
    global db
    countries = {}

    for row in db:
        print(row)
        if not row[2] in countries:
            countries[row[2]] = 0

    return list(countries.keys())

def getUniqueWhos():
    global db
    whos = {}

    for row in db:
        print(row)
        if not row[3] in whos:
            whos[row[3]] = 0
   
    return list(whos.keys())

@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

@app.get("/countries/")
async def countries():

    return {"countries":getUniqueCountries()}


@app.get("/whos/")
async def whos():

    return {"whos":getUniqueWhos()}

@app.get("/casesByRegion/")
async def casesByRegion(year:int = None):
    """
    Returns the number of cases by region
    
    """
    cases = {}
    
    for row in db:
        if year != None and year != int(row[0][:4]):
            continue
            #checks for new key and places in dictionary
        if not row[3] in cases:
            cases[row[3]] = 0
        cases[row[3]] += int(row[4])    

    return {"data":cases,"success":True,"message":"Cases by Region","size":len(cases),"year":year}

@app.get("/deaths/")
async def deaths():
    """
    This method will return the total number of death
    
    """
    return{"deaths":getdeath()}

@app.get("/deaths_by_country_year/")
async def deaths_by_country_year(country:str=None,year:int=None):
    """
    This method will return a total death count for a country and year

    -**Params:**

        - country (str) : A country name
        - year (int) : A 4 digit number

    -**Returns:**

        -(int) : Total number of deaths in that country during that year    
    """
    return{"deaths":getdeathCY(country,year)}

@app.get("/deaths_by_country/")
async def deaths_by_country(country:str=None):
    """
    Returns the number of deaths in a particular country
    """
    return{"deaths":getdeathC(country)}

@app.get("/cases_by_country/")
async def cases_by_country(country:str=None):
    """
    Returns the number of cases in a particular country
    """
    return{"cases":getcasesC(country)}

@app.get("/deaths_by_region/")
async def deaths_by_region(WHO_region:str=None):
    """
    This method will return a total death count for a WHO region

    -**Params:**

        - WHO_region (str) : A 4 letter region code
        

    -**Returns:**

        -(int) : Total number of deaths in that region   
    
    """
    return{"deaths":getdeathR(WHO_region)}

@app.get("/deaths_by_region_year/")
async def deaths_by_region_year(WHO_region:str=None,year:int=None):
    """
    This method will return a total death count for a region and year

    -**Params:**

        - WHO_region (str) : A 4 letter region code
        - year (int) : A 4 digit number

    -**Returns:**

        -(int) : Total number of deaths in that region during that year    
    
         
    """

    return{"deaths":getdeathRY(WHO_region,year)}

@app.get("/max_death")
async def max_death():
    """
    This gives the country with the maximum deaths in the data
    """
    return{"Max death and Country":getMaxDeaths()}

@app.get("/min_death")
async def min_death():
    """
    This give the country with the minimum deaths in the data
    """
    return{"Min death and Country":getMinDeaths()}

@app.get("/death_country_daterange")
async def death_country_daterange(country:str=None,minYear:int=None,maxYear:int=None):
    """
    This method will return a total deaths in a country for the time period given

    -**Params:**

        - Country (str) : Name of the country
        - minYear (int) : Format YYYYMMDD
        - maxYear (int) : Format YYYYMMDD

    -**Returns:**

        -(int) : Total number of deaths in that country during the period minYear to maxYear    
    
         
    """
    return{"deaths":getdeathsCYR(country,minYear,maxYear)}

@app.get("/max_death_RY")
async def max_death_RY(minYear:int=None,maxYear:int=None):
    """
    This method will return the country with the maximum deaths for the time period given

    -**Params:**

        - minYear (int) : Format YYYYMMDD
        - maxYear (int) : Format YYYYMMDD

    -**Returns:**

        -(int) : The country with the maximum deaths in the period minYear to maxYear    
    
         
    """
    return{"Max death and Country":getMaxDeathsRY(minYear,maxYear)}


    


if __name__ == "__main__":
    
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True) #host="127.0.0.1"
