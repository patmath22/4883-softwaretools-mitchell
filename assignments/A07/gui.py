""" 
Description:
    This is an example gui that allows you to enter the appropriate parameters to get the weather from wunderground.
TODO:
    - You will need to change the text input boxes to drop down boxes and add the appropriate values to the drop down boxes.
    - For example the month drop down box should have the values 1-12.
    - The day drop down box should have the values 1-31.
    - The year drop down box should have the values ??-2023.
    - The filter drop down box should have the values 'daily', 'weekly', 'monthly'.
"""
import PySimpleGUI as sg      

def currentDate(returnType='tuple'):
    """ Get the current date and return it as a tuple, list, or dictionary.
    Args:
        returnType (str): The type of object to return.  Valid values are 'tuple', 'list', or 'dict'.
    """
    from datetime import datetime
    if returnType == 'tuple':
        return (datetime.now().month, datetime.now().day, datetime.now().year)
    elif returnType == 'list':
        return [datetime.now().month, datetime.now().day, datetime.now().year]

    return {
        'day':datetime.now().day,
        'month':datetime.now().month,
        'year':datetime.now().year
    }

def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):
    """ A gui to pass parameters to get the weather from the web.
    Args:
        month (int): The month to get the weather for.
        day (int): The day to get the weather for.
        year (int): The year to get the weather for.
    Returns:
        Should return a URL like this, but replace the month, day, and year, filter, and airport with the values passed in.
        https://www.wunderground.com/history/daily/KCHO/date/2020-12-31
    """
   
    current_month,current_day,current_year = currentDate('tuple')
    
    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year
    
    # Create the gui's layout using text boxes that allow for user input without checking for valid input

    months=[]
    for i in range(12):
        months.append(i+1)

    days=[]
    for i in range(31):
        days.append(i+1)

    years=[]
    for i in range(23):
        years.append(i+2000)

    filters=['Daily','Weekly','Monthly']

    layout = [
        [sg.Text('Month')],[sg.Combo(months,default_value=current_month)],
        [sg.Text('Day')],[sg.Combo(days,default_value=current_day)],
        [sg.Text('Year')],[sg.Combo(years,default_value=current_year)],
        [sg.Text('Code')],[sg.InputText()],
        [sg.Text('Daily / Weekly / Monthly')],[sg.Combo(filters)],
        [sg.Submit(), sg.Cancel()]
    ]      

    window = sg.Window('Get The Weather', layout)    


    event, values = window.read()
    window.close()
        
    month = values[0]
    day = values[1]
    year = values[2]
    code = values[3]
    filter =values[4]

    print(values)
    print(month)
    print(day)

    sg.popup('You entered', f"Month: {month}, Day: {day}, Year: {year}, Code: {code}, Filter: {filter}")

    # return the URL to pass to wunderground to get appropriate weather data

    base_url = "https://wunderground.com/history"
    url = f"{base_url}/{filter}/{code}/{year}-{month}-{day}"
    print(url)


if __name__=='__main__':
    buildWeatherURL()