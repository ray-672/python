from tkinter import *
from datetime import *


win = Tk()
win.title('first tk window')
win.geometry('500x500')
win.configure(bg = 'black')

def greet():
    name = ent1.get()
    dt = datetime.now()
    text1.delete('1.0',END)
    text1.insert('1.0',name + 'welcome to the window\n' + str(dt))




lab1 = Label(win,text = 'first name', bg = 'cyan', fg = 'red')
lab1.pack()
ent1 = Entry()
ent1.pack()
butten1 = Button(win,text = 'click here', bg = 'green',fg = 'white', command  = greet)
butten1.pack()
text1 = Text(win,bg = 'yellow',fg = 'red',width=200, height= 7 )
text1.pack()



win.mainloop()

