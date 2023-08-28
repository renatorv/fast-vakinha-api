
import mysql.connector

config = {
        'user': 'root',
        'password': '159753',
        'host': '127.0.0.1',
        'database': 'vakinha_burger',
        'autocommit': True
    }

class Conexao:
    
    
    def __init__(self) -> None:
        self.config = {
        'user': 'root',
        'password': '159753',
        'host': '127.0.0.1',
        'database': 'vakinha_burger',
        'autocommit': True
    }
        # 
    def connectar(self):
        try:
            self.db = mysql.connector.connect(**self.config)
            self.cursor = self.db.cursor()
        except Exception:
            self.db = None
            raise
    
    def desconectar(self):
        try:
            self.cursor.close()
            self.db.close()
            self.db = None
        except Exception:
            pass
        
    def select(self, sql):
        self.connectar()
        self.execute(sql)
        data = self.cursor.fetchall()
        
        payload = []
        content = {}
        
        for result in data:
            content = {'id': result[0], 'nome': result[1], 'email': result[2], 'senha': result[3]}
            payload.append(content)
            content = {}
        
        return payload
    
    def sqlSelectLogin(sqlSelect, parametros):
        try:
            cnx = mysql.connector.connect(**config)
            cur = cnx.cursor()
            cur.execute(sqlSelect, parametros)
            data = cur.fetchall()
            payload = []
            content = {}
            
            if(len(data) > 0):
                for result in data:
                    content = {'id': result[0], 'nome': result[1], 'email': result[2]}
                    payload.append(content)
                    content = {}
                return payload[0]
            else:
                return {'message': 'Login/senha invalido(s)'}
        except Exception:
            return {'message': 'Erro ao realizar login.'}
        finally:
            if(cnx.is_connected):
                cnx.close()
                cur.close()
                print("MySQL connection is closed")
                
    def sqlInsertLogin(sqlInsert, parametrosInsert):
        try:
            cnx = mysql.connector.connect(**config)
            cur = cnx.cursor()
            cur.execute(sqlInsert, parametrosInsert)
            
            if(cur.rowcount > 0):
                return cur.lastrowid
            else:
                return 0
        except Exception:
            return {'message': 'Erro ao realizar login.'}
        finally:
            if(cnx.is_connected):
                cnx.close()
                cur.close()
                print("MySQL connection is closed")
        
    def sqlSelectRegister(sqlSelect, parametros):
        try:
            cnx = mysql.connector.connect(**config)
            cur = cnx.cursor()
            
            cur.execute(sqlSelect, parametros)
            data = cur.fetchall()
        
            return data
            
        except Exception:
            return {'message': 'Erro ao cadastrar usuario.'}
        finally:
            if(cnx.is_connected):
                cnx.close()
                cur.close()
                print("MySQL connection is closed")