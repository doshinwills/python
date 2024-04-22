import logging

try:
    a = 5
    a/0
except ZeroDivisionError as e:
    logging.error("Zero Division Error", e)
    print("Zero Division Error")
except:
    print("All Ex")