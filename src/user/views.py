from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from sqlalchemy import null
from src.models import User
from src import db
from src.user.forms import LoginForm, RegistrationForms

user = Blueprint('user', __name__, template_folder='templates',url_prefix='/user')

@user.route('/login' , methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('You have been logged in.', 'success')

            next_page = request.args.get('next')
            if not next_page or next_page[0] != '/':
                next_page = url_for('core.index')

            return redirect(next_page)
    return render_template('user/login.html' , form=form)

@user.route('/logout' , methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))
    
@user.route('/profile/<username>' , methods=['GET','POST'])
@login_required
def profile(username):
    if username is not null:
        user = User.query.filter_by(username=username).first()
        if user is not None:
            return render_template('user/profile.html', user=user)
    return redirect(url_for('user.login'))


@user.route('/register' , methods=['GET','POST'])
def register():
    form = RegistrationForms()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user')
        return redirect(url_for('user.login'))
    
    return render_template('user/register.html', form=form)
