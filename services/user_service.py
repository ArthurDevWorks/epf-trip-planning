import pymysql.cursors
from hashlib import sha256

class UserService:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='trip-planning',
            cursorclass=pymysql.cursors.DictCursor
        )

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
            self.connection.rollback()
            return False, str(e)

    def authenticate(self, email, password):
        hash_password = sha256(password.encode()).hexdigest()
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, hash_password))
            return cursor.fetchone()