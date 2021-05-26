from tkinter import *
from Funcao_Classes import *


# instância objeto para criação do tkinter
janela_principal = Tk()

# Centralizando aplicativo ao centro
janela_centralizada = Centralizar(janela_principal, 443, 335)
janela_centralizada.centralizado()

# Título do programa
janela_principal.title('FL - Folder list')

# adicionar iconê
janela_principal.iconbitmap('imagens/icon.ico')

# impedir redimensionamento
# janela_principal.resizable(False, False)

# # strings de uso em lista
# var_lista_detalhes = StringVar()

# menu
meu_menu = Menu(janela_principal)
janela_principal.config(menu=meu_menu)  # colocando visivel dentro da janela_principal
criar_menu = Menu(meu_menu, tearoff=0)
criar_menu.add_command(label='Novo', command=lambda: formulario_novo())
criar_menu.add_command(label='Editar')
meu_menu.add_cascade(label='Criar', menu=criar_menu)

# Frames --------------------------------|
# frame principal
frame_principal = Frame(janela_principal)

# widgets -------------------------------|
lista_detalhes = Listbox(frame_principal, width=40, height=15, font='Arial 10')
lista_chamar = Listbox(frame_principal, width=13, height=12, font='Arial 15')
btn_chamar = Button(frame_principal, text='Executar', width=10, height=2)
btn_deletar = Button(frame_principal, text='Deletar', width=10, height=2)

# Grid ---------------------------------|
frame_principal.pack()
# dentro da frame principal

lista_detalhes.grid(row=0, rowspan=3, column=0, columnspan=2)
btn_chamar.grid(row=3, rowspan=3, column=0)
btn_deletar.grid(row=3, rowspan=3, column=1)

lista_chamar.grid(row=0, rowspan=4, column=2)

preencher_listas(lista_detalhes, lista_chamar)
# Compila, e exibe
janela_principal.mainloop()
