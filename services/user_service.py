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
    
    #Funcao que cria a conta do usuario
    def create_account(self, name, email, birthdate, password):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
                if cursor.fetchone():
                    return False, 'Email já cadastrado'

                hash_password = sha256(password.encode()).hexdigest()
                cursor.execute(
                    "INSERT INTO users (name, email, birthdate, password) VALUES (%s, %s, %s, %s)",
                    (name, email, birthdate, hash_password)
                )
                self.connection.commit()
                return True, None
        except Exception as e:
            return False, str(e)

    #Funcao de autenticacao
    def authenticate(self, email, senha):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email=%s AND senha=%s", (email, sha256(senha.encode()).hexdigest()))
            return cursor.fetchone()

