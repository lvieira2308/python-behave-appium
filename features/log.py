import sys
import loguru

loguru.logger.remove()
loguru.logger.add(sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} - {message}")

def log_info(msg):
  loguru.logger.info(msg)

def log_warning(msg):
  loguru.logger.warning(msg)

def log_error(msg):
  loguru.logger.error(msg)

def log_debug(msg):
  loguru.logger.debug(msg)
