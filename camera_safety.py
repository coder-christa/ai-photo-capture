import cv2
import numpy as np
import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class Camera_safety:
     def __init__(self):
        self.PERSON_CLASS_ID = 1
        self.CONFIDENCE_THRESHOLD = 0.40 
        self.BASE_DIR = Path(__file__).resolve().parent
        ai_configs = os.path.join(self.BASE_DIR, "ai_configs")
        self.weights_path = "ai_configs/frozen_inference_graph.pb"
        self.config_path = "ai_configs/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        self.net = cv2.dnn.readNetFromTensorflow(self.weights_path, self.config_path)


     def enforce_mobilenet_privacy_blur(self,frame):
        h, w = frame.shape[:2]
    
        # Prepare the image blob for MobileNetV3 (Standard resizing and mean subtraction)
        blob = cv2.dnn.blobFromImage(frame, size=(320, 320), swapRB=True, crop=False) 
        self.net.setInput(blob)
        detections = self.net.forward()

        # Create the heavily blurred backdrop copy
        fully_blurred_frame = cv2.GaussianBlur(frame, (99, 99), 30)
        human_mask = np.zeros((h, w), dtype=np.uint8)
        person_detected = False

        # Loop through MobileNet detection matrix
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
        
            if confidence >= self.CONFIDENCE_THRESHOLD:
                class_id = int(detections[0, 0, i, 1])
            
                if class_id == self.PERSON_CLASS_ID:
                    person_detected = True
                
                    # MobileNet outputs normalized values (0.0 to 1.0), so scale them to your image size
                    x1 = int(detections[0, 0, i, 3] * w)
                    y1 = int(detections[0, 0, i, 4] * h)
                    x2 = int(detections[0, 0, i, 5] * w)
                    y2 = int(detections[0, 0, i, 6] * h)
                
                    # 2. Dynamically calculate padding based on photo resolution (e.g., 3%)
                    pad_w = int(w * 0.03)
                    pad_h = int(h * 0.03)

                    # 3. Add the adaptive safety margin padding 
                    x1  = max(0, x1 - pad_w)
                    y1 = max(0, y1 - pad_h)
                    x2 = min(w, x2 + pad_w)
                    y2 = min(h, y2 + pad_h)
                    # Mark the box to be blurred
                    cv2.rectangle(human_mask, (x1, y1), (x2, y2), 255, -1)

        if person_detected:
                logging.info("person detected in photo, masking photo")
                bgr_mask = cv2.cvtColor(human_mask, cv2.COLOR_GRAY2BGR)
                return np.where(bgr_mask == 255, fully_blurred_frame, frame)
    
        return frame
