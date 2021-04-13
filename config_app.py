import logging
import logging.handlers
import os
import time

# 绝对路径
BAS_URL = os.path.abspath(os.path.dirname(__file__))

def logging_rizhi(name='log'):
    time_int = int(time.time()*10000)
    # 创建日志器对象
    rizhiqi = logging.getLogger()
    rizhiqi.setLevel(level=logging.INFO)
    # 创建处理器（按时间切割日志文件）
    lht = logging.handlers.TimedRotatingFileHandler(BAS_URL + '/log/' + name + time_int + '.log',when='M',interval=1,backupCount=2)
    ls = logging.StreamHandler()
    # 创建格式化器对象
    fmt_name = '%(asctime)s %(levelname)s [%(name)s] ' \
               '[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt_name)
    # 给处理器设置格式化器
    lht.setFormatter(formatter)
    # 给日志器添加处理器
    rizhiqi.addHandler(lht)
    rizhiqi.addHandler(ls)