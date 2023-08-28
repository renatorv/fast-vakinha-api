from fastapi import Body, FastAPI
import uvicorn
import mysql.connector

from models.usuario import Usuario

from App.Usuario import Controller as usuario

app = FastAPI()


config = {
        'user': 'root',
        'password': '159753',
        'host': '127.0.0.1',
        'database': 'vakinha_burger',
        'autocommit': True
    }

# @app.post('/login')
# async def login(user: Usuario = Body()):
    
#     try:
#         cnx = mysql.connector.connect(**config)
#         cur = cnx.cursor()
#         sqlSelect = """SELECT * FROM usuario where email = %s and senha = %s"""
#         parametros = [user.email, user.password]
#         cur.execute(sqlSelect, parametros)
#         data = cur.fetchall()
#         payload = []
#         content = {}
        
#         if(len(data) > 0):
#             for result in data:
#                 content = {'id': result[0], 'nome': result[1], 'email': result[2]}
#                 payload.append(content)
#                 content = {}
#             return payload[0]
#         else:
#             return {'message': 'Login/senha invalido(s)'}
#     except Exception:
#         return {'message': 'Erro ao realizar login.'}
#     finally:
#         if(cnx.is_connected):
#             cnx.close()
#             cur.close()
#             print("Conexao fechada.")

@app.post('/register')
async def register(user: Usuario = Body()):
    try:
        cnx = mysql.connector.connect(**config)
        cur = cnx.cursor()
        sqlSelect = """SELECT * FROM usuario where email = %s"""
        parametros = [user.email]
        cur.execute(sqlSelect, parametros)
        data = cur.fetchall()
        
        # Verificar se e-mail já cadastrado 
        if(len(data) > 0):
            return {'message': 'E-mail já cadastrado'}
        
        # TODO:
        # Gravar senha criptografada.
        sqlInsert = f"""INSERT INTO usuario (`nome`, `email`, `senha`) VALUES (%s, %s, %s);"""
        
        parametrosInsert = [user.name, user.email, user.password]
        
        cur.execute(sqlInsert, parametrosInsert)
        
        ret = {}
        
        if(cur.rowcount > 0):
            idInsert = cur.lastrowid
            user.id = str(idInsert)
            ret = user
            
        return ret
    except Exception:
        return {'message': 'Erro ao cadastrar usuario.'}
    finally:
        if(cnx.is_connected):
            cnx.close()
            cur.close()
            print("Conexao fechada.")
    
app.include_router(usuario.router)

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=5566)