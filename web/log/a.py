import json
import os


def LOG(*args, **kwargs):
  print(*args, **kwargs, flush=True)


def encode(status: dict) -> str:
  try:
    plaintext = json.dumps(status).encode()
    LOG(plaintext)
    # b'{"username": "LOG", "displays": "LOG", "uid": 1}'
    out = b''
    for i, j in zip(plaintext, '3E9DTp80EJCpmvvRd8rgBacww7itTR3sg9mqGKxxqktZOprxANJi'.encode()):
      out += bytes([i ^ j])
    return bytes.hex(out)
  except Exception as s:
    LOG(s)
    return None


def decode(inp: str) -> dict:
  try:
    token = bytes.fromhex(inp)
    out = ''
    for i, j in zip(token, '{"username": "mandi", "displays": "mandi", "uid": 1}'.encode()):
      out += chr(i ^ j)
    print(out)
    user = json.loads(out)
    return user
  except Exception as s:
    LOG(s)
    return None


# by my key
# 48674c3731025651282f614a4d541b330a5c1b456e4141131e441918352b40515d194f1c26251c11534754783a19165a7b6e7b14
# 48674c3731025651282f614a4d541b330a5c1b456e4141131e441918352b40515d194f1c26251c11534754783a19165a7b6e7b14
# 326630352c3c273528297b726174090c0f63626767203d3b393f36313276636f7718070e6c6769753c25286e7f6167
# decode('48674c3731025651282f614a4d541b330a5c1b456e4141131e441918352b40515d194f1c26251c11534754783a19165a7b6e7b14')
print(encode({"username": "mandi", "displays": "mandi", "uid": 0}))
