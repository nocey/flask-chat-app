from flask import Blueprint, Flask, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from src import db
from src.models import User, UserFriends, UserMessages

chat = Blueprint('chat', __name__, template_folder='templates',url_prefix='/chat')

@chat.route('/<id>/<room>')
@login_required
def index(id , room): 
    messagesAll = UserMessages.query.filter_by(user_id=current_user.id , friends_id=id ).all()
    messagesFriends = UserMessages.query.filter_by(friends_id=current_user.id , user_id=id ).all()
    messages = messagesAll + messagesFriends
    def custom_sort(message):
        return message.created_at
    messages.sort(key=custom_sort)
    return render_template('chat/index.html' , friend_id=id , messages=messages , room = room)



@chat.route('/usersadd/<id>')
@login_required
def friendAdd(id):
    freiend = UserFriends(user_id = id, room_id = current_user.id)
    db.session.add(freiend)
    db.session.commit()
    return redirect(url_for('chat.index', id=id , room = current_user.id))

@chat.route('/users')
@login_required
def users():
    user = User.query.outerjoin(UserFriends).all()
    return render_template('chat/users.html' , users=user)
