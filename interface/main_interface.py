from tkinter import *

root = Tk()

lista = Listbox(root)

lista.pack()

lista.insert(0, 'item')
lista.insert(1, 'item1')

root.mainloop()
