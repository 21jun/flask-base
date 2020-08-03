from .post import posts_bp
from .index import index_bp


def init_app(app):
    print("INIT: ROUTES")
    app.register_blueprint(index_bp)
    app.register_blueprint(posts_bp)
