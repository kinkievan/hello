import sys

import os
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Wor000000000000000d!'


if __name__ == '__main__':
    logger.info("賴炘玫測試")
    app.run(host='0.0.0.0')