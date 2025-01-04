from flask import Flask, render_template
from api import api_bp
# from LiveMessage import LiveMessage_bp

app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix='/api')
# app.register_blueprint(LiveMessage_bp, url_prefix='/live-message')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Запуск приложения
app.run(host='0.0.0.0', debug=True)
