
from flask import Flask   #importamos flask
from backend.config.config import DATABASE_CONNECTION_URI #importamos la variable de conexion a la bd
from backend.models.db import db 
from backend.routes.routes_avengers import avenger_bp
from backend.models.avengers import Avenger



app = Flask(__name__)
app.register_blueprint(avenger_bp)


app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) #inicializamos SQLAlchemy con la app de Flask

with app.app_context():
    from backend.models.avengers import Avenger

    db.create_all() #crea las tablas si no existen

    
if __name__ == '__main__': #ejecutamos la app en modo debug para ver errores fácilmente durante el desarrollo.
    print("Bienvenido a nuestra app")
    app.run(debug=True)
