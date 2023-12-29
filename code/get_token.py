from dotenv import load_dotenv
from urllib.parse import urlencode

import base64
import json
import os
import requests
import socket
import webbrowser

class UserData:
    _user_data = None

    def __init__(self):
        load_dotenv()
        client_id = os.environ['client_id']
        client_secret = os.environ['client_secret']

        # Open web authentication
        auth_headers = {
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": "http://localhost:3000",
            "scope": "user-library-read playlist-read-private playlist-modify-private playlist-modify-public"
        }
        webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

        # Server to get code
        host = '127.0.0.1'
        port = 3000
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)
        conn, address = server_socket.accept()
        data = conn.recv(1024).decode()
        code = data.split()[1][7:]
        conn.send('HTTP/1.0 200 OK\n'.encode())
        conn.send('Content-Type: text/html\n'.encode())
        conn.send("""
            <html>
                <script type="text/javascript">
                    window.close();
                </script>
                <body>
                </body>
            </html>
            """.encode())
        conn.close()

        encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")
        token_headers = {
            "Authorization": "Basic " + encoded_credentials,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        token_data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "http://localhost:3000"
        }
        req = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

        self._user_data = json.loads(req.text)

    def get_data(self, atribute: str = '') -> str: 
        return self._user_data[atribute]
