from supercollider import Server, Synth, Buffer, AudioBus, ADD_TO_TAIL, Group
import time
import random
from matplotlib import pyplot as plt
import socketio

n_episodes = 4
episode_length = 2 


# TODO: include in a MeatSpace variable and instantiate in MindSpace
fnirs_buffer = [0,0,0,0,0]
fnirs_total = []

sio = socketio.Client()
sio.connect('http://localhost:3002')

server = Server()

def send_ping():
    global start_timer
    start_timer = time.time()
    sio.emit('ping_from_client')


@sio.event
def connect():
    print('connected to server')
    send_ping()

@sio.event
def chat_message(sid):
    print("message ", sid)
    print(sid['data'])
    fnirs_buffer.append(sid['data'])
    # print("message ", data)

@sio.event
def pong_from_server(data):
    global start_timer
    latency = time.time() - start_timer
    print('latency is {0:.2f} ms'.format(latency * 1000))
    sio.sleep(1)
    send_ping()
