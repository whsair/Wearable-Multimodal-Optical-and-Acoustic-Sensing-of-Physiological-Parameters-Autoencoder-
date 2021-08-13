import sys
sys.path.append('/home/pi/.local/lib/python3.7/site-packages/')
import matplotlib.pyplot as plt
import numpy as np
import usb.core
import usb.util
import numpy as np
import scipy.signal
import os
import pdb
import time
from tflite_runtime.interpreter import Interpreter
import numpy as np
from sklearn import preprocessing
#load tensorflow lite model
interpreter = Interpreter(model_path="converted_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()



SIZE_OF_DATA = 1024
SIZE_OF_COMMUNICATION = SIZE_OF_DATA*2

static_int_file_number = 0
folder = 0

dev = usb.core.find(idVendor=0x1fc9,idProduct=0x8a)
x1 = np.arange(0, SIZE_OF_DATA)
x1_new = np.arange(0, 3832)
y = [0]*SIZE_OF_DATA
data = dev.read(0x0081,SIZE_OF_COMMUNICATION,10000)
#pdb.set_trace()

while (1):
    
    data = dev.read(0x0081,SIZE_OF_COMMUNICATION,10000)
    print(data);
    print("\n");

    cnt = 0
    ab2 = []      ##cnt < 64
    while(cnt<100):
        ret = dev.read(0x0081,SIZE_OF_COMMUNICATION,10000) #input size 2048

        sret = [x for x in ret] #make list

        new_list = [0]*(int(len(sret)/2)) #create a new list with 1024 size

        i = 2 
        while i < len(sret):
            iby2 = int(i/2);
            computed = str((sret[i] + (sret[i+1]<<8)))
            i += 2
            new_list[iby2] = computed
            if(int(computed) < 32768):
                new_list[iby2] = int(computed)
            else:
                new_list[iby2] = new_list[iby2 - 1]

        ab = []           ##list for inserting into file
        ab1 = []          ##list for plotting and inserting into avg list
        for i in new_list:
            ab.append(str(i))
            ab1.append(int(i)) ##(0.2+int(i)/6400)
        cnt = cnt + 1
        #print(ab1)
        #print(len(ab1))
        ab2.append(ab1)
    
    #ab2 = np.random.randn(1,1024).tolist()
    #print(ab2)
    #print(len(ab2))
        
    #machine learning
    #X_test = np.genfromtxt('X_test.csv', delimiter=',')
    
    new_ab2 = ab2[0].copy()
    
    new_ab2 = new_ab2 + (3832 - SIZE_OF_DATA)*[0]#np.mean(new_ab2)]
    
    
    #new_ab2 = np.mean(ab2,axis=0)
    
    input_data = np.array([new_ab2], dtype=np.float32)
    input_data = preprocessing.normalize(input_data)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    new_ab2 = interpreter.get_tensor(output_details[0]['index'])
    
    #averaged_list = new_ab2
    averaged_list = np.mean(ab2,axis=0)
    #averaged_list = preprocessing.normalize(averaged_list.reshape(-1,1))
    
    #pdb.set_trace()
    #p2p = np.max(average_list[10:128]) - np.min(average_list[10:128]);
    #f_p2p.write(str(p2p))
    #f_p2p.write("\n")
    #f_p2p.close()

    #f.write("[")
    #for x in average_list:
     #    f.write(str(x)+",")
    #f.write(ab[len(ab)-1]+"]"+"\n")

    #f.close()
    y_plot_new = new_ab2[0]
    y_plot = averaged_list
    
    #pdb.set_trace()
    plt.plot(x1,ab2[0][:1024],'r')
    
    plt.plot(x1,y_plot_new[:1024],'b')
    plt.pause(.0005)
    plt.clf()

    plt.show(block=False)
