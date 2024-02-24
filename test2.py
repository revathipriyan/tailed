import socketio
import time

sio = socketio.Client()
sio.connect('http://localhost:5000')
time.sleep(5)


def tail(filepath):
    with open(filepath, 'r') as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
            else:
                print("emitting event")
                sio.emit('new_line', {'counter': line.strip()})

tail_generator = tail("dummy_log.txt")



