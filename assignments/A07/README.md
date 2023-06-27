
# Assignment 07 - Web Scraping
### Patrick Mitchell
### Description:

This project will combine several tools. We use python GUI to both enter a URL destination and produce a table. We use beautiful soup web scraper to extract pertain information. 
### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | [airports_better.json](airports_better.json)  | json file contain airport codes and other information     |
|   2   | [get_weather.py](get_weather.py)   | Code for scraping a web site      |
|   3  | [gui.py](gui.py) | This GUI generates the website URL |
|  4 | [table2.html](table2.html) | contains information from a scrape of a particular site |

### Instructions
The program get_weather.py is hard coded and bypasses the scraping of the web. Currently it runs and asks for a particular date, airport code and a filter(daily,monthly, yearly). This produces a corresponding URL, however the beautiful soup portion is bypass. A seperarte file was created called table2.html which contains the information that the beautiful soup portion created. Then that information is processed and displayed in a GUI table. 

The gui.py gets the airport codes from airports_better.json and produces a URL. 

In the code there are instructions for removing the bypass. This is accomplished by merely commenting out two lines and uncommenting another. 
UNCOMMENT LINE 59 AND COMMENT 61,62
