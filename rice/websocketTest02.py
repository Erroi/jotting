# 二、双向
import ssl
import websocket
import json

count = 5

def on_message(ws, message):
    global count
    print(message)
    count -= 1
    if count == 0:
        ws.close()

if __name__ == '__main__':
    ws = websocket.WebSocketApp(
        "wss://api.gemini.com/v1/marketdata/btcusd?top_of_book=true&offers=true",
        on_message=on_message)
    ws.run_forever(sslopt={'cert_reqs': ssl.CERT_NONE})


# {"type":"update","eventId":9583076091,"socket_sequence":0,"events":[{"type":"change","reason":"initial","price":"9405.80","delta":"0.2","remaining":"0.2","side":"ask"}]}
# {"type":"update","eventId":9583076416,"timestamp":1580707252,"timestampms":1580707252014,"socket_sequence":1,"events":[{"type":"change","side":"ask","price":"9405.79","remaining":"0.25456096","reason":"top-of-book"}]}
# {"type":"update","eventId":9583076419,"timestamp":1580707252,"timestampms":1580707252014,"socket_sequence":2,"events":[{"type":"change","side":"ask","price":"9405.78","remaining":"2","reason":"top-of-book"}]}
# {"type":"update","eventId":9583076632,"timestamp":1580707256,"timestampms":1580707256546,"socket_sequence":3,"events":[{"type":"change","side":"ask","price":"9405.77","remaining":"0.2","reason":"top-of-book"}]}
# {"type":"update","eventId":9583076946,"timestamp":1580707265,"timestampms":1580707265518,"socket_sequence":4,"events":[{"type":"change","side":"ask","price":"9405.78","remaining":"2","reason":"top-of-book"}]}

# 由此可以看出，在和Gemini建立连接后，没有向服务器发送任何消息，但可接收到服务器源源不断的推送来的数据。
# 优点：websocket是一种更加实时、高效的数据交互方式。
# 缺点：因为回复和请求是异步的，让我们程序的状态控制逻辑更加复杂。