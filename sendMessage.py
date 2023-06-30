import os
import requests

TOKEN = os.environ['TOKEN']
def sendMessage(chat_id:str, text:str):
    URL=f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    param = {
        'chat_id':chat_id,
        'text':'Salom Jasurbek'
    }
    r = requests.get(url=URL,params=param)
chat_id='1901668739'
sendMessage(chat_id=chat_id, text='Salom ')