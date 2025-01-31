import easygui
from window import window

a = easygui.buttonbox('What type of file would you like to create?', choices=['mhtfile', 'Text File', 'Other File'])
if a == 'mhtfile':
    file = easygui.fileopenbox('Where would you like to save the output file?', 'Path')
    if file:
        a = easygui.enterbox('Please enter the file name', 'File Name')
        file = file + '/' + a + '.mhtfile'
        b = easygui.enterbox('What do you want to write in the output file?', 'Write')
        window.write_file(file, b, 'utf-8')
        window.win('Saved to ' + file + ' folder', 'OK', 'OK')
        window.py_run('mihota07_english.py')
elif a == 'Text File':
    file = easygui.fileopenbox('Where would you like to save the output file?', 'Path')
    if file:
        a = easygui.enterbox('Please enter the file name', 'File Name')
        file = file + '/' + a + '.txt'
        b = easygui.enterbox('What do you want to write in the output file?', 'Write')
        window.write_file(file, b, 'utf-8')
        window.win('Saved to ' + file + ' folder', 'OK', 'OK')
        window.py_run('mihota07_english.py')
elif a == 'Other File':
    file = easygui.fileopenbox('Where would you like to save the output file?', 'Path')
    if file:
        a = easygui.enterbox('Please enter the file name', 'File Name')
        file = file + '/' + a
        f = open(file, 'w', encoding='utf-8')
        f.close()
        window.win('Saved to ' + file + ' folder', 'OK', 'OK')
        window.py_run('mihota07_english.py')
