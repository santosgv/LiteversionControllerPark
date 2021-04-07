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

    def Regentrada(self):
        entrada = database.Banco()
        veiculo=int(self.entent.get())
        vaga=int(self.self.entrpraca.get())
        entrada.Regientrada(veiculo,vaga)
        if veiculo !=True:
            self.lbentrada['text']="Entrada registrada"

    def Regsaida(self):
        saida=database.Banco()
        idsaida=int(self.entsaida.get())
        saida.Regisaida(idsaida)
        if saida !=True:
            self.lbsaida['text']="SAIDA REGISTRADA"

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
        Ishowveiculo.geometry('300x250')
        Ishowveiculo.title('Todos os veiculos')
        Ishowveiculo.resizable(True, True)
        self.grid = ttk.Treeview(Ishowveiculo, columns=('col1', 'col2', 'col3', 'col4'), show='headings')
        self.grid.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.95)
        self.grid.column('#0', width=0, minwidth=0)
        self.grid.column('col1', minwidth=0, width=50)
        self.grid.column('col2', minwidth=0, width=100)
        self.grid.column('col3', minwidth=0, width=100)
        self.grid.column('col4', minwidth=0, width=20)
        self.grid.heading('#0', text='')
        self.grid.heading('#1', text='ID')
        self.grid.heading('#2', text='PLACA')
        self.grid.heading('#3', text='COR')
        self.grid.heading('#4', text='T')
        self.grid.pack()

        def Gredviw():
            self.grid.delete(*self.grid.get_children())
            banco = database.Banco()
            resultado=banco.cur.execute(f'''select ID,PLACA,COR,TIPO from VEICULO order by PLACA asc''')

            for linhas in resultado:
                self.grid.insert("", END, values=(linhas[0],linhas[1],linhas[2],linhas[3]))
        Gredviw()

    def Ientrada(self):
        ientrada = Toplevel(self.principal, bg='white')
        ientrada.geometry('250x184')
        ientrada.title('Entrada de veiculo')
        ientrada.resizable(False, False)
        Label(ientrada, text='Codigo veiculo', bg='white').place(relx=0.30, rely=0.01)
        self.entent = Entry(ientrada)
        self.entent.place(relx=0.20, rely=0.15)

        Label(ientrada, text='Codigo da praca', bg='white').place(relx=0.01, rely=0.30)
        self.entrpraca=Entry(ientrada)
        self.entrpraca.place(relx=0.45, rely=0.30)

        Button(ientrada, text='Exibir veiculos', command=self.Ishowvec).place(relx=0.30, rely=0.60)
        Button(ientrada, text='registrar',command=self.Regentrada).place(relx=0.35, rely=0.80)
        self.lbentrada=Label(ientrada,text='',bg='white')
        self.lbentrada.place(relx=0.25, rely=0.40)

    def Iocupacao(self):
        Iocupado = Toplevel(self.principal, bg='white')
        Iocupado.geometry('350x250')
        Iocupado.title('Ocupacao')
        Iocupado.resizable(True, True)
        self.gridocupado = ttk.Treeview(Iocupado, columns=('col1', 'col2', 'col3', 'col4','col5'), show='headings')
        self.gridocupado.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.95)
        self.gridocupado.column('#0', width=0, minwidth=0)
        self.gridocupado.column('col1', minwidth=0, width=20)
        self.gridocupado.column('col2', minwidth=0, width=100)
        self.gridocupado.column('col3', minwidth=0, width=100)
        self.gridocupado.column('col4', minwidth=0, width=100)
        self.gridocupado.column('col5', minwidth=0, width=20)
        self.gridocupado.heading('#0', text='')
        self.gridocupado.heading('#1', text='ID')
        self.gridocupado.heading('#2', text='ENTRADA')
        self.gridocupado.heading('#3', text='PLACA')
        self.gridocupado.heading('#4', text='COR')
        self.gridocupado.heading('#5', text='T')
        self.gridocupado.pack()

        def Gredviw():
            self.gridocupado.delete(*self.gridocupado.get_children())
            banco = database.Banco()
            resultado=banco.cur.execute(f'''select A.ID,A.DATAINICIO,B.PLACA,B.COR,B.TIPO from movimentacao A JOIN VEICULO B ON A.VEICULO=B.ID where OCUPADO='S'
            ''')

            for linhas in resultado:
                self.gridocupado.insert("", END, values=(linhas[0],linhas[1],linhas[2],linhas[3],linhas[4]))
        Gredviw()

    def Isaida(self):
        isaida = Toplevel(self.principal, bg='white')
        isaida.geometry('250x184')
        isaida.title('Saida de veiculo')
        isaida.resizable(False, False)
        Label(isaida, text='Codigo saida', bg='white').place(relx=0.30, rely=0.01)
        self.entsaida = Entry(isaida)
        self.entsaida.place(relx=0.20, rely=0.15)
        Button(isaida, text='Ocupacao',command=self.Iocupacao).place(relx=0.30, rely=0.60)
        Button(isaida, text='Dar saida',command=self.Regsaida).place(relx=0.30, rely=0.80)
        self.lbsaida=Label(isaida,text='',bg='white')
        self.lbsaida.place(relx=0.25, rely=0.40)

    def Imovimen(self):
        Imovimentacao = Toplevel(self.principal, bg='white')
        Imovimentacao.geometry('450x250')
        Imovimentacao.title('Movimentacao')
        Imovimentacao.resizable(True, True)
        self.gridmovi = ttk.Treeview(Imovimentacao, columns=('col1', 'col2', 'col3', 'col4','col5','col6'), show='headings')
        self.gridmovi.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.95)
        self.gridmovi.column('#0', width=0, minwidth=0)
        self.gridmovi.column('col1', minwidth=0, width=20)
        self.gridmovi.column('col2', minwidth=0, width=100)
        self.gridmovi.column('col3', minwidth=0, width=100)
        self.gridmovi.column('col4', minwidth=0, width=100)
        self.gridmovi.column('col5', minwidth=0, width=20)
        self.gridmovi.column('col6', minwidth=0, width=100)
        self.gridmovi.heading('#0', text='')
        self.gridmovi.heading('#1', text='ID')
        self.gridmovi.heading('#2', text='ENTRADA')
        self.gridmovi.heading('#3', text='PLACA')
        self.gridmovi.heading('#4', text='COR')
        self.gridmovi.heading('#5', text='T')
        self.gridmovi.heading('#6', text='SAIDA')
        self.gridmovi.pack()

        def Gredviw():
            self.gridmovi.delete(*self.gridmovi.get_children())
            banco = database.Banco()
            resultado=banco.cur.execute(f'''select A.ID,A.DATAINICIO,B.PLACA,B.COR,B.TIPO,a.DATAFINAL from movimentacao A JOIN VEICULO B ON A.VEICULO=B.ID
            ''')

            for linhas in resultado:
                self.gridmovi.insert("", END, values=(linhas[0],linhas[1],linhas[2],linhas[3],linhas[4],linhas[5]))
        Gredviw()

    def LbandButtons(self):
        Button(self.principal, text='Movimentacao', fg='White', bg='#836FFF', command=self.Imovimen).place(
            relx=0.05, rely=0.10)
        Button(self.principal, text='Registrar entrada', fg='white', bg='#836FFF', command=self.Ientrada).place(
            relx=0.42, rely=0.10)
        Button(self.principal, text='Registrar saida', fg='white', bg='#836FFF',command=self.Isaida).place(relx=0.80, rely=0.10)

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
