from flask import Flask, render_template
from api import api_bp
from LiveMessage import LiveMessage_bp, socketio  # Импортируем socketio из LiveMessage

app = Flask(__name__)

# Регистрируем Blueprints
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(LiveMessage_bp, url_prefix='/live-message')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

<<<<<<< HEAD
socketio.init_app(app)
socketio.run(app, host='0.0.0.0', debug=True, allow_unsafe_werkzeug=True)
=======
# Запуск приложения
app.run(host='0.0.0.0', debug=True, port=80)
>>>>>>> origin/main
