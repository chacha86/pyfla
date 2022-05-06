from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index() :
    return redirect(url_for('article._list'))

@bp.route('/hello')
def hello() :
    print('hello')
    return 'hello'
