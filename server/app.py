from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# create a Flask application instance 
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create the Flask SQLAlchemy extension
db = SQLAlchemy(app, metadata=MetaData())

# import the Pet model
from models import Pet

# create all database tables
with app.app_context():
    db.create_all()

# routes for CRUD operations

@app.route('/pets', methods=['GET'])
def get_all_pets():
    pets = Pet.query.all()
    return jsonify([pet.serialize() for pet in pets])

@app.route('/pets/<int:id>', methods=['GET'])
def get_pet(id):
    pet = Pet.query.get(id)
    if pet:
        return jsonify(pet.serialize())
    else:
        return jsonify({'message': 'Pet not found'}), 404

@app.route('/pets', methods=['POST'])
def create_pet():
    data = request.json
    name = data.get('name')
    species = data.get('species')

    if not name or not species:
        return jsonify({'message': 'Name and species are required'}), 400

    new_pet = Pet(name=name, species=species)
    db.session.add(new_pet)
    db.session.commit()

    return jsonify(new_pet.serialize()), 201

@app.route('/pets/<int:id>', methods=['PUT'])
def update_pet(id):
    pet = Pet.query.get(id)
    if not pet:
        return jsonify({'message': 'Pet not found'}), 404

    data = request.json
    name = data.get('name')
    species = data.get('species')

    if name:
        pet.name = name
    if species:
        pet.species = species

    db.session.commit()

    return jsonify(pet.serialize())

@app.route('/pets/<int:id>', methods=['DELETE'])
def delete_pet(id):
    pet = Pet.query.get(id)
    if not pet:
        return jsonify({'message': 'Pet not found'}), 404

    db.session.delete(pet)
    db.session.commit()

    return jsonify({'message': 'Pet deleted'})

if __name__ == '__main__':
    app.run(port=5555, debug=True)





# # server/app.py

# from flask import Flask
# from flask_migrate import Migrate

# from models import db

# # create a Flask application instance 
# app = Flask(__name__)

# # configure the database connection to the local file app.db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# # configure flag to disable modification tracking and use less memory
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # create a Migrate object to manage schema modifications
# migrate = Migrate(app, db)

# # initialize the Flask application to use the database
# db.init_app(app)


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)
