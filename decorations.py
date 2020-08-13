import time
import sys
import random

ERROR_COLOR = '\u001b[43;1m'
RESET_COLOR = '\u001b[0m'
SUCCESS_COLOR = '\u001b[41;1m'


def loadingpercentage(initnum: int, endnum: int):
    """Writes the percentage done.

    Args:
        initnum (int): Where the percentage should start
        endnum (int): Where the percentage should end
    """
    for i in range(initnum, endnum):
        time.sleep(0.01)
        j = 0
        stri = ''
        while j <= i:
            stri += '|'
            j += 1
        sys.stdout.write(u"\u001b[1000D" + str(i+1) + "%" + str(stri))
        if i % 100 == random.randint(0, 100):
            time.sleep(random.randint(0, 2))
        sys.stdout.flush()


# loadingpercentage(0, 50)
# loadingpercentage(51, 100)
