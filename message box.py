from tkinter import messagebox
from tkinter import*


win = Tk()
win.title('event handler')
win.geometry('500x500')
win.configure(bg = 'tomato')

def msg():
    messagebox.showwarning('alert', 'issue detected')
button1 = Button(win,text= 'Click here', command = msg)
button1.pack()
win.mainloop()