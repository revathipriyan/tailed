
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import SocketIO, emit
import os, sys, json, random, time

app = Flask(__name__)
socketio = SocketIO(app)


def tail(filepath):
    with open(filepath, 'r') as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
            yield line
            


# @socketio.on('connect')
# def ws_connect():
#     try:
#         # data = tail("dummy_log.txt")
#         # print("data",next(data))
#         # tem = {"counter": str(next(data))}
#         # emit('user',tem,broadcast=True)
#         print("connected")
#     except Exception as e:
#         print("file read went wrong!",e)

@socketio.on('disconnect')
def ws_disconnect():
    try:
       print("client disconnected!!")
    except Exception as e:
        print("file read went wrong!",e)

@socketio.on('new_line')
def new_message(data):
    print("data",data)
    emit('user',data,broadcast=True)


@app.route('/',methods=['GET','POST'])
def home():
    # f = open("test.txt","r")
    # data = f.read()
    # data = tail("dummy_log.txt")
    # data = {"counter":str(next(data))}
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app)
    