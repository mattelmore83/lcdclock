import pyowm
import datetime

def getWeather(location):
    apikey = 'ace4a3f381475ee99d7502307c10a6e0'
    owm = pyowm.OWM(apikey)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(location)
    w = observation.weather
    temp = w.temperature('fahrenheit')
    humidity = w.humidity
    wind = w.wind()
    status = w.detailed_status
    sunrise = datetime.datetime.fromtimestamp(int(w.sunrise_time())).strftime('%I:%M')
    sunset = datetime.datetime.fromtimestamp(int(w.sunset_time())).strftime('%I:%M')
    return temp,humidity,wind,status,sunrise,sunset

# tuple looks like this:
# ({'temp': 62.42, 'temp_max': 64.4, 'temp_min': 61.0, 'temp_kf': None}, 93, {'speed': 2.1, 'deg': 70}, 'Rain', '05:40', '19:46')
weatherData = getWeather('Redstone Arsenal,US')

weather_string = ('Current Conditions:\n' +
                   'Temperature: ' + str(round(weatherData[0]['temp'])) + u'\N{DEGREE SIGN}' + '\n' +
                   'Humidity: ' + str(weatherData[1]) + '%\n' +
                   'Wind Speed: ' + str(weatherData[2]['speed']) + 'mph\n' +
                   'Conditions: ' + weatherData[3] + '\n' +
                   'Sunrise is at ' + weatherData[4] + 'am and sunset is at ' + weatherData[5] + 'pm.')
print(weather_string)
