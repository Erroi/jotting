# 消息队列的模式是发布和订阅：
# 一个或多个消息发布者可以发布消息，一个或多个消息接收者可以订阅消息。

# 订阅者 1
import zmq

def run():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://127.0.0.1:6666')
    socket.setsockopt_string(zmq.SUBSCRIBE, '')

    print('client 1')
    while True:
        msg = socket.recv()
        print('msg: %s' % msg)

if __name__ == '__main__':
    run()
