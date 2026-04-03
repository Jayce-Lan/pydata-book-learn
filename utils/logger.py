import logging
import logging.config
import os
import sys

# 自动获取项目根目录（utils 上一级）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_CONF_PATH = os.path.join(BASE_DIR, "logging.conf")

class Logger:
    _inited = False

    @staticmethod
    def get_logger():
        # 自动获取调用者文件名做 logger 名称
        frame = sys._getframe(1)
        filename = frame.f_code.co_filename
        logger_name = os.path.splitext(os.path.basename(filename))[0]

        if not Logger._inited:
            if os.path.exists(LOG_CONF_PATH):
                logging.config.fileConfig(LOG_CONF_PATH)
            else:
                # 没有配置文件时用默认配置
                logging.basicConfig(
                    level=logging.INFO,
                    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
                )
            Logger._inited = True

        return logging.getLogger(logger_name)

# 简化调用
log = Logger.get_logger()