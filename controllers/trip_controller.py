from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.trip_service import TripService

class TripController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.trip_service = TripService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/trip', method=['GET', 'POST'], callback=self.create_trip)
    
    def create_trip(self):
        session = request.environ.get('beaker.session')
        user_id = session.get('user_id')
        if not user_id:
            return redirect('/login')
        
        if request.method == 'GET':
            return self.render('trip', erro=None)
        
        dt_begin = request.forms.get('dt_begin')
        dt_end = request.forms.get('dt_end')
        local = request.forms.get('local')
        
        sucesso, erro = self.trip_service.save(user_id, dt_begin, dt_end, local)
        if sucesso:
            return redirect('/trip')
        return self.render('trip', erro=erro)

trip_routes = Bottle()
trip_controller = TripController(trip_routes)