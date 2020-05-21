import pyowm
import datetime

def getWeather(location):
    apikey = 'ace4a3f381475ee99d7502307c10a6e0'
    owm = pyowm.OWM(apikey)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    temp = w.get_temperature('fahrenheit')
    humidity = w.get_humidity()
    wind = w.get_wind()
    status = w.get_status()
    sunrise = datetime.datetime.fromtimestamp(int(w._sunrise_time)).strftime('%I:%M')
    sunset = datetime.datetime.fromtimestamp(int(w._sunset_time)).strftime('%I:%M')
    return temp,humidity,wind,status,sunrise,sunset

# tuple looks like this:
# ({'temp': 62.42, 'temp_max': 64.4, 'temp_min': 61.0, 'temp_kf': None}, 93, {'speed': 2.1, 'deg': 70}, 'Rain', '05:40', '19:46')
weather = getWeather('Redstone Arsenal,US')
x = ('Current Conditions:\n'
        ' Temperature:',round(weather[0]['temp']),'\n',
        'Humidity:',weather[1],'\n',
        'Wind Speed:',weather[2]['speed'],'mph\n',
        'Conditions:',weather[3],'\n',
        'Sunrise is at ',weather[4],'am and sunset is at',weather[5],'pm.'
      )
print(x)