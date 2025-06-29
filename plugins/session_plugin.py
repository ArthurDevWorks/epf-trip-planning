from bottle import request

class SessionPlugin:
    name = 'session'
    api = 2

    def __init__(self, options):
        self.options = options

    def apply(self, callback, route):
        def wrapper(*args, **kwargs):
            # Adiciona o atributo session ao request
            request.session = request.environ.get('beaker.session')
            return callback(*args, **kwargs)
        return wrapper