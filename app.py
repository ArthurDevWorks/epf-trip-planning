from bottle import Bottle, run
from beaker.middleware import SessionMiddleware
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        self.session_opts = {
            'session.type': 'file',
            'session.data_dir': self.config.DATA_PATH + '/sessions',
            'session.cookie_expires': 3600,  # 1 hora
            'session.auto': True,
        }

    def setup_routes(self):
        from controllers import init_controllers
        init_controllers(self.bottle)

    def run(self):
        self.setup_routes()
        app_with_session = SessionMiddleware(self.bottle, self.session_opts)
        run(
            app=app_with_session,
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

def create_app():
    return App()
