import os
import requests

TOKEN = os.environ['TOKEN']

def sendMessage(chat_id:str, text:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    button = {
        'text':'button 1'
    }
    keyboard = [[button, button]]
    reply_markup = {
        'keyboard':keyboard
    }

    payload = {
        'chat_id':chat_id,
        'text':'Salom',
        'reply_markup':reply_markup
    }
    r=requests.get(url=URL, json=payload)
chat_id='1901668739'
sendMessage(chat_id=chat_id, text='Salom')