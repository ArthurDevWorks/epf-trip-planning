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
        self.app.route('/trip', method='GET', callback=self.logout)

    def login(self):
        if request.method == 'GET':
            return self.render('login', erro=None)
        email = request.forms.get('email')
        password = request.forms.get('password')
        usuario = self.user_service.authenticate(email, password)
        if usuario:
            request.session['usuario_id'] = usuario['id']
            return redirect('/trip')
        return self.render('login', erro='Usuário ou senha inválidos')

    def register(self):
        if request.method == 'GET':
            return self.render('register', erro=None)
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        password = request.forms.get('password')
        sucesso, erro = self.user_service.create_account(name, email, birthdate, password)
        if sucesso:
            return redirect('/login')
        return self.render('register', erro=erro)

    def logout(self):
        request.session.pop('usuario_id', None)
        return redirect('/login')

    def trip(self):
        usuario_id = request.session.get('usuario_id')
        if not usuario_id:
            return redirect('/login')
        return self.render('trip')

user_routes = Bottle()
user_controller = UserController(user_routes)