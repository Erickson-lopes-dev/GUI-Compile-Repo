from tkinter import *
from tkinter import ttk
from tqdm import tqdm
from scraping.scrapy_data_full import get_data_repository_full
from scraping.scrapy_lines_bytes import get_lines_bytes
import webbrowser

repo = 'Erickson-lopes-dev/Compile-Repo'

# Carrega os dados
data = get_data_repository_full(repo)


# Centraliza a GUI
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
# Titulo da GUI
ws.title(f'Compile Repo GUI ({repo})')

# impedir redimensionamento
ws.resizable(False, False)

# Centralizando
janela_centralizada = Centralizar(ws, 600, 640)
janela_centralizada.centralizado()

# gerando frame
frame = Frame(ws)

# Gerando tabela
tabela = ttk.Treeview(frame, height=25)
tabela['columns'] = ('Name File', 'Extension', 'Lines', 'Size')
tabela.column('#0', width=0, stretch=NO)
tabela.column('Name File', anchor=CENTER, width=200)
tabela.column('Extension', anchor=CENTER, width=80)
tabela.column('Lines', anchor=CENTER, width=80)
tabela.column('Size', anchor=CENTER, width=80)

# Cabeçalho
tabela.heading('#0', text='', anchor=CENTER)
tabela.heading('Name File', text='Nome do Arquivo', anchor=CENTER)
tabela.heading('Extension', text='Extensão', anchor=CENTER)
tabela.heading('Lines', text='Qtd. Linhas', anchor=CENTER)
tabela.heading('Size', text='Tamanho', anchor=CENTER)


def on_double_click(event=FALSE):
    item = tabela.selection()
    for i in item:
        # Abre o navegador a partir do ultimo item dos valores(o link para o arquivo)
        webbrowser.open('https://github.com' + tabela.item(i, "values")[-1])


# adiciona os itens na tabela
for num, file in enumerate(tqdm(data, desc='Construindo Tabela')):
    if file['type_file'] == 'File' and file['extension'] != 'Go to parent directory':
        lb = get_lines_bytes('https://github.com' + file['url'])
        # Adiciona uma linha na tabela
        tabela.insert(parent='', index=num, iid=num, text='', values=(file['name'],
                                                                      file['extension'] if '.' in file[
                                                                          'name'] else '',
                                                                      lb[0] if lb[0] != 0 else '',
                                                                      lb[1],
                                                                      file['url']))

# Evendo do double click
tabela.bind('<Double-1>', on_double_click)

# Criação da label e botao
label_repo_name = Label(frame, text=repo.split('/')[1], font='Arial 18')
botao_link = Button(frame, text='Abrir Arquivo ', width=15, height=2, command=on_double_click)

# Exebindo e configurando posição dos itens
label_repo_name.grid(row=0, column=0)
botao_link.grid(row=2, column=0, pady=20)
tabela.grid(row=1, column=0)
frame.pack()

frame.mainloop()
