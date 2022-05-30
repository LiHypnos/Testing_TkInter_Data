from tkinter import *
import webbrowser

janela = Tk()
janela.title('Janela (juraaaaa limnda?)')
janela.geometry ('500x300')
def imprimirdados():
    print('================')
    print('digitou isso aqui bb?\n%s'%nome.get())

janela.configure(background = 'Violet')

text = Label(janela,text='POVO GLS ANIMADE',background = 'black', foreground= 'white').place(x=199,y=150,height=60,width=150)

nome = Entry(janela)
nome.place(x=170,y=40,height=60,width=200)

botao = Button(janela,text='Sair do maioral',background='light blue',foreground='black',command=janela.destroy)
botao.place(x=300,y=250)
botao2 = Button(janela,text='imprime né bb',background='light blue',foreground='black',command=imprimirdados)
botao2.place(x=100,y=250)






#vanilla code to open a new webbrowser jureee
new = 1
url = "https://www.google.com"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(janela, text = "Isso vai abrir o mero mero juraaaaa",command=openweb).place(x=200,y=250)


janela.mainloop()