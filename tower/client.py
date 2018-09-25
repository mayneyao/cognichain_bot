from configparser import ConfigParser
from urllib.parse import urljoin

import requests

conf = ConfigParser()
conf.read('conf.ini')

TOWER_BASE_URL = conf.get('APP', 'tower_base_url')
CLIENT_ID = conf.get('APP', 'client_id')
CLIENT_SECRET = conf.get('APP', 'client_secret')
REDIRECT_URL = conf.get('APP', 'redirect_url')


class TowerClient:
    def __init__(self, auth_code):
        self.auth_code = auth_code
        self.requests = requests.Session()
        self.access_token = None
        self.token_type = None
        self.expires_in = None
        self.refresh_token = None
        self.created_at = None
        self.get_token()
        self.set_header()

    def get_token(self):
        res = self.requests.post('https://tower.im/oauth/token', json={
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'code': self.auth_code,
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URL,
        }).json()

        print(res)
        self.access_token = res['access_token']
        self.token_type = res['token_type']
        self.expires_in = res['expires_in']
        self.refresh_token = res['created_at']
        self.created_at = res['created_at']

    def set_header(self):
        self.requests.headers = {
            'Authorization': 'Bearer {}'.format(self.access_token)
        }

    def refresh_token(self):
        pass

    def get_team_all_projetcts(self):
        url = 'https://tower.im/api/v1/teams/560be5e1666649d8958460c37710b703/projects/'
        res = self.requests.get(url).json()
        return res

    def get_project(self, project_id):
        url = urljoin(TOWER_BASE_URL, 'projects/{}'.format(project_id))
        return self.requests.get(url).json()
