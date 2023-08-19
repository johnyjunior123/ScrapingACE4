import psycopg2
class Conector:
    
    def __init__(self, banco):
        try:
            self.conexao = psycopg2.connect(
            user="postgres",
            password="demon123",
            host="127.0.0.1",
            database=banco)
            print('Conexão com Sucesso')
        except psycopg2.Error as error:
            print(error)
        
    def executarSQL(self, sql):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(sql)
            self.conexao.commit()
            print(cursor.rowcount, '200 - Sucess')
            cursor.close()
        except psycopg2.Error as error:
            print(error)

    def encerrar(self):
        self.conexao.close()
        print('--- Encerrada com Sucesso - 200 ---')