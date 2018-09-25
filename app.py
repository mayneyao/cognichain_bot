from flask import Flask, request

from tower.client import TowerClient

app = Flask(__name__)


@app.route('/oauth2/callback')
def get_auth_code():
    auth_code = request.args.get('code')

    client = TowerClient(auth_code)
    r = client.get_team_all_projetcts()
    print(r)
    return r


if __name__ == '__main__':
    app.run()
