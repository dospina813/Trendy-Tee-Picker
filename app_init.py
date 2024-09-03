from flask import Flask
from routes import register_routes

# The app initialization must be done in this module to avoid circular dependency problems.

def create_initialized_flask_app():
    # DO NOT INSTANTIATE THE FLASK APP IN ANOTHER MODULE.
    app = Flask(__name__, static_folder='static')

    register_routes(app)

    return app