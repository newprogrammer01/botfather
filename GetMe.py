import requests
TOKEN='6245605190:AAHYvQkFoBmeMAKvFbFd9F4op_gNY41agRI'
BASE_URL=f'https://api.telegram.org/bot{TOKEN}/getMe'

response=requests.get(url=BASE_URL)
user=response.json()['result']
print(user)