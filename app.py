from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        print('flask 1 fabric')
        return "Hello Flask 1"

if __name__ == "__main__":
        app.run(port=8888)
