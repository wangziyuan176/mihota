import matplotlib.pyplot as plt
import easygui
from window import window
def line_chart(x,y,xcol,ycol,title,xlabel,ylabel):
    plt.plot(x,y)
    plt.style.use('ggplot')
    plt.title(title)
    plt.xlabel(xlabel,color=xcol)
    plt.ylabel(ylabel,color=ycol)
    plt.show()
x = easygui.enterbox('输入x的坐标')
x = eval(x)
y = easygui.enterbox('输入y的坐标')
y = eval(y)
try:
    xcol = easygui.enterbox('输入x轴的颜色')
except:
    xcol = 'black'
try:
    ycol = easygui.enterbox('输入y轴的颜色')
except:
    ycol = 'black'
title = easygui.enterbox('输入图表的标题')
xlabel = easygui.enterbox('输入x轴的标签')
ylabel = easygui.enterbox('输入y轴的标签')
line_chart(x,y,xcol,ycol,title,xlabel,ylabel)
window.py_run('mihoto07.py')