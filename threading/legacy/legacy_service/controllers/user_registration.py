def build_user_registration_controller(user_repository, uuid):
  """
  Uma função que constrói um controlador de usuários

  :param UserRepository user_repository: o repositório de usuários a ser
  utilizado por este controlador
  :param function uuid: uma função que, quando chamada, retorna uma string
  contendo um UUID.
  """
  class Controller:
    def create_user(self, user):
      user.user_id = uuid()
      user_repository.add_user(user)
      return { 'userid': user.user_id }
    def retrieve_user(self, user_id):
      user = user_repository.get_user(user_id)
      return user
  return Controller
