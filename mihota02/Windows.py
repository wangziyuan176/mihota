import easygui
from window import window
a=easygui.enterbox('请输入输出文件的名字(格式:*.*)','输出')
b=easygui.enterbox('你要在输出文件中写入什么?','写入')
print(a)
window.write_file(a,b,'utf-8')
window.win('已保存到I:/PycharmProject/mihota/mihota02文件夹中','OK','OK')
window.py_run('mihota02.py')