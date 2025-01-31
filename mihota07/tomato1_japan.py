import easygui
from window import window

a = easygui.buttonbox('ポモドーロテクニック（集中25分、休憩5分）', 'ポモドーロ', ['開始', '終了'])
if a == '終了':
    window.py_run('mihota07_japan.py')
elif a == '開始':
    window.py_run('tomato_japan.py')
