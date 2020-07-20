from flask_restful import Api

from apps.apis.users.login import LoginApi

api = Api()


def api_init(app, **kwargs):
    api.init_app(app)


api.add_resource(LoginApi, '/api/private/v1/login')
