from flask import Flask

app = Flask(__name__)

@app.route('/oauth2/callback')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
