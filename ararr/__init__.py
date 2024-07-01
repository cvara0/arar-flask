#aca van configuraciones
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    #configuracion del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///arar.db'
    )
    
    db.init_app(app)

    #registrar bp
    from . import arar
    app.register_blueprint(arar.bp)
    
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def inicio():
       return render_template('inicio.html')
    
    with app.app_context():
        db.create_all()
    
    return app