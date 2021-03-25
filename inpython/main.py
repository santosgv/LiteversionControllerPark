from tkinter import *
import  database as b
main=Tk()


class Aplicacao():
    def __init__(self):
        self.main=main
        self.Telas()
        self.Frame()
        self.LbandButtons()
        main.mainloop()
    def Telas(self):
        self.main.title('Lite Park')
        self.main.configure(background='black')
        self.main.geometry('572x318')
        self.main.resizable(False,False)
    def Frame(self):
        self.principal=Frame(self.main,bg='white')
        self.principal.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)
    def LbandButtons(self):
        self.btpracas=Button(self.principal,text='Nova Praca',fg='White',bg='#836FFF',command=b.Banco.inserevaga)
        self.btpracas.place(relx=0.10,rely=0.10)

        self.btveiculo=Button(self.principal,text='Novo Veiculo',fg='White',bg='#836FFF',command=b.Banco.insereveiculo)
        self.btveiculo.place(relx=0.40,rely=0.10)

        self.btmovimentacao=Button(self.principal,text='Movimentacao',fg='White',bg='#836FFF')
        self.btmovimentacao.place(relx=0.70,rely=0.10)
Aplicacao()