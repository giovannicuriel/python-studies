
from flask import Flask
from legacy_service import default_app

app = Flask('legacy-server')
app.register_blueprint(default_app.blueprints)
app.run('localhost', 3000)
