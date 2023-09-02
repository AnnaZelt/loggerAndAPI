from enum import Enum
import requests

class Actions(Enum):
    DISPLAY_CURRENT = 1
    DISPLAY_FORECAST = 2
    EXIT = 3

#Returns a selected action
def menu_selection():
    for action in Actions:
        print(f"{action.value} - {action.name}")
    user_selection=Actions(int(input("What would you like to do? \n")))
    return user_selection

def menu():
    while(True):
        user_selection = menu_selection()
        if user_selection == Actions.DISPLAY_CURRENT:
            current_weather()
        if user_selection == Actions.DISPLAY_FORECAST:
            forecast_weather()
        if user_selection == Actions.EXIT: 
            return
        
def location():
    global current
    print("This displays weather for: ")
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q":"53.1,-0.13"}
    headers = {
        "X-RapidAPI-Key": "03cfd287e5msh13cbd61894182d2p1aad6djsnece76dc1606f",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response_loc = requests.get(url, headers=headers, params=querystring)
    current = response_loc.json()

    if 'location' in current:
        current_weather = current['location']
        name = current_weather.get('name')
        region = current_weather.get('region')
        country = current_weather.get('country')

        if country is not None:
            print("Country:", country)
        if region is not None:
            print("Region:", region)
        if name is not None:
            print(f"City: {name}\n")
    else:
        print("Location data retrieval failed.\n")

def current_weather():
    global current
    print("Current weather: \n")
    if 'current' in current:
        current_weather = current['current']
        temperature_c = current_weather.get('temp_c')
        humidity = current_weather.get('humidity')
        condition_text = current_weather.get('condition', {}).get('text')

        if temperature_c is not None:
            print("Temperature:", temperature_c, "°C")
        if humidity is not None:
            print("Humidity:", humidity, "%")
        if condition_text is not None:
            print(f"Condition: {condition_text}\n")
    else:
        print("Weather data retrieval failed.\n")

def forecast_weather():
    print("Forecast weather: \n")
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q":"London","days":"3"}
    headers = {
        "X-RapidAPI-Key": "03cfd287e5msh13cbd61894182d2p1aad6djsnece76dc1606f",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response_fore = requests.get(url, headers=headers, params=querystring)
    forecast = response_fore.json()
    if 'current' in forecast:
        current_weather = forecast['current']
        temperature_c = current_weather.get('temp_c')
        humidity = current_weather.get('humidity')
        condition_text = current_weather.get('condition', {}).get('text')

        if temperature_c is not None:
            print("Temperature:", temperature_c, "°C")
        if humidity is not None:
            print("Humidity:", humidity, "%")
        if condition_text is not None:
            print(f"Condition: {condition_text}\n")
    else:
        print("Weather data retrieval failed.\n")

if __name__ == "__main__":
    location()
    menu()

    