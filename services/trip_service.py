import pymysql
from models.trip import Trip
from controllers.base_controller import connect_db

class TripService:
    def save(self, user_id, dt_begin, dt_end, local):
        try:
            connection = connect_db()
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO trips (user_id, dt_begin, dt_end, local) VALUES (%s, %s, %s, %s)",
                    (user_id, dt_begin, dt_end, local)
                )
                connection.commit()
                return True, None
        except Exception as e:
            return False, str(e)
        finally:
            connection.close()
