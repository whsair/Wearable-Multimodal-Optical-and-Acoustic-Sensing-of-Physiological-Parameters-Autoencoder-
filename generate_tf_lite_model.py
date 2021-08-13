
import tensorflow as tf
from tensorflow import keras



model = tf.keras.models.load_model('my_model_80_5000.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)