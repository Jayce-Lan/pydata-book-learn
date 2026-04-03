import logging
import logging.config
import os
import sys

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_CONF = os.path.join(BASE_DIR, "logging.conf")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# 自动创建 logs 文件夹
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

class LoggerUtil:
    _inited = False

    @classmethod
    def get_logger(cls):
        # 获取调用者文件名
        frame = sys._getframe(1)
        filename = frame.f_code.co_filename
        logger_name = os.path.splitext(os.path.basename(filename))[0]

        if not cls._inited:
            logging.config.fileConfig(LOG_CONF)
            cls._inited = True

        return logging.getLogger(logger_name)

# 全局单例 log
log = LoggerUtil.get_logger()