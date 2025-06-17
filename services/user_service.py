import pymysql.cursors
from hashlib import sha256
from bottle import request
from models.user import UserModel, User

class UserService:

    #Conexao com banco de dados
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='trip-planning',
            cursorclass=pymysql.cursors.DictCursor
        )

    #Funcao de autenticacao
    def authenticate(self, email, senha):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE email=%s AND senha=%s", (email, sha256(senha.encode()).hexdigest()))
            return cursor.fetchone()
        
    #Criar conta
    def create_acoount(self, nome, email, senha):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT id FROM usuarios WHERE email=%s", (email,))
                if cursor.fetchone():
                    return False, 'Email já cadastrado'
                cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
                               (nome, email, sha256(senha.encode()).hexdigest()))
                self.connection.commit()
            return True, None
        except Exception as e:
            return False, str(e)

