# coding:utf-8
import os,time,logging

'''存放日志路径'''
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path),'logs')

'''如果不存在就自动创建'''
if not os.path.exists(log_path):os.mkdir(log_path)

class Log:

    def __init__(self):
        '''文件命名'''
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        #输入日志格式
        self.formatter = logging.Formatter('[%(asctime)s - %(filename)s - %(lineno)s] - %(levelname)s:%(message)s')

    def __console(self,level,message):
        '''创建一个FileHandler,用于写入本地'''
        fh  = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        #创建一个StreamHandler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 下面两行避免日志输出重复问题
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

if __name__ == '__main__':
    log = Log()
    log.info('---测试开始---')
    log.info('输入密码')
    log.error('--测试结束---')