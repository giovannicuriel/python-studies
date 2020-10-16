"""Main flask application

This is the main entrypoint for Flask application configuration and startup
"""
from flask import Flask
from legacy_service import build_user_registration


user_registration = build_user_registration()
app = Flask('legacy-server')
app.register_blueprint(user_registration.blueprint)
app.run('localhost', 3000)
