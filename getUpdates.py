import requests
TOKEN='6245605190:AAHYvQkFoBmeMAKvFbFd9F4op_gNY41agRI'
BASE_URL=f'https://api.telegram.org/bot{TOKEN}/getUpdates'


response = requests.get(url=BASE_URL)
updates=response.json()['result']

for update in updates:
    msg=update['message']
    print(msg['text'])