from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo('Are you?', 'Oh he gay')
    print('Thanks bro')
    quit()

def moveMouse(event):
    yes.place(x=random.randint(50, 550), y=random.randint(50, 550))

root = Tk()
root.geometry('600x600')
root.title('Are you?')
root.resizable(width=False, height=False)
root['bg'] = '#f0f0f0'

label = Label(root, text='Are you gay?', font='Arial 24 bold', bg='#f0f0f0', fg='#333333')
label.pack(pady=50)

yes = Button(root, text='No', font='Arial 20 bold', bg='#4caf50', fg='white')
yes.place(x=170, y=200)
yes.bind('<Enter>', moveMouse)

nono = Button(root, text='Yes', font='Arial 20 bold', bg='#f44336', fg='white', command=no)
nono.place(x=350, y=200)

root.mainloop()
