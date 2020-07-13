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


while True:
    try:
        gui = Tk()
        gui.attributes('-fullscreen', True)
        gui['bg'] = 'gray'
        # frames
        clockFrame = Frame(gui)
        clockFrame.pack(side=TOP)
        weatherFrame = Frame(gui)
        weatherFrame.pack()

        clock = Label(clockFrame, font=("times", 32, "bold"), bg="gray")
        weather = Label(weatherFrame, font=("times", 22, "bold"), bg="gray")
        clock.grid(row=0, column=1)
        weather.grid(row=0, column=1)
        tick()
        gui.mainloop()
    except Exception:
        logger.error("Fatal error in main loop", exc_info=True)
