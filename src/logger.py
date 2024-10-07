#This code is setting up a logging system,to track events that happen during the execution

import logging
import os
from datetime import datetime

# Creating a unique log file name based on the current timestamp
log_file_name = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# Defining the path for storing the log files inside a 'logs' folder in the current directory
log_directory = os.path.join(os.getcwd(), "logs", log_file_name)

# Creating the 'logs' folder if it doesn't already exist
os.makedirs(log_directory, exist_ok=True)

# log file path
log_file_path = os.path.join(log_directory, log_file_name)

# Configuring logging to write logs to the specified file and format the log messages
logging.basicConfig(
    filename=log_file_path,  # Location of the log file
    format="[%(asctime)s] Line: %(lineno)d | Logger: %(name)s | Level: %(levelname)s - %(message)s",  # Log format
    level=logging.INFO,  
)

# if __name__ == '__main__':
#     logging.info("Logging started")
    