import easygui,random,sys,os,time
def win(str_a,window_name,button):
    easygui.msgbox(str_a,window_name,button)
def window_ramdom_have_msg(inta,intb,msg):
    i=random.randint(inta,intb)
    easygui.msgbox(msg+str(i))
def window_random_donot_have_msg(inta,intb):
    i=random.randint(inta,intb)
    easygui.msgbox(str(i))
def write_file(name,msg,code):
    f=open(name,'w',encoding=code)
    f.write(msg)
def path_to_what(path):
    os.chdir(path)
def py_run(file):
    os.system('python '+file)
def over():
    sys.exit(0)
def window_time_now():
    easygui.msgbox(time.strftime("%Y-%m-%d %H:%M:%S"))
def window_no_button(msg,choice):
    easygui.choicebox(msg,choices=choice)
def window_has_button(msg,choice):
    easygui.buttonbox(msg,choices=choice)
def win_must_have_keyboard(str_a, window_name):
    easygui.enterbox(str_a, window_name)
