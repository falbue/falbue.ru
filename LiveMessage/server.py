import uuid
from flask import Blueprint, render_template
from flask_socketio import SocketIO, join_room, leave_room

LiveMessage_bp = Blueprint(
    'live_message',
    __name__,
    template_folder='templates',  # Указываем путь к папке с шаблонами конкретно для этого Blueprint
    static_folder='static',
    static_url_path='/static'
)

socketio = SocketIO()

@LiveMessage_bp.route('/')
def index():
    chat_id = uuid.uuid4().hex  # Генерируем chat_id
    return render_template('main.html', chat_id=chat_id)

@LiveMessage_bp.route('/chat/<chat_id>')
def chat(chat_id):
    return render_template('chat.html', chat_id=chat_id)

@socketio.on('join_chat')
def on_join(data):
    chat_id = data['chat_id']
    sender_id = data['sender_id']
    join_room(chat_id)  # Подключаем клиента к комнате с chat_id
    print(f'Client joined chat {chat_id}')
    socketio.emit('receive_message', {'text': 'Пользователь подключился!', 'sender_id': sender_id}, room=chat_id)

@socketio.on('update_message')
def handle_message(data):
    chat_id = data['chat_id']
    text = data['text']
    sender_id = data['sender_id']
    # Отправляем сообщение только в комнату chat_id
    socketio.emit('receive_message', {'text': text, 'sender_id': sender_id}, room=chat_id)

@socketio.on('leave_chat')
def on_leave(data):
    chat_id = data['chat_id']
    leave_room(chat_id)  # клиент покидает комнату
    print(f'Client left chat {chat_id}')
