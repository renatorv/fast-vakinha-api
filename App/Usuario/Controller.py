from fastapi import APIRouter, Body, Depends

from fastapi import Body, FastAPI
import uvicorn
import mysql.connector

from models.usuario import Usuario

router = APIRouter(
    tags=["usuario"],
    responses={404: {"description": "Not found"}},
)

config = {
        'user': 'root',
        'password': '159753',
        'host': '127.0.0.1',
        'database': 'vakinha_burger',
        'autocommit': True
    }

@router.post('/login')
async def login(user: Usuario = Body()):
    
    try:
        cnx = mysql.connector.connect(**config)
        cur = cnx.cursor()
        sqlSelect = """SELECT * FROM usuario where email = %s and senha = %s"""
        parametros = [user.email, user.password]
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
            print("Conexao fechada.")