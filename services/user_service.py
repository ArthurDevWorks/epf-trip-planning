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
    
    def getDataUser(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
                results = cursor.fetchone()

                return results
        except Exception as e:
            print(f"Erro ao buscar dados do usuario: {e}")
            return []
    
    def update_user(self, user_id, name, email, birthdate, password):
        try:
            with self.connection.cursor() as cursor:
                if password:
                    hash_password = sha256(password.encode()).hexdigest()
                    cursor.execute("""
                        UPDATE users SET name=%s, email=%s, birthdate=%s, password=%s WHERE id=%s
                    """, (name, email, birthdate, hash_password, user_id))
                else:
                    cursor.execute("""
                        UPDATE users SET name=%s, email=%s, birthdate=%s WHERE id=%s
                    """, (name, email, birthdate, user_id))
            self.connection.commit()
            return True, None
        except Exception as e:
            self.connection.rollback()
            return False, str(e)
