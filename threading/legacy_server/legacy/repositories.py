def build_user_repository(random, current_time):
  """
  Constrói um repositório de usuários
  
  :param function random: Uma função que escolhe aleatoriamente um valor, sendo
  seus limites passados como parâmetro. Por exemplo, random(1, 10) deve
  escolher um valor entre 1 e 10 (inclusive). Deve ser compatível com
  random.randint.
  :param function current_time: Uma função que, quando chamada, deve retornar o
  tempo Unix em segundos
  """
  class UserRepository:
    def __init__(self):
      self.user_map = {  }
      self.metadata = { }

    def add_user(self, user):
      delay = 10 + random(0, 10)
      print(f'Delaying user {user.user_id} by {delay} seconds.')
      self.metadata[user.user_id] = {
        'ttl': current_time() + delay
      }
      user.process_status = 'not-ready'
      self.user_map[user.user_id] = user
      return user.user_id

    def get_user(self, user_id):
      user = self.user_map[user_id]
      user.process_status = ['ok', 'error'][random(0,1)] if (user.process_status == 'not-ready') and (self.metadata[user_id]['ttl'] < current_time()) else user.process_status
      return user

  return UserRepository
