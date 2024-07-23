import os
from . import db
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'catalog.db'),
    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    return app
