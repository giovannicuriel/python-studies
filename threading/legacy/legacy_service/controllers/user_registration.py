"""User registration controller factory
"""
from collections import namedtuple


def build_user_registration_controller(user_repository, uuid):
    """Builder for user registration controller class

    This function must be called in order to define and create a user registration
    controller class.

    :param UserRegistrationRepository user_repository: user repository to be used by this
    controller
    :param function uuid: a function that generates a unique ID.
    """
    def create_user(user):
        """Create a new user

        :param User user: the user to be added. UserID will be overwritten.
        :returns A simple dictionary with only on parameter, which will be the
        user ID
        """
        user.user_id = uuid()
        user_repository.add_user(user)
        return {'userid': user.user_id}

    def retrieve_user(user_id):
        """Retrieve a registered user from the repository
        """
        user = user_repository.get_user(user_id)
        return user
    UserRegistrationController = namedtuple('UserRegistrationController', [
                                            'create_user', 'retrieve_user'])

    return lambda: UserRegistrationController(create_user=create_user, retrieve_user=retrieve_user)
