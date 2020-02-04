# RESTful 的重要要求：无状态。
# 每个REST请求都是独立的，不需要服务器在会话Session中缓存中间状态来完成这个请求。
# 比如：服务器A收到请求时宕机了，转而发送给交易所的服务器B，也能继续完成，这个接口就是无状态的。

# 反例：有状态。
# 服务器要求，在客户端请求取消订单的时候，必须发送两次不一样的请求：第一次为‘等待取消’，第二次为‘确认取消’

import requests
import json
import base64
import hmac
import hashlib
import datetime
import time

current_time = datetime.datetime.now()
print(int(datetime.datetime.timestamp(current_time)*1000))
print(int(time.mktime(current_time.timetuple())*1000))

base_url = 'https://api.sandbox.gemini.com'
endpoint = '/v1/order/new'
url = base_url + endpoint

gemini_api_key = 'account-zmidXEwP72yLSSybXVvn'
gemini_api_secret = '375b97HfE7E4tL8YaP3SJ239Pky9'.encode()

t = datetime.datetime.now()
payload_nonce = str(int(time.mktime(t.timetuple())*1000))

payload = {
    'requests': '/v1/order/new',
    'nonce': payload_nonce,
    'symbol': 'btcusd',
    'amount': 5,
    'price': '3633.00',
    'side': 'buy',
    'type': 'exchange limit',
    'options': ['maker-or-cancel']
}

encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
signature = hmac.new(gemini_api_secret,b64,hashlib.sha384).hexdigest()

requests_headers = {
    'Content-Type': 'text/plain',
    'Content-Length': '0',
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': 'no-cache'
}

response = requests.post(url,
                        data=None,
                        headers=requests_headers)
new_order = response.json()
print(new_order)