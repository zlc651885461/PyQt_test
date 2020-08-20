import datetime
import time

if __name__ == '__main__':
    import time

    time1 = datetime.datetime.now()
    time.sleep(14)
    time2 = datetime.datetime.now()
    print((time2 - time1).seconds)