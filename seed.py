import os
import json
from app import app
from backend.models.db import db
from backend.models.avengers import Avenger 

DATA_DIR = 'backend/data'

def populate_avengers(data):
    created = 0
    for item in data:
        habilidades_str = json.dumps(item['habilidades']) #convertimos la lista de habilidades en string para guardarlo en la bd
        avenger = Avenger(
            nombre=item['nombre'],
            alias=item['alias'],
            habilidades=habilidades_str,
            actor=item['actor']
        )
        db.session.add(avenger)
        created += 1
    return created

def populate_all():
    with app.app_context():
        print("Entrando en el contexto de la app...")

        # Opcional: limpiar tabla para evitar duplicados
        Avenger.query.delete()
        db.session.commit()

        filepath = os.path.join(DATA_DIR, 'avengers.json')
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
            print(f"Datos cargados desde avengers.json")

            created = populate_avengers(data['avengers'])
            print(f'{created} Avengers cargados desde avengers.json')

            print("Haciendo commit final a la base de datos...")
            db.session.commit()
        else:
            print(f'Archivo no encontrado: {filepath}')

if __name__ == '__main__':
    populate_all()

