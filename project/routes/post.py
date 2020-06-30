from flask import Blueprint

posts_bp = Blueprint('post', __name__, url_prefix='/post')


@posts_bp.route('/')
def index():
    return "post index"


@posts_bp.route('/1')
def first_post():
    return "First Post"
