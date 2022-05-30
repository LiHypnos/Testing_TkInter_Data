from tkinter import *
import math
#back-end
lk=eval
error='ERRO: não utilize letras para fazer calculos'
def imprimir():
    label1['text'] = entry1.get()
def calcular():
    label1['text'] = entry1.get()
    entry1.get()
    uk=lk(entry1.get())
    label1['text'] = uk



#criar a janela
janela = Tk()
janela.title('Windows Execute')
janela.geometry('400x200+100+500')#perguntar o porquê de ter +100 e +500 dps
janela.minsize(width=400, height=200)#definir tamanho minimo da janela
janela.maxsize(width=1200, height=600)#definir tamanho maximo da janela
janela.config(bg=('#810F5F'))#definir a cor de background da janela
#criar os widgets
label1 = Label(janela, text='Comece a digitar :D',font='Arial 16',background='dark blue', foreground='yellow')
entry1 = Entry(janela,font='Arial 13')
btn=Button(janela,text='sair :(', font='Arial 10', command=quit, background='light blue')
btn2=Button(janela,text='Imprimir',font='Arial 10', command=imprimir, background='light blue')
btn3=Button(janela,text='Calcular', font='Arial 10', command=calcular, background='light blue')

#organizar os widgets
label1.pack()
entry1.pack()
btn.pack()
btn2.pack()
btn3.pack()
#executar a janelaa
janela.mainloop()