from flask import Flask
import time
import random
import uuid
from legacy import routes

from legacy.repositories import build_user_repository
from legacy.controllers import build_user_controller

userRepo = build_user_repository(random.randint, lambda: int(time.time()))()
userController = build_user_controller(userRepo, lambda: str(uuid.uuid4()))()
legacyRoutes = routes.build_routes(userController)

app = Flask('legacy-server')
app.register_blueprint(legacyRoutes)
app.run('localhost', 3000)

