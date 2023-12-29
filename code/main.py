from dotenv import load_dotenv
from urllib.parse import urlencode

import eel
import json
import os
import requests

# Internal
from user import UserData
import callbacks
import utils.log.log as log

dirname = os.path.dirname(__file__)



eel.init(os.path.join(dirname, 'graphic'))
eel.start('login.html', close_callback=callbacks.close_callback)



#user = UserData()

#auth_header = {"Authorization": user.get_data('token_type') + " " + user.get_data('access_token')}
#request = requests.get('https://api.spotify.com/v1/me/playlists', headers=auth_header)
#playlist = json.loads(request.content.decode())
#print (playlist)