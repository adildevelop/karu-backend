import os
from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = '{}://{}:{}@{}/{}'.format(
        os.getenv('DB_TYPE'),
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOST'),
        os.getenv('DB_NAME')
    )

    db.init_app(app)

    return app