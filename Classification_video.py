import sys
import cv2
import numpy as np
import os
from utils.cls_utils import load_yolo_model, load_cls_model, get_dog_location, preprocessing_image, get_results

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# set location
video = './video4.mkv'
output_video = './outputs/output4.avi'

# load models
yolo_model = load_yolo_model()
soft_model = load_cls_model()

# load video
cap = cv2.VideoCapture(video)

if not cap.isOpened():
    print("Video open failed!")
    sys.exit()

# save result video
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(output_video, fourcc, 20, (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

color = list(np.random.random(size=3) * 255) # set bbox color

# read video
while True:
    ret, frame = cap.read()

    
    if not ret:
        break
    
    df = get_dog_location(yolo_model, frame)
    
    # classification
    if len(df) == 0:
        pass
    
    else:
        for i in range(len(df)):
            dog_img = frame[int(df.iloc[i].y1) : int(df.iloc[i].y2), int(df.iloc[i].x1) : int(df.iloc[i].x2), :]
            
            resize_frame = preprocessing_image(dog_img)
            
            pred = soft_model.predict(resize_frame)[0]
            score, class_txt = get_results(pred)
            
            if score < 0.7: # classification result score threshold
                continue
            
            else:
                # draw bbox
                scale = max(frame.shape[0:2]) / 416
                line_width = int(2 * scale)
                
                cv2.rectangle(frame, (int(df.iloc[i].x1), int(df.iloc[i].y1)), (int(df.iloc[i].x2), int(df.iloc[i].y2)), color, line_width)
                
                text = f'{class_txt} {score:.2f}'
                font = cv2.FONT_HERSHEY_DUPLEX
                font_scale = max(0.3 * scale, 0.3)
                thickness = max(int(1 * scale), 1)
                
                (text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=thickness)[0]
                cv2.rectangle(frame, (int(df.iloc[i].x1) - line_width//2, int(df.iloc[i].y1) - text_height), (int(df.iloc[i].x1) + text_width, int(df.iloc[i].y1)), color, cv2.FILLED)
                cv2.putText(frame, text, (int(df.iloc[i].x1), int(df.iloc[i].y1)), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
                
    cv2.imshow('frame', frame)            
    out.write(frame)            
    
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()