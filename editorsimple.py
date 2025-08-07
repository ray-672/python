from tkinter import *
from tkinter.filedialog import askopenfile,asksaveasfile

window = Tk()

window.title('text editor')
window.geometry('500x500')

def openfile():
    file1 = askopenfile(mode = 'r', filetypes=[('text files','*.txt')])
    content = file1.read()
    text1.delete('1.0', 'end')
    text1.insert(END,content)


def saveas():
    file1 = asksaveasfile(mode = 'w', filetypes=[('text files','*.txt')])

    if file1 is not None:
        content = text1.get('1.0','END')
        file1.write(content)



text1 = Text(window,bg = 'lightgray', fg = 'tomato', width = 50, height = 20, borderwidth=4, relief = 'groove')

button1 = Button(window,text = 'open', command = openfile)
button2 = Button(window,text = 'save as...', command = saveas)

button1.grid(row = 0, column=0)
button2.grid(row = 1, column=0)
text1.grid(row=0,column =1, rowspan = 2)


window.mainloop()


