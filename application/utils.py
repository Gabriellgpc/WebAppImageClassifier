import tensorflow as tf


def tf_imread(filename, target_size):
    content = tf.io.read_file(filename)
    image = tf_decode_image(content)
    image = tf.image.resize(image, size=target_size)
    return image
    
def tf_decode_image(content):
    image = tf.image.decode_image(content)
    image = tf.expand_dims(image, axis=0)
    return image

def tf_imwrite(filename, image_tf):
    content = tf.image.encode_png(image_tf)
    tf.io.write_file(filename, content)
