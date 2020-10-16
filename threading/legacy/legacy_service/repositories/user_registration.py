"""User registration repository module"""

def build_user_registration_repository(random, current_time):
    """Build a user registration repository class

    :param function random: a function that generates a random number, given min
    an max values (defined as its parameters).
    :param function current_time: a function that returns Unix time in seconds
    """
    class UserRegistrationRepository:
        """User registration repository class

        This class is a simple in-memory dictionary that contains all user
        registrations. It is not intented to be persisted nor have a significant
        performance.
        """

        def __init__(self):
            self.user_map = {}
            self.metadata = {}

        def add_user(self, user):
            """Add a user registration

            This function will also set how much time it will take to
            considered this registration as 'ready'. This is set to be 10 +
            random value between 0 and 10.

            :param User user: the user to be added. User ID must have already
            been set
            """
            delay = 10 + random(0, 10)
            print(f'Delaying user {user.user_id} by {delay} seconds.')
            self.metadata[user.user_id] = {
                'ttl': current_time() + delay
            }
            user.process_status = 'not-ready'
            self.user_map[user.user_id] = user
            return user.user_id

        def get_user(self, user_id):
            """Retrieve a user from the store

            If the time set to this particular registration is already elapsed, then
            this function will set if it was successful or not.

            As one might notice, this decision is lazy.
            """
            generate_status = lambda: ['ok', 'error'][random(0, 1)]
            is_ready = lambda: (user.process_status == 'not-ready') and (
                self.metadata[user_id]['ttl'] < current_time())

            if user_id in self.user_map:
                user = self.user_map[user_id]
                user.process_status = generate_status() if is_ready() else user.process_status
                return user
            return None

    return UserRegistrationRepository
