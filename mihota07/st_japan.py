import easygui
from window import window

a = easygui.choicebox('設定', 'mihota', ['時間', 'について', '戻る'])
if a == '時間':
    window.py_run('st1.py')
elif a == 'について':
    window.py_run('st2.py')
elif a == '戻る':
    window.py_run('mihota07_japan.py')
