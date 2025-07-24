from tkinter import *

win = Tk()
win.title('~numnber pad')
win.geometry('300x400')
win.configure(bg = 'black')

t = [[7,8,9],[4,5,6],[1,2,3]]

for i in range(3):
    win.rowconfigure(i,weight = 0,minsize = 80)
    for j in range(3):
        win.columnconfigure(j,weight = 0, minsize = 80)

        lab1 = Label(win,text = t[i][j],relief= 'raised', bg = 'black', fg = 'tomato')
        lab1.grid(row = i,column = j)

win.mainloop()