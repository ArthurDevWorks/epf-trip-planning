from bottle import Bottle, request, redirect
from .base_controller import BaseController
from controllers.user_controller import user_controller
from services.trip_service import TripService

class TripController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.trip_service = TripService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/trip-create', method=['GET', 'POST'], callback=self.create_trip)
        self.app.route('/trip-list', method=['GET', 'POST'], callback=self.list_trip)
        self.app.route('/user/edit', method=['GET', 'POST'], callback=user_controller.edit)
    
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