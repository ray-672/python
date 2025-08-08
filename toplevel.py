from tkinter import *

win = Tk()
win.title('root window.')
win.geometry('500x500')
win.configure(bg = 'black')


def top():
    toplevel = Toplevel()
    toplevel.geometry('160x160')
    toplevel.configure(bg = 'tomato')
    label2 = Label(toplevel, text = ' top level window' , font = ('arial', 12, 'bold'))
    label2.place(x = 10, y = 10)


label1 = Label(win, text = ' main window' , font = ('arial', 18, 'bold'))
label1.place(x = 120, y = 120)

button1 = Button(win, text = ' click me' , font = ('arial', 18, 'bold'), command= top)
button1.place(x = 120, y = 180)

win.mainloop()