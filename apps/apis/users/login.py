from flask import request
from flask_restful import Resource, fields, marshal
from apps.models.user_models import User
from apps.utils.jwt import Jwt
from settings import Config

user_info = {
    "id": fields.Integer,
    "rid": fields.Integer,
    "username": fields.String,
    "mobile": fields.String,
    "email": fields.String,
}


class LoginApi(Resource):
    @staticmethod
    def post():
        data = request.json
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            print(user)
            token = Jwt.encode({"username": str(user)}, Config.SIGN)
            ret = {
                "data": marshal(user, user_info),
                "meta": {
                    "msg": "登录成功",
                    "status": 200,
                    "token": token.decode()
                }
            }
            return ret
        else:
            ret = {
                "data": None,
                "meta": {
                    "msg": "登录失败",
                    "status": 422
                }
            }
            return ret
