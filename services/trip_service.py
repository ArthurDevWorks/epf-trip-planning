import pymysql
import requests
from models.trip import Trip
from datetime import datetime

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

    def getTripsByUserId(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM trips WHERE user_id = %s", (user_id,))
                results = cursor.fetchall()

                # Formatar datas
                for trip in results:
                    trip['dt_begin'] = datetime.strptime(str(trip['dt_begin']), "%Y-%m-%d").strftime("%d/%m/%Y")
                    trip['dt_end'] = datetime.strptime(str(trip['dt_end']), "%Y-%m-%d").strftime("%d/%m/%Y")

                return results
        except Exception as e:
            print(f"Erro ao buscar viagens: {e}")
            return []
