import pyodbc

class Banco():
    def __init__(self):
        server = 'DESKTOP-O0728HG\SQLEXPRESS'
        database = 'ESTACIONAMENTO'
        string_conexao = 'Driver={SQL Server Native CLient 11.0};Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'
        c = pyodbc.connect(string_conexao)
        self.cur = c.cursor()

    def inserevaga(self,VAGA,ENDERECO):
        self.cur.execute(f'''insert into PRACAS values('{VAGA}',{ENDERECO})'''),self.cur.commit(),print("Vaga inserida")
        return True

    def insereveiculo(self,PLACA,COR,TIPO):
        self.cur.execute(f'''
        insert into veiculo values('{PLACA}','{COR}',{TIPO})'''),self.cur.commit(),print("Veiculo inserido")
        return True

    def Regientrada(self,VEICULO,PRACA):
        self.cur.execute(f'''insert into movimentacao (DATAINICIO,VEICULO,OCUPADO,P) values(getdate(),{VEICULO},'S',{PRACA})'''),self.cur.commit(),print('Registrado')
        return  True

    def Regisaida(self,ID):
        self.cur.execute(f'''UPDATE movimentacao set DATAFINAL=GETDATE(),OCUPADO='N' where ID={ID}'''),self.cur.commit(),print('SAIDA REGISTRADA')
        return  True

    def show_vagas(self):
        VAGAS=self.cur.execute(f'''select * from PRACAS''')
        for i in VAGAS.fetchall():
            print(i)
            return i



