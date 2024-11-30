import easygui
from window import window
a=easygui.buttonbox('此电脑','mihota',['设置','猜数字小游戏','输出文件到Windows','番茄钟','计算器','天气查询'])
if a=='设置':
    window.py_run('st.py')
elif a=='输出文件到Windows':
    window.py_run('Windows.py')
elif a=='猜数字小游戏':
    window.py_run('guess_number_game.py')
elif a=='番茄钟':
    window.py_run('tomato1.py')
elif a=='计算器':
    window.py_run('calculator.py')
elif a=='天气查询':
    window.py_run('weather.py')