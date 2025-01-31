import requests
import easygui
from window import window

easygui.msgbox('Welcome to use Weather App!')
cityName = easygui.enterbox('Please enter the city name:')
url = 'http://apis.juhe.cn/simpleWeather/query?city=' + cityName + '&key=b911fccda239ba5f448870f9ab11e3e4'
response = requests.get(url)
data = response.json()
if data['error_code'] == 0:
    weather = data['result']['realtime']['info']
    temperature = data['result']['realtime']['temperature']
    easygui.msgbox('City: ' + cityName + '\n' + 'Weather: ' + weather + '\n' + 'Temperature: ' + temperature + '℃')
    window.py_run('mihota07.py')
else:
    easygui.msgbox('Failed to retrieve weather information!')
    window.py_run('mihota07.py')


