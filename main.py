import logging
from app_init import create_initialized_flask_app

# Flask app creation should be done by create_initialized_flask_app to avoid circular dependency problems.
app = create_initialized_flask_app()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Vercel requires the app to be named 'app'
application = app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)