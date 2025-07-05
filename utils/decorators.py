from bottle import request, redirect

def login_required(callback):
    def wrapper(*args, **kwargs):
        session = request.environ.get('beaker.session')
        if not session.get('user_id'):
            return redirect('/login')
        return callback(*args, **kwargs)
    return wrapper