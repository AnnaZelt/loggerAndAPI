import pprint
import requests

# def translate(query):
#     url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

#     payload = {
#         "source": "en",
#         "target": "es",
#         "q": query
#     }
#     headers = {
#         "content-type": "application/x-www-form-urlencoded",
#         "Accept-Encoding": "application/gzip",
#         "X-RapidAPI-Key": "03cfd287e5msh13cbd61894182d2p1aad6djsnece76dc1606f",
#         "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
#     }

#     response = requests.post(url, data=payload, headers=headers)
#     data = response.json()
#     if 'data' in data and 'translations' in data['data']:
#         translated_text = data['data']['translations'][0]['translatedText']
#         print("Translated Text:", translated_text)
#     else:
#         print("Translation failed.")

# translate(input("Sentence to translate: "))

def weather_api():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":"53.1,-0.13"}

    headers = {
	"X-RapidAPI-Key": "03cfd287e5msh13cbd61894182d2p1aad6djsnece76dc1606f",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    if 'current' in data:
        current_weather = data['current']
        temperature_c = current_weather.get('temp_c')
        humidity = current_weather.get('humidity')
        condition_text = current_weather.get('condition', {}).get('text')

        if temperature_c is not None:
            print("Temperature:", temperature_c, "°C")
        if humidity is not None:
            print("Humidity:", humidity, "%")
        if condition_text is not None:
            print("Condition:", condition_text)
    else:
        print("Weather data retrieval failed.")

weather_api()