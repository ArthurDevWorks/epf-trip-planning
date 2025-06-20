from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.user_service import UserService

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/register', method=['GET', 'POST'], callback=self.register)
        self.app.route('/logout', method='GET', callback=self.logout)

    def login(self):
        if request.method == 'GET':
            return self.render('login', erro=None)
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        usuario = self.user_service.autenticar(email, senha)
        if usuario:
            request.session['usuario_id'] = usuario['id']
            return redirect('/viagem')
        return self.render('login', erro='Usuário ou senha inválidos')

    def register(self):
        if request.method == 'GET':
            return self.render('register', erro=None)
        nome = request.forms.get('nome')
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        sucesso, erro = self.user_service.criar_conta(nome, email, senha)
        if sucesso:
            return redirect('/login')
        return self.render('register', erro=erro)

    def logout(self):
        request.session.pop('usuario_id', None)
        return redirect('/login')

user_routes = Bottle()
user_controller = UserController(user_routes)