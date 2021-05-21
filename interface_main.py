# from tkinter import *
#
# from main import CompileRepo
# from scraping.scrapy_data_full import get_data_repository_full
#
# root = Tk()
#
# lista = Listbox(root, width=50, height=25)
#
# lista.pack()
#
# data = get_data_repository_full('Erickson-lopes-dev/Dica_Python_Linkedin')
#
# print(data)
#
# for file in data:
#     if file['type_file'] == 'File' and file['extension'] != 'Go to parent directory':
#         lista.insert(END, file['url'])
#
# root.mainloop()

from tkinter import *
from tkinter import ttk

from scraping.scrapy_data_full import get_data_repository_full
from scraping.scrapy_lines_bytes import get_lines_bytes

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws['bg'] = '#fb0'

tv = ttk.Treeview(ws)
tv['columns'] = ('Name File', 'Extension', 'Lines', 'Size')
tv.column('#0', width=0, stretch=NO)
tv.column('Name File', anchor=CENTER, width=90)
tv.column('Extension', anchor=CENTER, width=80)
tv.column('Lines', anchor=CENTER, width=80)
tv.column('Size', anchor=CENTER, width=80)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('Name File', text='Name File', anchor=CENTER)
tv.heading('Extension', text='Extension', anchor=CENTER)
tv.heading('Lines', text='Lines', anchor=CENTER)
tv.heading('Size', text='Size', anchor=CENTER)

data = get_data_repository_full('Erickson-lopes-dev/Compile-Repo')

for num, file in enumerate(data):
    if file['type_file'] == 'File' and file['extension'] != 'Go to parent directory':
        lb = get_lines_bytes('https://github.com' + file['url'])
        # Adiciona uma linha na tabela
        tv.insert(parent='', index=num, iid=num, text='', values=(file['name'],
                                                                  file['extension'],
                                                                  lb[0],
                                                                  lb[1]))

tv.pack()

ws.mainloop()
