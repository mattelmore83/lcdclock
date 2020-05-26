import sys
import time
import datetime
from tkinter import *
import pyowm

import functools
import operator


def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str

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

def tick():
    time_string = time.strftime("%I:%M:%S")
    date_string = time.strftime("%a %b %d")
    datetime_string = date_string + ', ' + time_string
    weatherData = getWeather('Redstone Arsenal,US')
    weather_string = ('Current Conditions:\n' +
                      'Temperature: ' + str(round(weatherData[0]['temp'])) + u'\N{DEGREE SIGN}' + '\n' +
                      'Humidity: ' + str(weatherData[1]) + '%\n' +
                      'Wind Speed: ' + str(weatherData[2]['speed']) + 'mph\n' +
                      'Conditions: ' + weatherData[3] + '\n' +
                      'Sunrise is at ' + weatherData[4] + 'am and\nsunset is at ' + weatherData[5] + 'pm.')
    clock.config(text=datetime_string)
    weather.config(text=weather_string)
    clock.after(200,tick)

gui = Tk()
gui.attributes('-fullscreen', True)
gui['bg']='gray'
# frames
clockFrame = Frame(gui)
clockFrame.pack(side=TOP)
weatherFrame = Frame(gui)
weatherFrame.pack()

clock = Label(clockFrame, font = ("times", 32, "bold"), bg="gray")
weather = Label(weatherFrame, font = ("times", 22, "bold"), bg="gray")
clock.grid(row=0, column=1)
weather.grid(row=0, column=1)
tick()
gui.mainloop()



print(weather_string)