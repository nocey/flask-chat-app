from flask import render_template,Blueprint, request, redirect, url_for, flash, abort

core = Blueprint('core', __name__, template_folder='templates' ,url_prefix='/')

@core.route('/')
def index():
    
    return render_template('index/index.html')