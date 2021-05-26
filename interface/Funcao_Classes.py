from tkinter import *
from tkinter import filedialog
import os


# ajuda a centralizar o programa na tela de qualquer computador
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


def pegar_arquivo():
    return filedialog.askopenfilename()


# tentar criar uma classe
def formulario_novo():
    # declara uma TopLavel para abrir outra janela
    top = Toplevel()

    # titulo Dessa janela
    top.title('Adicionar novo função')

    # declarção de widgets
    frame_lt = Frame(top)
    label_nome = Label(frame_lt, text='Nome da pasta')
    text_nome = Entry(frame_lt)

    frame_lbbb = Frame(top)
    lista_item = Listbox(frame_lbbb, width=50)
    btn_salvar = Button(frame_lbbb, text='Salvar', width=10, height=2)
    btn_inserir = Button(frame_lbbb, text='+ Programa', width=10, height=2,
                         command=lambda: pegar_arquivo())
    btn_delete = Button(frame_lbbb, text='Deletar', width=10, height=2)

    # declaração de exibição dos widgets
    label_nome.grid(row=0, column=0)
    text_nome.grid(row=0, column=1)
    frame_lt.grid(row=0, column=0)

    frame_lbbb.grid(row=1, column=0, columnspan=1, pady=10)
    lista_item.grid(row=1, column=0, columnspan=3)
    btn_delete.grid(row=2, column=1)
    btn_inserir.grid(row=2, column=0)
    btn_salvar.grid(row=2, column=2)

    # declaração da classe que centraliza
    top_centralizado = Centralizar(top, 304, 240)
    top_centralizado.centralizado()


def preencher_listas(lista_d, lista_c):
    # abre o arquivo
    with open('salvos/save.txt', encoding='UTF-8') as arquivo:
        # armazena tudo que encontrou por linha e transforma em linha
        arquivo = arquivo.readlines()

        # por item da lsita encontrado ele inseri dentro da lista(textbox)
        for linha in range(len(arquivo)):
            lista_aquivo = arquivo[linha].replace('\n', '')
            lista_aquivo = arquivo[linha].replace(',', '')
            if linha != 0:
                lista_d.insert(END, lista_aquivo)
            else:
                lista_c.insert(END, lista_aquivo)
