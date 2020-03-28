import json
import requests


#这里用 HTTPS End Point 代替
nodeUrl = 'https://nr02.d1.zetez.com/node'

apiUrl = nodeUrl + '/data'

data = {
    'data': 'Hello from Python'
}

resp = requests.post(
        apiUrl,
        json = data
    )

if resp.status_code != 200:
    # This means something went wrong.
    print('HTTP Error: ' + resp.status_code)
else:
    respJson = resp.json()

    print('HTTP Response: '+json.dumps(respJson))

