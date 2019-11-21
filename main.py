import logging,sys

filelog = True
path = r'log.txt'

logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)

# ?�μ�??,�p�G??�ޥΡA��p�h��?�ΡA�C��?�K�[Handler�A�y�����`��ӡA??�C�����������Ҧ���handler�A�Z���b���s�K�[�A�i�H��?????
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)

# file log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
if filelog:
    fh = logging.FileHandler(path,encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

# console log
formatter = logging.Formatter('%(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

if __name__ == '__main__':
    logger.info("?�O�@???")