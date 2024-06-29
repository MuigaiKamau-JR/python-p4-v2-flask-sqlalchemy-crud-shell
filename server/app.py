from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
