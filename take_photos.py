from pathlib import Path
import logging
from configs.logging_settings import setup_logging, get_current_time
import sys
import argparse
from camera_management import Camera
from datetime import datetime

# This sets the base directory to the relative path of take_photos.py
# This prevents some amount of code breaking if the code base is moved
#Ideally, unless you have something specific in mind, keep all code base files together 
BASE_DIR = Path(__file__).resolve().parent
setup_logging(BASE_DIR)


logging.info(f"Application started: {get_current_time()}")


logging.info(f"initializing camera class {get_current_time()}")
camera = Camera()


# this block is for capturing a command line argument 
# this makes it easier to set a different directory for where photos are placed. 
# Create the directory then pass the new directory name when this executes. 
parser = argparse.ArgumentParser(description="Capture webcam photo and save to specified directory.")
parser.add_argument("output_dir", type=str, help="Directory to save the photo.")
arg = parser.parse_args()

#set the directory captured from the arugment
arg_dir = arg.output_dir
output_dir = BASE_DIR  / arg_dir

#sets the file name with a time stamp name for unique file names 
#This naming convention will also be used for sorting based on date/time in future updates
file_date = datetime.now().strftime("%Y%m%d_%H:%M:%S")
filename = f"app_{file_date}.jpg"

logging.info(f"Setting file name: app_{get_current_time()}.jpg and directory: {output_dir}")

#capture a photo
#log any errors that occur
#the capture function handles functions around getting a photo taken 
#see camera_management.py for further code details and comments
try:
    camera.capture(filename, output_dir)
except Exception as e:
    logging.info(f"Error occurred: {e} {get_current_time()}")
else: 
    logging.info(f"Photo taken. Success. {get_current_time()}")
