from tkinter import *

win = Tk()
win.title('Password + login')
win.geometry('500x500')
win.configure(bg = 'tomato')

def log():
    name = entry1.get()

    greet = 'login was successful  '+name
    text1.delete('1.0', 'end')

    text1.insert(END, greet )


f1 = Frame(win, bg = 'tomato',relief = 'ridge' , width = 500, height = 13, border= 3)
f1.pack()
entry1 = Entry(f1)
lab1 = Label(f1,text = 'Name',bg = 'light blue', font = ('arial', 12, 'bold'))

lab2 = Label(f1,text = 'password',bg = 'light blue', font = ('arial', 12, 'bold'))
entry2= Entry(f1,show= "*")
button = Button(f1,text = 'login', command = log)
lab1.grid(row = 1 , column = 0)
entry1.grid(row = 1 , column = 1)
lab2.grid(row = 2 , column = 0)
entry2.grid(row = 2 , column = 1)
button.grid(row = 3 , column = 0, columnspan = 2,)
text1 = Text(win,bg = 'skyblue', font = ('arial', 12, 'bold'), width = 300, height = 7)
text1.pack()


win.mainloop()

