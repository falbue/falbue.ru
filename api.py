from flask import Blueprint, jsonify
import os
import json

api_bp = Blueprint('api', __name__)


PROJECTS_FOLDER = 'static/projects'

@api_bp.route('/', methods=['GET'])
def check_api():
    return jsonify({"message":"api активно"})

@api_bp.route('/projects', methods=['GET'])
def get_projects():
    projects = []
    for filename in os.listdir(PROJECTS_FOLDER):
        if filename.endswith('.json'):
            with open(os.path.join(PROJECTS_FOLDER, filename), 'r', encoding='utf-8') as f:
                project_data = json.load(f)
                projects.append(project_data)
    return jsonify(projects)
