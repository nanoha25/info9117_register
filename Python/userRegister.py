from flask import Flask
from Python import enterPassword
from Python import enterUsername

app = Flask(__name__)
host="localhost"
port="5000"
address="http://{0}:{1}".format(host,port)

@app.route('/')
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
