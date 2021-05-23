from tkinter import *
from tkinter import ttk
from tqdm import tqdm
from scraping.scrapy_data_full import get_data_repository_full
from scraping.scrapy_lines_bytes import get_lines_bytes

data = get_data_repository_full('Erickson-lopes-dev/Dicas_Pandas_Linkedin')


class Centralizar:
    def __init__(self, janela, largura, altura):
        self.janela = janela
        self.largura = largura
        self.altura = altura

        largura_sistema = janela.winfo_screenwidth()
        altura_sistema = janela.winfo_screenheight()

        self.posicao_x = int(largura_sistema / 2 - largura / 2)
        self.posicao_y = int(altura_sistema / 2 - altura / 2)

    def centralizado(self):
        return self.janela.geometry('{}x{}+{}+{}'.format(self.largura,
                                                         self.altura,
                                                         self.posicao_x,
                                                         self.posicao_y))


ws = Tk()
ws.title('PythonGuides')
# ws.geometry('600x600')
# ws['bg'] = '#fb0'

janela_centralizada = Centralizar(ws, 600, 600)
janela_centralizada.centralizado()

tv = ttk.Treeview(ws, height=25)
tv['columns'] = ('Name File', 'Extension', 'Lines', 'Size')
tv.column('#0', width=0, stretch=NO)
tv.column('Name File', anchor=CENTER, width=200)
tv.column('Extension', anchor=CENTER, width=80)
tv.column('Lines', anchor=CENTER, width=80)
tv.column('Size', anchor=CENTER, width=80)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('Name File', text='Name File', anchor=CENTER)
tv.heading('Extension', text='Extension', anchor=CENTER)
tv.heading('Lines', text='Lines', anchor=CENTER)
tv.heading('Size', text='Size', anchor=CENTER)

for num, file in enumerate(tqdm(data, desc='Construindo Tabela')):
    if file['type_file'] == 'File' and file['extension'] != 'Go to parent directory':
        lb = get_lines_bytes('https://github.com' + file['url'])
        # Adiciona uma linha na tabela
        tv.insert(parent='', index=num, iid=num, text='', values=(file['name'],
                                                                  file['extension'] if '.' in file['name'] else '',
                                                                  lb[0] if lb[0] != 0 else '',
                                                                  lb[1]))

tv.pack()
