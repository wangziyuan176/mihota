import matplotlib.pyplot as plt
import easygui
def line_chart(x,y,xcol,ycol,title,xlabel,ylabel):
    plt.plot(x,y)
    plt.style.use('ggplot')
    plt.title(title)
    plt.xlabel(xlabel,xcol)
    plt.ylabel(ylabel,ycol)
    plt.show()
x = easygui.enterbox('输入x的坐标')
x = eval(x)
y = easygui.enterbox('输入y的坐标')
y = eval(y)
xcol = easygui.enterbox('输入x轴的颜色')
ycol = easygui.enterbox('输入y轴的颜色')
title = easygui.enterbox('输入图表的标题')
xlabel = easygui.enterbox('输入x轴的标签')
ylabel = easygui.enterbox('输入y轴的标签')
line_chart(x,y,xcol,ycol,title,xlabel,ylabel)