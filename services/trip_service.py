import pymysql
from models.trip import Trip

class TripService:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='trip-planning',
            cursorclass=pymysql.cursors.DictCursor
        )

    def save(self, user_id, dt_begin, dt_end, local):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO trips (user_id, dt_begin, dt_end, local) VALUES (%s, %s, %s, %s)",
                    (user_id, dt_begin, dt_end, local)
                )
                self.connection.commit()
                return True, None
        except Exception as e:
            return False, str(e)
        finally:
           self.connection.close()
