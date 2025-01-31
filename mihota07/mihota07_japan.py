import easygui
from window import window

a = easygui.buttonbox('このコンピュータ', 'mihota', ['設定', '数字を当てるゲーム', 'mhtfileファイルをWindowsに出力', 'ポモドーロタイマー', '電卓', '天気予報'])
if a == '設定':
    window.py_run('st.py')
elif a == 'mhtfileファイルをWindowsに出力':
    window.py_run('Windows.py')
elif a == '数字を当てるゲーム':
    window.py_run('guess_number_game.py')
elif a == 'ポモドーロタイマー':
    window.py_run('tomato1.py')
elif a == '電卓':
    window.py_run('calculator.py')
elif a == '天気予報':
    window.py_run('weather.py')
elif a == '出力mhtfileファイルをWindowsに':
    window.py_run('see_mhtfile.py')
