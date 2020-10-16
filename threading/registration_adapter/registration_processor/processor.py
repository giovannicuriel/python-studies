"""Factory for message processor"""


def build_processor(legacy_server, task_executor):
    """Build a message processor class"""
    class RegistrationProcessor:
        """Class for user registration message processor

        This class is a simple redirection - it will process a message received
        from a RabbitMQ queue and forward it to the legacy service.

        It also request the legacy service for user registration status.
        """

        def __init__(self):
            self.wait_time = 2

        def __build_callback(self, user_id):
            return lambda: self.retrieve_results(user_id)

        def retrieve_results(self, user_id):
            """Ask legacy server for user registration status

            :param str user_id: The user ID to be checked
            """
            user = legacy_server.get_user_status(user_id)
            print(f'User status is {user["process_status"]}')
            if user['process_status'] != 'ok' and user['process_status'] != 'error':
                task_executor.add_task(
                    self.wait_time, self.__build_callback(user_id))

        def process_message(self, message):
            """Process a user registration message

            :param message: The message to be received. It should have all
            attributes for a User object
            """
            user = legacy_server.register_user(message)
            print(f'User ID is {user["userid"]}')
            task_executor.add_task(
                self.wait_time, self.__build_callback(user['userid']))
    return RegistrationProcessor
