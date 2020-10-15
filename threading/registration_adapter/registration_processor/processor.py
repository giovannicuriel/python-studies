
def build_registration_processor(legacy_server, task_executor):
  class RegistrationProcessor:
    def __init__(self):
      self.wait_time = 2
    def __build_callback(self, user_id):
      return lambda: self.retrieve_results(user_id)
    def retrieve_results(self, user_id):
      user = legacy_server.get_user_status(user_id)
      print(f'User status is {user["process_status"]}')
      if user['process_status'] != 'ok' and user['process_status'] != 'error':
        task_executor.add_task(self.wait_time, self.__build_callback(user_id))
    def process_message(self, message):
      user = legacy_server.register_user(message)
      print(f'User ID is {user["userid"]}')
      task_executor.add_task(self.wait_time, self.__build_callback(user['userid']))
  return RegistrationProcessor
