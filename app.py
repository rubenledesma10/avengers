import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.avenger_routes import avenger_bp
from models.avenger_model import db

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/shield_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

app.register_blueprint(avenger_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
