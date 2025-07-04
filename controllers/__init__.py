from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.trip_controller import trip_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(trip_routes)
