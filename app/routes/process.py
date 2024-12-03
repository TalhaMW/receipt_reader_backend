from flask import Blueprint, jsonify
from app.services import process_images

process_blueprint = Blueprint("process", __name__)


@process_blueprint.route("/ping", methods=["GET"])
def ping():
    return jsonify("Running")

@process_blueprint.route("/process-images", methods=["GET"])
def process_images_endpoint():
    result = process_images()
    return jsonify(result)