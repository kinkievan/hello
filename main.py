from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.FileHandler(filename='translator.log', encoding='utf-8')
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')