import zmq
import vexmessage


context = zmq.Context()
sub_socket = context.socket(zmq.SUB)
sub_socket.connect('tcp://127.0.0.1:4000')
sub_socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    frame = sub_socket.recv_multipart()
    message = vexmessage.decode_vex_message(frame)

    print(message)
