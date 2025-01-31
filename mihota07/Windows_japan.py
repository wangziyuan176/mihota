import easygui
from window import window

a = easygui.buttonbox('どのタイプのファイルを作成しますか？', choices=['mhtfileファイル', 'テキストファイル', 'その他のファイル'])
if a == 'mhtfileファイル':
    file = easygui.fileopenbox('出力ファイルをどのパスに保存しますか？', 'パス')
    if file:
        a = easygui.enterbox('ファイル名を入力してください', 'ファイル名')
        file = file + '/' + a + '.mhtfile'
        b = easygui.enterbox('出力ファイルに何を書き込みますか？', '書き込み')
        window.write_file(file, b, 'utf-8')
        window.win(file + 'に保存されました', 'OK', 'OK')
        window.py_run('mihota07_japan.py')
elif a == 'テキストファイル':
    file = easygui.fileopenbox('出力ファイルをどのパスに保存しますか？', 'パス')
    if file:
        a = easygui.enterbox('ファイル名を入力してください', 'ファイル名')
        file = file + '/' + a + '.txt'
        b = easygui.enterbox('出力ファイルに何を書き込みますか？', '書き込み')
        window.write_file(file, b, 'utf-8')
        window.win(file + 'に保存されました', 'OK', 'OK')
        window.py_run('mihota07_japan.py')
elif a == 'その他のファイル':
    file = easygui.fileopenbox('出力ファイルをどのパスに保存しますか？', 'パス')
    if file:
        a = easygui.enterbox('ファイル名を入力してください', 'ファイル名')
        file = file + '/' + a
        f = open(file, 'w', encoding='utf-8')
        f.close()
        window.win(file + 'に保存されました', 'OK', 'OK')
        window.py_run('mihota07_japan.py')