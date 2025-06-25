from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.user_service import UserService
from flask import Blueprint, request, redirect, url_for, session
from services.auth_service import AuthService

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = AuthService.authenticate(username, password)
    if user:
        session['user_id'] = user.id
        return redirect(url_for('home'))
    return "Falha no login, tente novamente.", 401

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
        password = request.forms.get('password')
        usuario = self.user_service.autenticar(email, password)
        if usuario:
            request.session['usuario_id'] = usuario['id']
            return redirect('/viagem')
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

user_routes = Bottle()
user_controller = UserController(user_routes)