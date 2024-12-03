from flask import Flask
from flask_cors import CORS
from app.routes.process import process_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    # Allow all origins for all API routes
    CORS(app)

    app.register_blueprint(process_blueprint, url_prefix="/api/v1")
    
    return app
