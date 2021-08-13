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

SIZE_OF_DATA = 1024
SIZE_OF_COMMUNICATION = SIZE_OF_DATA*2

static_int_file_number = 0
folder = 0

dev = usb.core.find(idVendor=0x1fc9,idProduct=0x8a)
x1 = np.arange(0, SIZE_OF_DATA)
y = [0]*SIZE_OF_DATA
data = dev.read(0x0081,SIZE_OF_COMMUNICATION,1000)
#pdb.set_trace()

while(1):
    data = dev.read(0x0081,SIZE_OF_COMMUNICATION,1000)
    #print(data);
    #print("\n");

    cnt = 0
    ab2 = []        ##cnt < 64                                            ##stores the 100 lists before averaging
    while(cnt<1):
        ret = dev.read(0x0081,SIZE_OF_COMMUNICATION,10000)
        
        sret = [x for x in ret]

        new_list = [0]*(int(len(sret)/2))                       ##returned list

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
                
        ab = []                                                 ##list for inserting into file
        ab1 = []                                                ##list for plotting and inserting into avg list
        for i in new_list:
            ab.append(str(i))
            ab1.append(int(i)) ##(0.2+int(i)/6400)
        cnt = cnt + 1

        ab2.append(ab1)

    averaged_list = np.mean(ab2,axis=0)
    #pdb.set_trace()
    #p2p = np.max(averaged_list[10:128]) - np.min(averaged_list[10:128]);
    #f_p2p.write(str(p2p))
    #f_p2p.write("\n")
    #f_p2p.close()
    
    ##f.write("[")
    #for x in averaged_list:
    #    f.write(str(x)+",")
    #f.write(ab[len(ab)-1]+"]"+"\n")

    #f.close()
    y_plot = averaged_list
    #pdb.set_trace()
    plt.plot(x1,y_plot)
    plt.ylim(2250, 2750);
    plt.pause(.0005)
    plt.clf()

    plt.show(block=False)
