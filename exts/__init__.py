from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()


def db_init(app, **kwargs):
    db.init_app(app)
    migrate.init_app(app, db)
