import requests
import easygui
from window import window

easygui.msgbox('天気情報へようこそ！')
cityName = easygui.enterbox('都市名を入力してください：')
url = 'http://apis.juhe.cn/simpleWeather/query?city=' + cityName + '&key=b911fccda239ba5f448870f9ab11e3e4'
response = requests.get(url)
data = response.json()
if data['error_code'] == 0:
    weather = data['result']['realtime']['info']
    temperature = data['result']['realtime']['temperature']
    easygui.msgbox('都市：' + cityName + '\n' + '天気：' + weather + '\n' + '気温：' + temperature + '℃')
    window.py_run('mihota07_japan.py')
else:
    easygui.msgbox('天気情報の取得に失敗しました！')
    window.py_run('mihota07_japan.py')
