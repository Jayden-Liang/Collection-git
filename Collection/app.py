import os
from flask import Flask, Blueprint
from flask_migrate import Migrate

from routes.user.route_user import main as route_user
from routes.blog.route_blog import main as route_blog
from routes.todo.route_todo import todo_main
from extensions import csrf, moment, migrate, login_manager, bootstrap
from models import db, User



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                                            'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                                        'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_pyfile('settings.py', silent=True)
    app.secret_key = b'fdhakhfkjaghj873o8qyhhg'

    app.register_blueprint(route_blog)
    app.register_blueprint(route_user)
    app.register_blueprint(todo_main)
    extension(app)
    migrate = Migrate(app, db)
    return app


def extension(app):
    csrf.init_app(app)
    moment.init_app(app)
    migrate.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    return None


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


app = create_app()


if __name__=='__main__':
    app.run(debug=True, port=5000)


















# db.init_app(app)
# db.app= app
# migrate = Migrate(app, db)
















