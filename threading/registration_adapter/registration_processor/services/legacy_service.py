"""Legacy service wrapper"""


def build_legacy_service(requests):
    """Factory for legacy service

    :param requests requests: this should be the 'requests' library, which will
    be used to send and receive data to/from legacy service
    """
    class LegacyService:
        """Legacy service wrapper"""
        def __init__(self, url):
            self.url = url

        def register_user(self, user):
            """Send a user registration request

            There are a bunch of things that were not added to this function for
            the sake of simplicity - this is a threading tutorial, not a how
            well a system should be designed to achieve great performance.

            I might add, though, a few checks in the future, so that this is
            not a half-backed system.
            :param User user: the user to be registered
            """
            response = requests.post(self.url, json=user)
            return response.json()['result']

        def get_user_status(self, user_id):
            """Retrieve user status

            This function will ask legacy service for user registration status.
            :param str user_id: the user ID to be asked
            """
            response = requests.get(f'{self.url}/{user_id}')
            user_status = response.json()
            print(f'User current status is {user_status}')
            return response.json()['result']
    return LegacyService
