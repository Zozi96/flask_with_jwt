from flask import request
from flask.json import jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended.utils import get_jwt_identity
from . import web


@web.route('/', methods=["GET"])
@jwt_required()
def index():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@web.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    if username != 'batman' or password != 'batigalletas':
        return jsonify(
            {
                'message': 'Usuario o contrasena mal ingresado'
            }
        )
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@web.route('/partial', methods=['GET'])
@jwt_required(optional=True)
def partial():
    current_identity = get_jwt_identity()
    if current_identity:
        return jsonify(logeado_como=current_identity)
    else:
        return jsonify(logeado_como='Usuario anonimo')
