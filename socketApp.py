import os
from flask_socketio import SocketIO , emit , send ,join_room , leave_room
from src import app ,db
from flask_migrate import Migrate

from src.models import UserMessages

migrate = Migrate(app, db)
socketio = SocketIO(app , port=2043)

@socketio.on('connect_server')
def connect(auth):
    # join_room(auth['room'])
    emit('server_message', {'message': 'Connected to server'})

@socketio.on('client_message')
def handle_message(data):
    emit('server_message',data, broadcast=True )#to=data['room']
    message = UserMessages(data.get('user_id'), data.get('friend_id'), data.get('message'))
    db.session.add(message)
    db.session.commit()