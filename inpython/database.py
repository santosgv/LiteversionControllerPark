import pyodbc

class Banco():
    def __init__(self):
        server = 'DESKTOP-O0728HG\SQLEXPRESS'
        database = 'ESTACIONAMENTO'
        string_conexao = 'Driver={SQL Server Native CLient 11.0};Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'
        c = pyodbc.connect(string_conexao)
        self.cur = c.cursor()

    def inserevaga(self,VAGA,ENDERECO):
        self.cur.execute(f'''insert into PRACAS values('{VAGA}',{ENDERECO})'''),self.cur.commit(),print("vaga inserida"),self.c.close()


    def insereveiculo(self,PLACA,COR,TIPO):
        self.cur.execute(f'''
        insert into veiculo values('{PLACA}','{COR}',{TIPO})'''),self.cur.commit(),print("Veiculo inserido"),self.c.close()


    def show_vagas(self):
        vagas=self.cur.execute(f'''select * from PRACAS'''),self.c.close()
        for i in vagas:
            return i

    def show_veiculos(self):
        veiculos=self.cur.execute(f'''select * from veiculo'''),self.c.close()
        for i in veiculos:
            return i
