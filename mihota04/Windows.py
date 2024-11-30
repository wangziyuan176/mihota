import easygui
from window import window
file=easygui.fileopenbox('您要把输出文件保存到哪个路径?','路径')
if file:
    a=easygui.enterbox('请输入文件名','文件名')
    file=file+'/'+a+'.mhtfile'
    b=easygui.enterbox('你要在输出文件中写入什么?','写入')
    window.write_file(file,b,'utf-8')
    window.win('已保存到'+file+'文件夹中','OK','OK')
    window.py_run('mihota04.py')