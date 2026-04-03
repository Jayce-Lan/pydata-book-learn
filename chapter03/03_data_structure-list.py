import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import log

log.info("This is a log message from 03_data_structure-list.py")