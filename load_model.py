import tensorflow as tf
import numpy as np

#import sys


X_test = np.genfromtxt('X_test.csv', delimiter=',')
model = tf.keras.models.load_model('my_model_80_5000.h5')
output_data = model.predict(X_test[0].reshape(1,-1))
print(output_data[0])