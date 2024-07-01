from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register')
def register():
    return 'registrar usuario'

@bp.route('/login')
def login():
    return 'iniciar sesion'