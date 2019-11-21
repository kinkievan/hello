import sys
sys.setdefaultencoding('utf-8')

import os
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

from flask import Flask
app = Flask(__name__)
import logging,sys
import logging,sys

filelog = True
path = r'log.txt'
logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
if filelog:
    fh = logging.FileHandler(path,encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
formatter = logging.Formatter('%(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
@app.route('/')
def hello_world():  
    return 'Hel000000000000lo World!'

if __name__ == '__main__':
    logger.info("賴炘玫測試")
    app.run(host='0.0.0.0')