from email.policy import default
from src import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model , UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, nullable=False,default=db.func.now())
    friends = db.relationship('UserFriends', backref='user', lazy=True)
    messages = db.relationship('UserMessages', backref='user', lazy=True)
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f" User {self.username}"

class UserFriends(db.Model):
    __tablename__ = 'room_friends'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    room_id = db.Column(db.Integer, nullable=False)
    
    def __init__(self, user_id, room_id):
        self.user_id = user_id
        self.room_id = room_id

    def __repr__(self):
        return f"{self.room_id}"

class UserMessages(db.Model):
    __tablename__ = 'user_messages'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    friends_id = db.Column(db.Integer, db.ForeignKey('room_friends.id'), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=db.func.now())

    def __init__(self, user_id, friend_id, message):
        self.user_id = user_id
        self.friends_id = friend_id
        self.message = message

    def __repr__(self):
        return f" message {self.user_id} {self.friend_id}"



