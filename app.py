
from flask import Flask, request

app = Flask(__name__)



@app.route('/oauth2/callback')
def get_auth_code():
    auth_code = request.args.get('code')
    return


if __name__ == '__main__':
    app.run()
