import os
import requests

TOKEN=os.environ['TOKEN']
def sendPhoto(chat_id:str, photo:str):
    URL=f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    param = {
        'chat_id':chat_id,
        'photo':photo,
        'caption':'This is a photo'

    }

    
    r=requests.get(url=URL, params=param)
    print(r.json())

chat_id='1901668739'
photo_url='https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg'

sendPhoto(chat_id, photo=photo_url)