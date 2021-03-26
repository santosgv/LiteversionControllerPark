from tkinter import *
#import  database as b
main=Tk()

class Validadores():
    def validapraca(self):
        pass
    def validaveiculos(self):
        pass


class Aplicacao(Validadores):
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
    def Ipraca(self):
        nwwindow=Toplevel(self.principal,bg='white')
        nwwindow.geometry('250x184')
        nwwindow.title('Cadastrar Praca')
        nwwindow.resizable(False,False)

        Label(nwwindow,text='Vaga',bg='white').place(relx=0.01,rely=0.20)
        self.EtVaga=Entry(nwwindow)
        self.EtVaga.place(relx=0.35,rely=0.20)

        Label(nwwindow, text='Endereço',bg='white').place(relx=0.01, rely=0.40)
        self.EtEnd=Entry(nwwindow)
        self.EtEnd.place(relx=0.35,rely=0.40)

        self.BtCadvaga=Button(nwwindow,text='Cadastrar vaga',bg='green',command=self.validapraca)
        self.BtCadvaga.place(relx=0.30,rely=0.65)
    def IVeiculo(self):
        Iveiculos=Toplevel(self.principal,bg='white')
        Iveiculos.geometry('250x184')
        Iveiculos.title('Cadastrar Veiculos')
        Iveiculos.resizable(False,False)

        Label(Iveiculos,text='Placa',bg='white').place(relx=0.01,rely=0.20)
        self.Etplaca=Entry(Iveiculos)
        self.Etplaca.place(relx=0.20,rely=0.20,relwidth=0.20)

        Label(Iveiculos, text='Cor',bg='white').place(relx=0.01, rely=0.40)
        self.EtCor=Entry(Iveiculos)
        self.EtCor.place(relx=0.20,rely=0.40,relwidth=0.20)

        Label(Iveiculos,text='Tipo',bg='White').place(relx=0.50,rely=0.20)
        self.EtTipo=Entry(Iveiculos)
        self.EtTipo.place(relx=0.65,rely=0.20,relwidth=0.08)

        self.BtCadvaga=Button(Iveiculos,text='Cadastrar Veiculo',bg='green',command=self.validaveiculos)
        self.BtCadvaga.place(relx=0.30,rely=0.65)
    def LbandButtons(self):
        self.btpracas=Button(self.principal,text='Nova Praca',fg='White',bg='#836FFF',command=self.Ipraca)
        self.btpracas.place(relx=0.10,rely=0.10)

        self.btveiculo=Button(self.principal,text='Novo Veiculo',fg='White',bg='#836FFF',command=self.IVeiculo)
        self.btveiculo.place(relx=0.40,rely=0.10)

        self.btmovimentacao=Button(self.principal,text='Movimentacao',fg='White',bg='#836FFF')
        self.btmovimentacao.place(relx=0.70,rely=0.10)
Aplicacao()