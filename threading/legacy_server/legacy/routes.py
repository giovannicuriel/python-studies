from flask import Blueprint, request, make_response
from legacy.models.user import userSchema, User

def build_routes(user_controller):
  """
  Constrói os roteadores utilizados nesta aplicação

  :param UserController user_controller: o controlador de usuários a ser
  utilizado nas rotas
  """
  legacy_routes = Blueprint('user_registration', __name__)
  def add_user():
    validation_result = userSchema.validate(request.json)
    if userSchema.validate(request.json).keys(): 
      # Há erros de validação
      return make_response(validation_result, 400)
    user = User(**request.json)
    result = user_controller.process_user_creation(user)
    return make_response({'userid': result, 'message': 'ok'}, 201)

  def get_user(userid):
    result = user_controller.process_user_retrieval(userid)
    return make_response({'user': userSchema.dump(result), 'message': 'ok'}, 201)

  legacy_routes.add_url_rule('/registration/<userid>', 'get-user', get_user, methods=['GET']) 
  legacy_routes.add_url_rule('/registration', 'new-user', add_user, methods=['POST'])  
  return legacy_routes
