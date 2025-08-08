from tkinter import *
from tkinter import messagebox
from os import system
system('pip install pillow')
#from PIL import Image, ImageTk

root = Tk()
root.title('denomination counter')
root.geometry('500x500')
#upload = Image.open('img.jpg')
#pload = upload.resize((300,300))
#img = ImageTk.PhotoImage(upload)
#label = Label(root, image = img)

#label.place(x=100,y=20)

label1 = Label(root, text = 'her user welcome to the denomination counter')
label1.place(x = 50, y = 350)


def msg():
    msgbox = messagebox.showinfo('alert', 'do you want to use?')
    if msgbox == 'ok':
        topwin()

button1 = Button(root, text = 'lets start', command=msg, bg = 'lightgray', fg ='black')
button1.place(x = 180, y= 360)

def topwin():
    def calculater():
        global amount
        amount = int(entry1.get())
        note2000 = amount//2000
        amount = amount%2000
        note500 = amount//500
        amount = amount%500
        note100 = amount//100
        amount = amount%100
        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))

    top = Toplevel()
    top.title('toplevel')
    top.geometry('400x400')
    label = Label(top,text = 'enter total amount')
    label.place(x= 100, y=100)
    entry1 = Entry(top)
    entry1.place(x = 180, y = 100)
    
    lb1 = Label(top, text = 'here are the numbers of notes for each welcome to the denomination calculater')
    l1 = Label(top,text = '2000')
    l2 = Label(top, text = '500')
    l3 = Label(top, text = '100')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    btn = Button(top, text= 'calculate', command = calculater)
    btn.place(x = 170,y = 100)
    entry1.place( x = 80, y = 100)

    l1.place(x = 150, y = 200)
    l2.place(x = 150, y = 230)
    l3.place(x = 150, y = 250)
    t1.place(x = 200, y = 200)
    t2.place(x = 200, y = 230)
    t3.place(x = 200, y = 250)

root.mainloop()
   


