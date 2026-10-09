import cv2
import numpy as np
import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class Camera_safety:
     def __init__(self):
        #these variables are for setting the directory structure and pointing to the model config files
        self.BASE_DIR = Path(__file__).resolve().parent
        ai_configs = os.path.join(self.BASE_DIR, "ai_configs")
        self.weights_path = "ai_configs/frozen_inference_graph.pb"
        self.config_path = "ai_configs/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"


        #photo model parameters:
        self.PERSON_CLASS_ID = 1
        self.CONFIDENCE_THRESHOLD = 0.40 
        base_net = cv2.dnn.readNetFromTensorflow(self.weights_path, self.config_path)
        self.model = cv2.dnn_DetectionModel(base_net)
                
        self.model.setInputParams(
            size=(320, 320), 
            scale=1.0 / 127.5, 
            mean=(127.5, 127.5, 127.5), 
            swapRB=True,
            crop=False
        )


     def enforce_mobilenet_privacy_blur(self,frame):
        h, w = frame.shape[:2]
    
        # Prepare the image blob for MobileNetV3 (Standard resizing and mean subtraction)
        blob = cv2.dnn.blobFromImage(frame, size=(320, 320), swapRB=True, crop=False) 
        # Create the heavily blurred backdrop copy
        fully_blurred_frame = cv2.GaussianBlur(frame, (99, 99), 30)
        human_mask = np.zeros((h, w), dtype=np.uint8)
        person_detected = False

        class_ids, confidences, boxes = self.model.detect(
            frame, 
            confThreshold=self.CONFIDENCE_THRESHOLD
        )

        if len(class_ids) == 0:
            return frame

# Loop directly through the objects list
        for class_id, confidence, box in zip(class_ids.flatten(), confidences.flatten(), boxes):
             if class_id == self.PERSON_CLASS_ID:
                person_detected = True
                
                # MobileNet outputs normalized values (0.0 to 1.0), so scale them to your image size
                bx, by, bw, bh = box
                x1, y1 = bx, by
                x2, y2 = bx + bw, by + bh
                
                # Dynamic 3% safety buffer logic matching your target stream dimensions
                pad_w = int(w * 0.03)
                pad_h = int(h * 0.03)

                x1 = max(0, x1 - pad_w)
                y1 = max(0, y1 - pad_h)
                x2 = min(w, x2 + pad_w)
                y2 = min(h, y2 + pad_h)
                cv2.rectangle(human_mask, (x1, y1), (x2, y2), 255, -1)

        if person_detected:
                logging.info("person detected in photo, masking photo")
                bgr_mask = cv2.cvtColor(human_mask, cv2.COLOR_GRAY2BGR)
                return np.where(bgr_mask == 255, fully_blurred_frame, frame)
    
        return frame
