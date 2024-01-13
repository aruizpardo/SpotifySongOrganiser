from user import UserData

import json
import requests

def get_playlists (user: UserData) -> None:
    auth_header = {"Authorization": user.get_data('token_type') + " " + user.get_data('access_token')}
    request = requests.get('https://api.spotify.com/v1/me/playlists', headers=auth_header)
    response = json.loads(request.content.decode())
    playlists = []
    for item in response['items']:
        playlists.append(item['name'])
    print('\n'.join(playlists))
    return playlists