from tkinter import *
import database

main=Tk()

class Validadores():
    def validapraca(self):
        banco=database.Banco()
        endereco=int(self.EtEnd.get())
        banco.inserevaga(self.EtVaga.get(),endereco)
        if banco !=True:
            self.St['text']=('Praca cadastrada')

    def validaveiculos(self):
        veiculo=database.Banco()
        tipo=int(self.EtTipo.get())
        veiculo.insereveiculo(self.Etplaca.get(),self.EtCor.get(),tipo)
        if veiculo !=True:
            self.Stsvaiculo['text']='Veiculo Cadastrado'

    def movimentacao(self):
        pass

class Aplicacao(Validadores):
    def __init__(self):
        self.main=main
        self.Telas()
        self.Frame()
        self.Menus()
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
        self.St=Label(nwwindow,text="",bg='white')
        self.St.place(relx=0.30,rely=0.80)
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

        self.BtCadvaiculo=Button(Iveiculos,text='Cadastrar Veiculo',bg='green',command=self.validaveiculos)
        self.BtCadvaiculo.place(relx=0.30,rely=0.65)

        self.Stsvaiculo=Label(Iveiculos,text='',bg='white')
        self.Stsvaiculo.place(relx=0.30,rely=0.80)
    def Imovimentacao(self):
        iMovie=Toplevel(self.principal,bg='white')
        iMovie.geometry('250x184')
        iMovie.title('Movimentacao de Praca')
        iMovie.resizable(False,False)
        Button(iMovie,text='Movimentacao de Praca',command=self.movimentacao).place(relx=0.01,rely=0.10)
    def LbandButtons(self):
        Button(self.principal,text='Movimentacao',fg='White',bg='#836FFF',command=self.Imovimentacao).place(relx=0.05,rely=0.10)
        Button(self.principal,text='Registrar entrada',fg='white',bg='#836FFF').place(relx=0.42,rely=0.10)
        Button(self.principal,text='Registrar saida',fg='white',bg='#836FFF').place(relx=0.80,rely=0.10)
    def Menus(self):
        menubar=Menu(self.main)
        self.main.config(menu=menubar)
        Menumain=Menu(menubar)
        def Quit(): self.main.destroy()
        menubar.add_cascade(label='Cadastros',menu=Menumain)
        Menumain.add_command(label='Cadastrar Vaga',command=self.Ipraca)
        Menumain.add_command(label='Cadastrar veiculos',command=self.IVeiculo)
        Menumain.add_command(label='Sair',command=Quit)

Aplicacao()