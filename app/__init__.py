from flask import Flask

from app.routes.process import process_blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__);
    app.config.from_pyfile("config.py")
    CORS(app)
  
    app.register_blueprint(process_blueprint, url_prefix="/api/v1")

    return app
