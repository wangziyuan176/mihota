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

x = easygui.enterbox('Enter the x coordinates')
x = eval(x)
y = easygui.enterbox('Enter the y coordinates')
y = eval(y)
try:
    xcol = easygui.enterbox('Enter the color forthe x-axis')
    ycol = easygui.enterbox('Enter the color for the y-axis')
except:
    xcol = 'black'
    ycol = 'black'
title = easygui.enterbox('Enter the title of the chart')
xlabel = easygui.enterbox('Enter the label for the x-axis')
ylabel = easygui.enterbox('Enter the label for the y-axis')

line_chart(x, y, xcol, ycol, title, xlabel, ylabel)
window.py_run('mihoto07_english.py')