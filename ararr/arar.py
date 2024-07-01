from flask import Blueprint, render_template

bp = Blueprint('arar', __name__, url_prefix='/arar') #se registran las vistas,y con el url prefix se establece el url inicial


@bp.route('/arte')
def arte():
    return render_template('arte.html')

@bp.route('/artesania')
def artesania():
    return 'este es artesania'