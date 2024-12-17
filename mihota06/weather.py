import requests
import easygui
from window import window

easygui.msgbox('欢迎使用天气！')
cityName = easygui.enterbox('请输入城市名称：')
url='http://apis.juhe.cn/simpleWeather/query?city=' + cityName + '&key=b911fccda239ba5f448870f9ab11e3e4'
response = requests.get(url)
data = response.json()
if data['error_code'] == 0:
    weather = data['result']['realtime']['info']
    temperature = data['result']['realtime']['temperature']
    easygui.msgbox('城市：'+cityName+'\n'+'天气：'+weather+'\n'+'温度：'+temperature+'℃')
    window.py_run('mihota05.py')
else:
    easygui.msgbox('获取天气信息失败！')
    window.py_run('mihota05.py')

