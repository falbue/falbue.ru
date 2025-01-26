from flask import Flask, render_template
from flask_socketio import SocketIO
from api import api_bp
import os

app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

# Регистрируем Blueprints
app.register_blueprint(api_bp, url_prefix='/api')
socketio = SocketIO(app)

import os

def check_path(path):
    if os.path.exists(path):
        return True
    else:
        return False

def load_projects(main_app, socketio=None):
    projects_dir = os.path.join(os.path.dirname(__file__), 'projects')
    for project_name in os.listdir(projects_dir):
        project_path = os.path.join(projects_dir, project_name)
        if os.path.isdir(project_path) and 'server.py' in os.listdir(project_path):
            project_module = __import__(f'projects.{project_name}.server', fromlist=['server'])
            main_app.register_blueprint(project_module.Blueprint, url_prefix=f'/{project_name}')
            if socketio is not None and hasattr(project_module, 'socketio'):
                project_module.socketio.init_app(main_app)

if check_path("projects") == True:
    load_projects(app, socketio)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

socketio.init_app(app)
socketio.run(app, host='0.0.0.0', port=80, debug=True, allow_unsafe_werkzeug=False)