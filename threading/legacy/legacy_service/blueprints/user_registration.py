"""User registration blueprints"""
from flask import Blueprint, request, make_response


def build_user_registration_blueprints(user_controller, user_schema, user_class):
    """Build blueprints for this application

    :param UserController user_controller: the controller to be used by this
    router
    """
    user_registration_routes = Blueprint('user_registration', __name__)

    def add_user():
        validation_result = user_schema.validate(request.json)
        if user_schema.validate(request.json).keys():
            # Há erros de validação
            return make_response(validation_result, 400)
        user = user_class(**request.json)
        result = user_controller.create_user(user)
        return make_response({'result': result, 'message': 'ok'}, 201)

    def get_user(userid):
        result = user_controller.retrieve_user(userid)
        if result:
            return make_response({'result': user_schema.dump(result), 'message': 'ok'}, 201)
        return make_response({'message': 'not-found'}, 404)

    user_registration_routes.add_url_rule(
        '/registration/<userid>', 'get-user', get_user, methods=['GET'])
    user_registration_routes.add_url_rule(
        '/registration', 'new-user', add_user, methods=['POST'])
    return user_registration_routes
