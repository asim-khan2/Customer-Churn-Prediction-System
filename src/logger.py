import logging 
import os
from datetime import datetime

FILE_PATH = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

logs_file = os.path.join(os.getcwd(),'logs')

os.makedirs(logs_file,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_file,FILE_PATH)

logging.basicConfig(
    level=logging.DEBUG,
    filename=LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s ",

)

