import easygui
from window import window

a = easygui.buttonbox('Pomodoro Timer (Focus for 25 minutes, Rest for 5 minutes)', 'Pomodoro Timer', ['Start', 'Exit'])
if a == 'Exit':
    window.py_run('mihota07_english.py')
elif a == 'Start':
    window.py_run('tomato.py')
