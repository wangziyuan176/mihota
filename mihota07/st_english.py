import easygui
from window import window

a = easygui.choicebox('Settings', 'mihota', ['Time', 'About', 'Return'])
if a == 'Time':
    window.py_run('st1.py')
elif a == 'About':
    window.py_run('st2.py')
elif a == 'Return':
    window.py_run('mihota07_english.py.py')
