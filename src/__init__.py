from flask_migrate import Migrate
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_admin import Admin 
# from flask_admin.contrib.sqla import ModelView
# from src.models import User

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:root@localhost:8889/chat-app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data2.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
db = SQLAlchemy(app)

# admin = Admin(app)
# admin.add_view(ModelView(User, db.session))

# login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'

from src.error.handlers import error_pages
from src.core.views import core
from src.user.views import user
from src.admin.views import admin
from src.chat.views import chat
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(chat)