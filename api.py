from flask import Blueprint, jsonify
import os
import json

api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def check_api():
    return jsonify({"message":"api активно"})