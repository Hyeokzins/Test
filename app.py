from flask import Flask, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        socketio.emit('message', {'data': text})
        return "Success", 200
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)