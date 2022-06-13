from flask import Blueprint, Flask, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from src.models import User

admin = Blueprint('admin', __name__, template_folder='templates',url_prefix='/admin')

is_admin = False

def isAdmin(redirectURL , template):
    if hasattr(current_user, 'is_admin'):
        if(current_user.is_admin is not True):
            flash('You are not authorized to access this page.')
            return redirect(redirectURL)
        else :
            return template
    else :
        flash('You are not authorized to access this page.')
        return redirect(redirectURL)

@admin.route('/')
@login_required
def index():
    return isAdmin(url_for('core.index'), render_template('admin/index.html'))



@admin.route('/users')
@login_required
def users():
    return isAdmin(url_for('core.index'), render_template('admin/users.html'))
