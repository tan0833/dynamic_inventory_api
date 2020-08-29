import datetime

class OperteTime:

    def format_time(self):
        time_stamp = '{0:%Y-%m-%d %H_%M_%S}'.format(datetime.datetime.now())
        return time_stamp


if __name__ == '__main__':
    a = OperteTime()
    b = a.format_time()
    print(b)