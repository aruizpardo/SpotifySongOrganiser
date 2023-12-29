from dotenv import load_dotenv
from urllib.parse import urlencode

import json
import requests

# Internal
from user import UserData


user = UserData()

auth_header = {"Authorization": user.get_data('token_type') + " " + user.get_data('access_token')}
request = requests.get('https://api.spotify.com/v1/me/playlists', headers=auth_header)
playlist = json.loads(request.content.decode())
print (playlist)