from tkinter import *
from datetime import datetime
import random

root = Tk()
root.title('resturant management system')
root.geometry('800x400')
root.configure(bg='beige')
frame1 = Frame(root,width = 500,height = 300,relief= SUNKEN, bg='beige')
frame1.pack()
label1 = Label(frame1, font =("arial",18, ' bold'))

label1 = Label(frame1,font= ('arial',18,'bold'),text ="Resturant managment system",bg = 'firebrick')
label1.grid(row=0, column=0, columnspan = 4, padx =10,pady= 10)


drink = StringVar()
pizza = StringVar()
burger= StringVar()
largeburger= StringVar()
fries= StringVar()


labeldrink = Label(frame1, text = 'Drink',fg = 'tomato', font =('Times', 12, 'bold'))
labeldrink.grid(row=3, column = 0,padx=10, pady= 10)
entrydrink= Entry(frame1,textvariable= drink, justify= RIGHT)
entrydrink.insert(END,0)
entrydrink.grid(row=3, column = 1,padx=10, pady= 10)


labelpizza = Label(frame1, text = 'Pizza',fg = 'tomato', font =('Times', 12, 'bold'))
labelpizza.grid(row=4, column = 0,padx=10, pady= 10)
entrypizza= Entry(frame1,textvariable= pizza, justify= RIGHT)
entrypizza.grid(row=4, column = 1,padx=10, pady= 10)
entrypizza.insert(END,0)


labelburger = Label(frame1, text = 'burger',fg = 'tomato', font =('Times', 12, 'bold'))
labelburger.grid(row=5, column = 0,padx=10, pady= 10)
entryburger= Entry(frame1,textvariable= burger, justify= RIGHT)
entryburger.grid(row=5, column = 1,padx=10, pady= 10)
entryburger.insert(END,0)

labellargeburger = Label(frame1, text = 'large burger',fg = 'tomato', font =('Times', 12, 'bold'))
labellargeburger.grid(row=6, column = 0,padx=10, pady= 10)
entrylargeburger= Entry(frame1,textvariable= largeburger, justify= RIGHT)
entrylargeburger.grid(row=6, column = 1,padx=10, pady= 10)
entrylargeburger.insert(END,0)

labelfries = Label(frame1, text = 'fries',fg = 'tomato', font =('Times', 12, 'bold'))
labelfries.grid(row=7, column = 0,padx=10, pady= 10)
entryfries= Entry(frame1,textvariable= fries, justify= RIGHT)
entryfries.grid(row=7, column = 1,padx=10, pady= 10)
entryfries.insert(END,0)




labelorderno = Label(frame1, text = 'Order no.',fg = 'tomato', font =('Times', 12, 'bold'))
labelorderno.grid(row=3, column = 2)
entryorderno= Entry(frame1)
entryorderno.grid(row=3, column = 3)

labelcost = Label(frame1, text = 'cost',fg = 'tomato', font =('Times', 12, 'bold'))
labelcost.grid(row=4, column = 2)
entrycost= Entry(frame1)
entrycost.grid(row=4, column = 3)


labelservice = Label(frame1, text = 'service',fg = 'tomato', font =('Times', 12, 'bold'))
labelservice.grid(row=5, column = 2)
entryservice= Entry(frame1)
entryservice.grid(row=5, column = 3)

labeltax = Label(frame1, text = 'Tax',fg = 'tomato', font =('Times', 12, 'bold'))
labeltax.grid(row=7, column = 2)
entrytax= Entry(frame1)
entrytax.grid(row=7, column = 3)

labeltotal = Label(frame1, text = 'Total',fg = 'tomato', font =('Times', 12, 'bold'))
labeltotal.grid(row=6, column = 2)
entrytotal= Entry(frame1)
entrytotal.grid(row=6, column = 3)

def ex():
    root.destroy()
def reset():
    entryburger.delete(0,END)
    entrydrink.delete(0,END)
    entryfries.delete(0,END)
    entrylargeburger.delete(0,END)
    entrypizza.delete(0,END)



    entrydrink.insert(END,0)
    entrypizza.insert(END,0)
    entryburger.insert(END,0)


    entrycost.delete(0,END)
    entrylargeburger.insert(END,0)
    entryfries.insert(END,0)
    entryorderno.delete(0,END)
    entryservice.delete(0,END)
    entrytax.delete(0,END)
    entrytotal.delete(0,END)

def total():
    global drink
    global burger
    global largeburger
    global fries
    global pizza

    drink = float(drink.get())
    burger = float(burger.get())
    largeburger= float(largeburger.get())
    fries = float(fries.get())
    pizza = float(pizza.get())

    cost = 20 * drink + 200 * burger + 350 * largeburger + 250 * fries + 350 * pizza
    print(cost)
    entrycost.insert(1,str(cost))
    service =  cost * 0.02
    entryservice.insert(0,str('Rs %.2f'% service))
    tax = cost*0.1
    entrytax.insert(0,str('Rs %.2f'% service))
    totalcost = cost+service+tax
    entrytotal.insert(0,str('Rs %.2f'% totalcost))
    rand = random.randint(1,10000)
    entryorderno.insert(0,str(rand))

def price():
    top = Toplevel()
    top.geometry('300x300')
    top.title('toplevel')
    l2 = Label(top, text = 'price', font = ('Times', 22, 'bold'))
    l3 = Label(top, text = 'Drink Rs.20', font = ('Times', 22, 'bold'))
    l4 = Label(top, text = ' burger Rs. 200', font = ('Times', 22, 'bold'))
    l5 = Label(top, text = 'largeburger Rs 350', font = ('Times', 22, 'bold'))
    l6 = Label(top, text = 'fries Rs.250', font = ('Times', 22, 'bold'))
    l7 = Label(top, text = 'pizza Rs.350', font = ('Times', 22, 'bold'))
    l2.pack()
    l3.pack()
    l4.pack()
    l5.pack()
    l6.pack()
    l7.pack()


button1 = Button(frame1, text = 'price' ,fg= 'tomato', font=('Times', 12,'bold'),bg= 'firebrick', command= price, padx =10,pady=10)
button1.grid(row = 10, column = 0, padx = 10,pady = 10)
button2 = Button(frame1, text = 'total', fg= 'tomato', font=('Times', 12,'bold'),bg= 'firebrick', command= total, padx =10,pady=10)
button2.grid(row = 10, column = 1, padx = 10,pady = 10)
button3 = Button(frame1, text = 'reset' ,fg= 'tomato', font=('Times', 12,'bold'),bg= 'firebrick', command= reset, padx =10,pady=10)
button3.grid(row = 10, column = 2, padx = 10,pady = 10)
button4 = Button(frame1, text = 'Exit' ,fg= 'tomato', font=('Times', 12,'bold'),bg= 'firebrick', command= exit, padx =10,pady=10)
button4.grid(row = 10, column = 3, padx = 10,pady = 10)


root.mainloop()


