import json
import hashlib
from datetime import datetime, timedelta
import logging
from datetime import datetime

def get_config(key):
    config_file = "D:/GITHUB/python_flask/config.json"
    file = open(config_file, "r")
    config = json.loads(file.read())
    file.close()
    
    if key in config:
        return config[key]
    else:
        raise Exception("Key {} is not found in config.json".format(key))
    

logging.basicConfig(
    filename='App_logging.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def logger(admin_user, action, details=""):
    log_message = f"Admin: {admin_user}, Action: {action}, Details: {details}"
    logging.info(log_message)
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warn message')
    logging.error('error message')
    logging.critical('critical message')
   

