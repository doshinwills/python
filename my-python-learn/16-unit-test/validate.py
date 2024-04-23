from datetime import *

def validateCc(expDate, returnType):
    if expDate>datetime.now().date():
        return 'Valid'
    else:
        if returnType == 0:
            return 'Expired'
        else:
            raise RuntimeError
