
#This class is intended for multithreaded purposes in the future.
#It's taking into account large numbers of photos that will be dumped and processed
#the locking/release of the device is to prevent crashes and conflicts 
#when multiple threads come into play
#some of this isn't in use and intended for future proofing as I merge in more code.

import cv2
import time
import threading
import os
import logging

logger = logging.getLogger(__name__)
#initiate the class
class Camera:
    def __init__(self, device_index=0):
        self.device_index = device_index
        self.camera = None
        self.lock = threading.Lock()

#initiate the camera
    def init_camera(self):
        if self.camera is None:
            self.camera = cv2.VideoCapture(self.device_index)
            cam = self.camera 
        if not cam.isOpened():
            raise RuntimeError("Camera could not be opened")

#capture the camera state and time when the camera was last accessed
# this function is currently unused but will be used in the future
    def get_camera_state(self):
        camera_lock = threading.Lock()
        last_used = time.time()
 
 
 #lock the device to prevent multiple threads accessing at once
 #Initialize the camera
 #warm up the camera until it's ready
 #capture a photo
 #raise an error if unable to capture photo 
 #if no error write to the specified directory
 #release the lock to prevent potential crashes/corruption if it wasn't already released
    def capture(self, filename, output_dir):
        try:
            with self.lock:
                self.init_camera()
                self.wait_until_ready()
                ret, frame = self.camera.read()
                if not ret:
                    raise RuntimeError("Failed to capture frame")
                else:
                    cv2.imwrite(f"{output_dir}/{filename}", frame)
        finally:
            self.release()

#this is called by the capture function
#it takes dummy photos that aren't stored until a good one is detected
#If a usable photo isn't captured before the timeout, it raises an error 
#The timeout prevents an infinite loop if the camera can't get a good photo
    def wait_until_ready(self, timeout=5):
        start = time.time()
        ret, frame = self.camera.read()
        if ret and frame is not None:
            if frame.mean() != 0.0:
                return frame
        
        if time.time() - start > timeout:
            raise RuntimeError("Camera never became ready")

        time.sleep(0.1)

#releases locks on the camera to minimize crashes and corruption
#can be called to force a release of a lock
#this cam be called if a finished thread doesn't release it's lock nicely.
    def release(self):
        if self.camera:
            self.camera.release()
            self.camera = None

#checks if the camera is ready and initialized properly(not in use currently)
#future proofing with multiple threads in mind 
#this can be used if it's ambiguous if the camera was initialized
#it can also help with debugging
    def is_ready(self):
        return self.camera is not None and self.camera.isOpened()