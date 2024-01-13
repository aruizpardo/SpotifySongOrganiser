from dotenv import load_dotenv
from urllib.parse import urlencode

import eel
import os

# Internal
from user import UserData
import callbacks
import utils.log.log as log
import utils.web.playlists


user = UserData()

log.message('info', 'Iniciando aplicación')

@eel.expose
def get_playlists_frontend():
    return utils.web.playlists.get_playlists(user)

dirname = os.path.dirname(__file__)
eel.init(os.path.join(dirname, 'graphic'))
eel.start('login.html', close_callback=callbacks.close_callback)
