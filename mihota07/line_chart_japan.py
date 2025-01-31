import matplotlib.pyplot as plt
import easygui
from window import window

def line_chart(x, y, xcol, ycol, title, xlabel, ylabel):
    plt.plot(x, y)
    plt.style.use('ggplot')
    plt.title(title)
    plt.xlabel(xlabel, color=xcol)
    plt.ylabel(ylabel, color=ycol)
    plt.show()

x = easygui.enterbox('xの座標を入力してください')
x = eval(x)
y = easygui.enterbox('yの座標を入力してください')
y = eval(y)

try:
    xcol = easygui.enterbox('x軸の色を入力してください')
except:
    xcol = 'black'

try:
    ycol = easygui.enterbox('y軸の色を入力してください')
except:
    ycol = 'black'

title = easygui.enterbox('グラフのタイトルを入力してください')
xlabel = easygui.enterbox('x軸のラベルを入力してください')
ylabel = easygui.enterbox('y軸のラベルを入力してください')

line_chart(x, y, xcol, ycol, title, xlabel, ylabel)
window.py_run('mihoto07_japan.py')
