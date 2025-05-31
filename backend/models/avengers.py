import uuid
from backend.models.db import db


class Avenger(db.Model):
    __tablename__ = "avengers"

    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    alias = db.Column(db.String(100), nullable=False)
    habilidades = db.Column(db.Text, nullable=False)
    actor = db.Column(db.String(100), nullable=False)

    def __init__(self, nombre, alias, habilidades, actor, foto_nombre=None):
        self.nombre = nombre
        self.alias = alias
        self.habilidades = habilidades
        self.actor = actor

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "alias": self.alias,
            "habilidades": self.habilidades,
            "actor": self.actor,
        }
