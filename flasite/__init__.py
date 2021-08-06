import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bekttykzfmadzf:1c448c728cd8fd296ef5241ac92785e81e2890c81671665243237f67b7d09d75@ec2-3-226-59-11.compute-1.amazonaws.com:5432/d4l812t330k3bp'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = os.getenv('manas.satpute99@gmail.com')
    app.config['MAIL_PASSWORD'] = os.getenv('Manas@14september')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flasite.users.routes import users
    from flasite.posts.routes import posts
    from flasite.main.routes import main
    from flasite.errors.handler import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app