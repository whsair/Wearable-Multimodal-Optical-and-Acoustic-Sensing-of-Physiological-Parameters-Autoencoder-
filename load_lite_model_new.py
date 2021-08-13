from tflite_runtime.interpreter import Interpreter
import numpy as np
#import sys


X_test = np.genfromtxt('X_test.csv', delimiter=',')
interpreter = Interpreter(model_path="converted_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print(X_test)
print(X_test.shape)
print(X_test[0])
print(input_details)

input_data = np.array([X_test[0]], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)

 
