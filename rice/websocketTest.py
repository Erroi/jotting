# webSocket 是一种在**单个 TCP/TSL 连接**上，进行全双工、双向通信的协议。
# webSocket 使客户端与服务器之间的数据交换变得简单高效，**服务端也可以主动向客户端推送**数据。
# 两者只需要完成**一次握手**，两者直接就可以直接创建持久性连接，并进行双向数据传输。

import websocket
import _thread
import time

#  一、双工
# 接受到服务器发送的消息时调用
def on_message(ws, message):
    print('Received:' + message)

# 和服务器建立完成连接时调用
def on_open(ws):
    # 线程运行函数
    def gao():
        # 往服务器依次发送0-4，每次发送完休息0.01s
        for i in range(5):
            time.sleep(0.01)
            msg="{0}".format(i)
            ws.send(msg)
            print('Sent:' + msg)
        # 休息1秒用于接收服务器回复的消息
        time.sleep(1)

        # 关闭Websocket的连接
        ws.close()
        print('Websocket closed')
    
    # 在另一个线程运行gao()函数
    _thread.start_new_thread(gao, ())

if __name__ == '__main__':
    ws = websocket.WebSocketApp('ws://echo.websocket.org',
                            on_message = on_message,
                            on_open= on_open)
    ws.run_forever()

