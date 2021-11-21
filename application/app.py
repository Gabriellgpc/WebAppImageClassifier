import os
from flask import Flask
from flask import request
from flask import render_template

from image_classifier import ImageNetClassifier
from utils import tf_imread, tf_decode_image, tf_imwrite

UPLOAD_FOLDER = '/home/condados/workarea/saturday-projects/WebAppImageClassifier/application/static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    ext = filename.rsplit('.')[-1].lower()
    return (ext in ALLOWED_EXTENSIONS) and ('.' in filename)

@app.route('/', methods=['GET', 'POST'])
def home():
   
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            if allowed_file(image_file.filename):
                image_loc = os.path.join(
                    UPLOAD_FOLDER,
                    image_file.filename
                    )
                image_file.save(image_loc)
                
                input_image = tf_imread(image_loc, target_size=[224,224])
                pred_class, pred_conf = ImageNetClassifier.predict(input_image)

                return render_template('index.html', 
                                       prediction_class=pred_class, 
                                       prediction_confidence=pred_conf,
                                       image_loc=image_file.filename)
                
                # Load the image from raw data
                
                # image_data = image_file.stream.read()
                # image = tf_decode_image(image_data)
                # print(image.shape)
                # tf_imwrite('uploaded_image.png', image[0])
            else:
                # WARNING
                # Image file type not allowed
                pass
    
    return render_template('index.html', 
                           prediction_class="N/A", 
                           prediction_confidence="N/A",
                           image_loc=None)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
