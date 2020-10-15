from collections import namedtuple
import time
import random
import uuid

from legacy_service.routes.user_registration import build_user_registration_blueprint
from legacy_service.repositories.user_repository import build_user_repository
from legacy_service.controllers.user_registration import build_user_registration_controller
from legacy_service.models.user import user_schema, User

__DefaultApp = namedtuple('DefaultApp', ['controllers', 'repositories', 'blueprints'])
__user_repo = build_user_repository(random.randint, lambda: int(time.time()))()
__user_controller = build_user_registration_controller(__user_repo, lambda: str(uuid.uuid4()))()
__legacy_blueprints = build_user_registration_blueprint(__user_controller, user_schema, User)

default_app = __DefaultApp(
  controllers=__user_controller,
  repositories=__user_repo,
  blueprints=__legacy_blueprints
)
