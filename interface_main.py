from tkinter import *

from main import CompileRepo
from scraping.scrapy_data_full import get_data_repository_full

root = Tk()

lista = Listbox(root, width=50, height=25)

lista.pack()

data = get_data_repository_full('Erickson-lopes-dev/Dica_Python_Linkedin')

print(data)

for file in data:
    if file['type_file'] == 'File' and file['extension'] != 'Go to parent directory':
        lista.insert(END, file['url'])

root.mainloop()
