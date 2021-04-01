from tkinter import *
import database
from time import strftime
from tkinter import ttk

main = Tk()


class Validadores():
    def validapraca(self):
        banco = database.Banco()
        endereco = int(self.EtEnd.get())
        banco.inserevaga(self.EtVaga.get(), endereco)
        if banco != True:
            self.St['text'] = ('Praca cadastrada')

    def validaveiculos(self):
        veiculo = database.Banco()
        tipo = int(self.EtTipo.get())
        veiculo.insereveiculo(self.Etplaca.get(), self.EtCor.get(), tipo)
        if veiculo != True:
            self.Stsvaiculo['text'] = 'Veiculo Cadastrado'

    def movimentacao(self):
        pass

    def Regentrada(self):
        entrada = database.Banco()
        entrada.Regientrada()


class Aplicacao(Validadores):
    def __init__(self):
        self.main = main
        self.Telas()
        self.Frame()
        self.Menus()
        self.LbandButtons()
        main.mainloop()

    def Telas(self):
        self.main.title('Lite Park')
        self.main.configure(background='black')
        self.main.geometry('572x318')
        self.main.resizable(False, False)

    def Frame(self):
        self.principal = Frame(self.main, bg='white')
        self.principal.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def Ipraca(self):
        nwwindow = Toplevel(self.principal, bg='white')
        nwwindow.geometry('250x184')
        nwwindow.title('Cadastrar Praca')
        nwwindow.resizable(False, False)

        Label(nwwindow, text='Vaga', bg='white').place(relx=0.01, rely=0.20)
        self.EtVaga = Entry(nwwindow)
        self.EtVaga.place(relx=0.35, rely=0.20)

        Label(nwwindow, text='Endereço', bg='white').place(relx=0.01, rely=0.40)
        self.EtEnd = Entry(nwwindow)
        self.EtEnd.place(relx=0.35, rely=0.40)

        self.BtCadvaga = Button(nwwindow, text='Cadastrar vaga', bg='green', command=self.validapraca)
        self.BtCadvaga.place(relx=0.30, rely=0.65)
        self.St = Label(nwwindow, text="", bg='white')
        self.St.place(relx=0.30, rely=0.80)

    def IVeiculo(self):
        Iveiculos = Toplevel(self.principal, bg='white')
        Iveiculos.geometry('250x184')
        Iveiculos.title('Cadastrar Veiculos')
        Iveiculos.resizable(False, False)

        Label(Iveiculos, text='Placa', bg='white').place(relx=0.01, rely=0.20)
        self.Etplaca = Entry(Iveiculos)
        self.Etplaca.place(relx=0.20, rely=0.20, relwidth=0.20)

        Label(Iveiculos, text='Cor', bg='white').place(relx=0.01, rely=0.40)
        self.EtCor = Entry(Iveiculos)
        self.EtCor.place(relx=0.20, rely=0.40, relwidth=0.20)

        Label(Iveiculos, text='Tipo', bg='White').place(relx=0.50, rely=0.20)
        self.EtTipo = Entry(Iveiculos)
        self.EtTipo.place(relx=0.65, rely=0.20, relwidth=0.08)

        self.BtCadvaiculo = Button(Iveiculos, text='Cadastrar Veiculo', bg='green', command=self.validaveiculos)
        self.BtCadvaiculo.place(relx=0.30, rely=0.65)

        self.Stsvaiculo = Label(Iveiculos, text='', bg='white')
        self.Stsvaiculo.place(relx=0.30, rely=0.80)

    def Ishowvec(self):
        Ishowveiculo = Toplevel(self.principal, bg='white')
        Ishowveiculo.geometry('250x250')
        Ishowveiculo.title('Todos os veiculos')
        Ishowveiculo.resizable(False, False)
        self.grid = ttk.Treeview(Ishowveiculo, columns=('col1', 'col2', 'col3', 'col4'), show='headings')
        self.grid.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.95)
        self.grid.column('#0', width=0, minwidth=0)
        self.grid.column('col1', minwidth=0, width=20)
        self.grid.column('col2', minwidth=0, width=50)
        self.grid.column('col3', minwidth=0, width=50)
        self.grid.column('col4', minwidth=0, width=20)
        self.grid.heading('#0', text='')
        self.grid.heading('#1', text='ID')
        self.grid.heading('#2', text='PLACA')
        self.grid.heading('#3', text='COR')
        self.grid.heading('#4', text='T')
        self.grid.pack()

        def Gredviw():
            banco = database.Banco()
            a = banco.show_veiculos()
            for i in a:
                self.grid.insert("", END, values=i)
        Gredviw()

    def Imovimentacao(self):
        iMovie = Toplevel(self.principal, bg='white')
        iMovie.geometry('250x184')
        iMovie.title('Movimentacao de Praca')
        iMovie.resizable(False, False)
        Button(iMovie, text='Movimentacao de Praca', command=self.movimentacao).place(relx=0.01, rely=0.10)

    def Ientrada(self):
        ientrada = Toplevel(self.principal, bg='white')
        ientrada.geometry('250x184')
        ientrada.title('Entrada de veiculo')
        ientrada.resizable(False, False)
        Label(ientrada, text='Codigo veiculo', bg='white').place(relx=0.35, rely=0.01)
        self.entent = Entry(ientrada)
        self.entent.place(relx=0.20, rely=0.15)
        Button(ientrada, text='Exibir veiculos', command=self.Ishowvec).place(relx=0.30, rely=0.60)
        Button(ientrada, text='registrar').place(relx=0.35, rely=0.80)

    def LbandButtons(self):
        Button(self.principal, text='Movimentacao', fg='White', bg='#836FFF', command=self.Imovimentacao).place(
            relx=0.05, rely=0.10)
        Button(self.principal, text='Registrar entrada', fg='white', bg='#836FFF', command=self.Ientrada).place(
            relx=0.42, rely=0.10)
        Button(self.principal, text='Registrar saida', fg='white', bg='#836FFF').place(relx=0.80, rely=0.10)

        self.lb_relogio = Label(self.main, background='white', font=('verdana', 12))
        self.lb_relogio.place(relx=0.35, rely=0.90, relwidth=0.25, relheight=0.08)

        def tic():
            data_e_hora = strftime('%d/%m/%y %H:%M')
            self.lb_relogio['text'] = data_e_hora

        def tac():
            tic()
            self.lb_relogio.after(1000, tac)

        tac()

    def Menus(self):
        menubar = Menu(self.main)
        self.main.config(menu=menubar)
        Menumain = Menu(menubar)

        def Quit(): self.main.destroy()

        menubar.add_cascade(label='Cadastros', menu=Menumain)
        Menumain.add_command(label='Cadastrar Vaga', command=self.Ipraca)
        Menumain.add_command(label='Cadastrar veiculos', command=self.IVeiculo)
        Menumain.add_command(label='Sair', command=Quit)


Aplicacao()
