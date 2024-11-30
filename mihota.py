import easygui,sys
from window import window
easygui.msgbox('欢迎安装mihota！')
b=easygui.choicebox('请选择要下载的版本','mihota',['mihota0.1','mihota0.2','mihota0.3','mihota0.4','mihota0.5','退出'])
easygui.msgbox('欢迎使用mihota!')
if b=='mihota0.1':
    a=easygui.fileopenbox('请选择mihota0.1的源码路径','mihota')
    window.path_to_what(a)
    window.py_run('mihota01.py')
elif b=='mihota0.2':
    c=easygui.fileopenbox('请选择mihota0.2的源码路径','mihota')
    window.path_to_what(c)
    window.py_run('mihota02.py')
elif b=='mihota0.3':
    d=easygui.fileopenbox('请选择mihota0.4的源码路径','mihota')
    window.path_to_what(d)
    window.py_run('mihota03.py')
elif b=='mihota0.4':
    e=easygui.fileopenbox('请选择mihota0.4的源码路径','mihota')
    window.path_to_what(e)
    window.py_run('mihota04.py')
elif b=='mihota0.5':
    f=easygui.fileopenbox('请选择mihota0.5的源码路径','mihota')
    window.path_to_what(f)
    window.py_run('mihota05.py')
elif b=='退出':
    sys.exit(0)
    