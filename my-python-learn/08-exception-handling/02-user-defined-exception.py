# main exceptions https://martinxpn.medium.com/exception-hierarchy-python-58-100-days-of-python-9d8585e6569b
class OverTheLimitException(Exception):
    def __init__(self, msg):
        self.msg = msg

i = 501

if(i > 500):
    raise OverTheLimitException("More than ");