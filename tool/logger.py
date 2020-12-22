'''
三大块：
1. 日志器   日志的入口，然后往里面去写，比喻：日记本
级别越来越高：    原则：你设置的级别，比它大的级别都会显示出来，比他低级的级别是不会显示出来的
debug（调试级别），info（信息级别），warning（警告级别），error（错误级别），critical（致命的，严重的）
2. 格式器   以什么样的格式去写这个日志
3. 处理器   表示对日志内容的一个处理方式，比如可以直接把日志输出到console里面，或者是输出到文件里面
'''

from tool.test import get_path
# 导包：把日志模块和处理器一并导入进来
import logging.handlers

class Logger():
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 1. 获取日志器
            cls.logger = logging.getLogger('WebAutoTest')
            # 给日志器设置总的级别，级别是封装在logging里面的
            # 我要设置错误级别，完全大写
            cls.logger.setLevel(logging.INFO)

            # 2. 获取格式器
            '''
            asctime：当前时间
            levelname：日志级别
            name：日志指定的名字
            filename：当前文件，当前报错的文件
            funcName：那个函数报错
            lineno：函数的第几行报错了
            message：具体错误信息
            ===> 2020-11-18 16:51:26,167 ERROR [root] [logger.py (<module>:60)] - 错误信息
            2020-11-18 16:51:26,168 CRITICAL [root] [logger.py (<module>:61)] - 致命的
            '''
            # 2.1 这个只是要输出的样式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
            # 2.2 获取格式器，参数 具体要输出什么样的样式
            fm = logging.Formatter(fmt)

            # 3. 获取处理器，按时间切割的文件处理器（工作中都是用的midnight）
            '''
            FileHandler：意思是所有日志文件都放在一个文件里
            TimedRotatingFileHandler：按时间去切割文件，比如可以一个小时切割出一个文件
            
            backupCount=3：除了原件，只保存最新的三个
            '''
            tf = logging.handlers.TimedRotatingFileHandler(filename=get_path('logger', 'test.log'),
                                                      when='H',
                                                      interval=1,
                                                      backupCount=3,
                                                      encoding='utf-8')

            # 在处理器中添加格式器
            tf.setFormatter(fm)
            # 给处理器设置一个级别
            # tf.setLevel(logging.INFO)
            # 在日志器中添加处理器
            cls.logger.addHandler(tf)
        return cls.logger
'''
class Logger():
    def __init__(self):
        self.logger = logging.getLogger('fps.log')
        self.fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] ===> %(message)s"
        self.filename = get_path('logger', 'test.log')
        self.log_config()

    def log_config(self):
        if not self.logger.handlers:
            logging.basicConfig(level=logging.DEBUG,
                                format=self.fmt,
                                datefmt='%d %b %Y %H:%M:%S',
                                filename=self.filename,
                                filemode='w')
            # 打印的方式
            console = logging.StreamHandler()
            # 设置级别
            console.setLevel(logging.DEBUG)
            # 在处理器中添加格式器
            formatter = logging.Formatter(self.fmt)
            console.setFormatter(formatter)
            # 在日志器中添加处理器
            self.logger.addHandler(console)

    def info(self, msg):
        self.logger.info(str(msg))

    def error(self, msg):
        self.logger.error(str(msg))

    def warning(self, msg):
        self.logger.warning(str(msg))

'''

if __name__ == '__main__':
    logger = Logger().get_logger()
    logger.debug('调试')
    logger.info('信息')
    logger.warning('警告')
    logger.error('错误信息')
    logger.critical('致命的')












































