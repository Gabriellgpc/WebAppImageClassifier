from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import decode_predictions

from utils import tf_imread, tf_decode_image


class ImageNetClassifier():
    model = None    
    
    @classmethod
    def get_model(cls):
        if cls.model == None:
            cls.model = EfficientNetB0(weights='imagenet')
        return cls.model
    
    @classmethod
    def predict(cls, input):
        model = cls.get_model()
        pred = model.predict(input)
        pred_decod = decode_predictions(pred)
        pred_class = pred_decod[0][0][1]
        pred_conf  = pred_decod[0][0][2]
        return (pred_class, pred_conf)   

