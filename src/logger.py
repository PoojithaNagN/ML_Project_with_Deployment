# For the purpose of this project, we will use the logging module to log the messages    
import logging
import os
from datetime import datetime

# Create a logger
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_DIR = os.path.join(os.getcwd(), "logs")  # Directory for logs
os.makedirs(LOG_DIR, exist_ok=True)  # Create the directory if it doesn't exist

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)  # Full path to the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d' %(name)s- %(levelname)s - %(message)s",
    level=logging.INFO,
)

   