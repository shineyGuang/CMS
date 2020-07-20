from flask import Flask

from apps.apis import api_init
from exts import db_init
from settings import envs
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(envs.get('develop'))
    db_init(app)
    api_init(app)
    CORS(app)
    return app
