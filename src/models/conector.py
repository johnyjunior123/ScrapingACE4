import mysql.connector

class Conector:
    
    def __init__(self, config):
        try:
            self.conexao = mysql.connector.connect(**config)
            print('Conexão com Sucesso')
        except mysql.connector.Error as error:
            print(error)
        
    def executarSQL(self, sql):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(sql)
            self.conexao.commit()
            print(cursor.rowcount, '200 - Sucess')
            cursor.close()
        except mysql.connector.Error as error:
            print(error)

    def encerrar(self):
        self.conexao.close()
        print('--- Encerrada com Sucesso - 200 ---')

config = {
    "user" : "johny",
    "password" : "DeF1234*",
    "host" : "127.0.0.1",
    "database" : "noticias"
}





