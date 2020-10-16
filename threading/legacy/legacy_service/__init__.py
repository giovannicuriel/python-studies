"""Default structures for this app

This file will build and properly configure all structures needed to run this
app (except, of course, the server). Just call `build_user_registration` and
get a ready-to-use blueprint! (And also a controller and a repository, just in
case)
"""
from collections import namedtuple
import time
import random
import uuid

from .blueprints.user_registration import build_user_registration_blueprints
from .repositories.user_registration import build_user_registration_repository
from .controllers.user_registration import build_user_registration_controller
from .models.user import user_schema, User

# Default structures


def build_user_registration():
    """Build user registration structures
    """
    repository = build_user_registration_repository(
        random.randint, lambda: int(time.time()))()
    controller = build_user_registration_controller(
        repository, lambda: str(uuid.uuid4()))()
    blueprint = build_user_registration_blueprints(controller, user_schema, User)

    UserRegistration = namedtuple(
        'UserRegistration', ['controller', 'repository', 'blueprint'])
    return UserRegistration(controller=controller, repository=repository, blueprint=blueprint)
