import json
import requests
from datetime import datetime, timedelta
from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.trip_service import TripService
from controllers.user_controller import user_controller

class TripController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.trip_service = TripService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/trip-create', method=['GET', 'POST'], callback=self.create_trip)
        self.app.route('/trip-list', method=['GET', 'POST'], callback=self.list_trip)
        self.app.route('/user/edit', method=['GET', 'POST'], callback=user_controller.edit)
        self.app.route('/api/weather', method=['GET','POST'], callback=self.weather_api)

    def weather_api(self):

        data = request.json
        local = data.get('local')
        dt_begin = data.get('dt_begin')
        dt_end = data.get('dt_end')

        try:
            # Etapa 1: Geocodificação
            geo_res = requests.get(
                f"http://api.openweathermap.org/geo/1.0/direct?q={local}&limit=1&appid=d9c3d08371036ecd889477f5015e40a4"
            )

            geo = geo_res.json()
            if not geo or len(geo) == 0:
                return json.dumps({"error": "Destino não encontrado na API de geolocalização."})

            lat, lon = geo[0]['lat'], geo[0]['lon']

            # Etapa 2: Previsão do tempo
            weather_res = requests.get(
                f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&lang=pt_br&appid=d9c3d08371036ecd889477f5015e40a4"
            )

            weather = weather_res.json()
            if 'list' not in weather:
                return json.dumps({"error": "Não foi possível obter a previsão do tempo."})

            # Etapa 3: Filtrar por datas
            start_date = datetime.strptime(dt_begin, "%Y-%m-%d").date()
            end_date = datetime.strptime(dt_end, "%Y-%m-%d").date()

            dias = []
            for item in weather["list"]:
                data_prev = datetime.fromtimestamp(item["dt"]).date()  # Converte o timestamp para data

                # Verificando se a data prevista está dentro do intervalo
                if start_date <= data_prev <= end_date:
                    dias.append({
                        "date": datetime.fromtimestamp(item["dt"]).strftime("%d/%m/%Y %H:%M"),  # Formato adequado
                        "temp_min": item["main"]["temp_min"],  # Temperatura mínima
                        "temp_max": item["main"]["temp_max"],  # Temperatura máxima
                        "description": item["weather"][0]["description"],
                        "icon": item["weather"][0]["icon"]
                    })

            if not dias:
                return json.dumps({"error": "Ainda não há previsão para o período selecionado, tente com outras datas."})

            return json.dumps({"forecast": dias})

        except Exception as e:
            return json.dumps({"error": f"Erro ao consultar clima: {str(e)}"})
    
    def create_trip(self):
        session = request.environ.get('beaker.session')
        user_id = session.get('user_id')
        if not user_id:
            return redirect('/login')
        
        if request.method == 'GET':
            return self.render('trip-create', erro=None)
        
        dt_begin = request.forms.get('dt_begin')
        dt_end = request.forms.get('dt_end')
        local = request.forms.get('local')
        
        sucesso, erro = self.trip_service.save(user_id, dt_begin, dt_end, local)
        if sucesso:
            return redirect('/trip')
        return self.render('trip', erro=erro)
    
    def list_trip(self):
        session = request.environ.get('beaker.session')
        user_id = session.get('user_id')
        if not user_id:
            return redirect('/login')
        
        trips = self.trip_service.getTripsByUserId(user_id)
            
        return self.render('trip-list', trips=trips)

trip_routes = Bottle()
trip_controller = TripController(trip_routes)