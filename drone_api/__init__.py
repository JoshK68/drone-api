from flask import Flask

# TODO: Import Config Object for Flask Project
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import for Login Manager
from flask_login import UserMixin

# Import for Flask Login
from flask_login import LoginManager

# Import for AuthLib integrations
from authlib.integrations.flask_client import OAuth



app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app) #review what's going on here and next line
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'signin' #Specify what page to load for Non-Authed users

oauth = OAuth(app)

from drone_api import routes, models