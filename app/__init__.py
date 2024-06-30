from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, ProductionConfig
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_mail import Mail

if os.environ.get('FLASK_ENV') == 'production':
    config_class = ProductionConfig
else:
    config_class = DevelopmentConfig

app = Flask(__name__)
app.config.from_object(config_class)
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail = Mail(app)


from app import routes, models  # noqa
