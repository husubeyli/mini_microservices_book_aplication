from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from book_service.app import app
from flask_marshmallow import Marshmallow


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://db_user:bTmNECmEZOrdUcX4DQkAGevLtRakY@127.0.0.1:5432/db_name'
app.config['SECRET_KEY'] = 'this is private'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config["APPLICATION_ROOT"] = "api/v1.0/post/"


db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
ma = Marshmallow(app)