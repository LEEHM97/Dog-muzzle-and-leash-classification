import tensorflow as tf
import cv2
import numpy as np
from YOLO.models import Yolov4

from tensorflow.keras.layers import Dense, Flatten, GlobalAveragePooling2D
from tensorflow.keras.models import load_model
from tensorflow.keras import Model



# load yolov4 model
def load_yolo_model():
    yolo_model = Yolov4(weight_path='./YOLO/yolov4.weights',
                class_name_path='./YOLO/class_names/coco_classes.txt')
    return yolo_model

# load classification model (MobileNetV2)
def load_cls_model():
    MobileNetV2Model= tf.keras.applications.MobileNetV2(
        input_shape=(224,224,3),
        include_top=False,
        weights="imagenet",
        input_tensor=None,
        pooling=None)
    x = GlobalAveragePooling2D()(MobileNetV2Model.output)
    x = Flatten()(x)
    x = Dense(256, activation="relu")(x)
    predictions = Dense(3, activation='softmax', name = "output_node")(x)
    model = Model(inputs=MobileNetV2Model.input, outputs=predictions)

    soft_model = load_model('./MobileNetV2-107-0.2315-0.9500.hdf5')
    return soft_model

# get dog location in one frame
def get_dog_location(model, frame):
    df = model.predict_img(frame)
    
    # set dog score threshold
    df = df[df.score>0.5]
    return df

# preprocessing image to input MobileNetV2 model
def preprocessing_image(img):
    resize_img = cv2.resize(img, (224, 224))
    img_array_expanded_dims = np.expand_dims(resize_img, axis=0)
    return tf.keras.applications.mobilenet_v2.preprocess_input(img_array_expanded_dims)


# get iamge classification results
def get_results(pred):
    if pred[0] > 0.7 and pred[1] > 0.7:
        class_txt = "leash_muzzle"
        score = (pred[0]+pred[1]) / 2
    
    else:
        class_num = pred.argmax(axis=-1)
        score = pred.max()
        
        if class_num == 0:
            class_txt = "leash"
        elif class_num == 1:
            class_txt = "muzzle"
        else:
            class_txt = "nothing"
    
    return score, class_txt