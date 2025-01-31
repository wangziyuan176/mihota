import easygui
from window import window

# Prompt the user with a button box displaying options
a = easygui.buttonbox('This computer', 'mihota', ['Settings', 'Guess the Number Game', 'Output mhtfile to Windows', 'Pomodoro Timer', 'Calculator', 'Weather Inquiry'])
if a == 'Settings':
    window.py_run('st.py')
elif a == 'Output File to Windows':
    window.py_run('Windows_english.py.py')
elif a == 'Guess the Number Game':
    window.py_run('guess_number_game_english.py')
elif a == 'Pomodoro Timer':
    window.py_run('tomato1_english.py')
elif a == 'Calculator':
    window.py_run('calculator_english.py')
elif a == 'Weather Inquiry':
    window.py_run('weather_inquiry_english.py')
elif a == 'Output mhtfile to Windows':
    window.py_run('see_mhtfile_english  .py')
