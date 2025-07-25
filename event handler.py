from tkinter import messagebox
from tkinter import*



win = Tk()
win.title('event handler')
win.geometry('500x500')
win.configure(bg = 'tomato')

def kp(event):
    print(event.char)

win.bind('<Key>', kp)
def click(event):
    print('butten is clicked')

buttom1 = Button(win,text = 'click on me!')
buttom1.pack()
buttom1.bind('<Button-1>',click)




win.mainloop()