from bottle import Bottle
from config import Config

from flask import Flask
from controllers.user_controller import user_bp

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # TROCAR CHAVE!!!!!!!!!
app.register_blueprint(user_bp)

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()


    def setup_routes(self):
        from controllers import init_controllers

        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)


    def run(self):
        self.setup_routes()
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()
