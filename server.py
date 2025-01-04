from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)
PROJECTS_FOLDER = 'static/projects'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/projects', methods=['GET'])
def get_projects():
    projects = []
    for filename in os.listdir(PROJECTS_FOLDER):
        if filename.endswith('.json'):
            # Открываем файл и считываем информацию
            with open(os.path.join(PROJECTS_FOLDER, filename), 'r', encoding='utf-8') as f:
                project_data = json.load(f)
                projects.append(project_data)
    
    return jsonify(projects)

# app.run(host='0.0.0.0', port=80)
app.run(host='0.0.0.0',debug=True)