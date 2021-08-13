# Wearable-Multimodal-Optical-and-Acoustic-Sensing-of-Physiological-Parameters-Autoencoder

### Aurther: Hongshuo Wang

#### Director: [Professor Sri-Rajasekhar (Raj) Kothapalli](https://www.bme.psu.edu/department/directory-detail-g.aspx?q=szk416) & PHD. SUMIT AGRAWAL
#### Range: 05/2021 - 08/2021
###### Only includes code 

## Installed packages
- numpy
- scipy
- pdb
- pyusb
- sklearn
- matplotlib
- [tflite_runtime](https://www.tensorflow.org/lite/guide/python#learn_more) (during running)
- tensorflow 2.x (training)




## Instruction on lab Pi


#### How to check the storage of the pi:

``` bash
df
```

#### How to run the trained tensorflow-lite model:

1. open the command windows

2. type cmd  (go to the tflite1 directory): 
```bash
cd /home/pi/tflite1
```

3. type cmd (activate python visual-envir): 
```bash
source tflite-env/bin/activate 
```

4. type cmd: jupyter notebook (open jupyter notebook)
	* demo2.ipynb (short demo to show the final workout)
	* load_lite_model_new.py (testing tensorflow lite model on testing set)
	* measure_running_speed.ipynb (compare normal tensorflow model vs tensorflow lite model in running speed)
	* Plotter_test.py (live demo on input streaming signal)
	* X_test.csv (X value)
	* y_test.csv (y value)
	* converted_model.tflite (converted tensorflow lite model)
	* my_model_80_5000.h5 (og version of tensorflow model)




#### How display live data(running Plotter_test.py or Plotter_test_og)

1. open the command windows

2. type cmd (go to the tflite1 directory): 
```bash
cd /home/pi/tflite1 
```

3. type cmd: 
```bash
sudo thonny Plotter_test_og.py
sudo thonny Plotter_test.py
```

4. click run(green) icon




#### How to train the tensorflow model using given X and y 
	
- run [training_data.ipynb](https://github.com/whsair/Wearable-Multimodal-Optical-and-Acoustic-Sensing-of-Physiological-Parameters-Autoencoder-/blob/main/training_data.ipynb)

#### How to convert h5 trained weight to tensorflow-lite version

- run [generate_tf_lite_model.py](https://github.com/whsair/Wearable-Multimodal-Optical-and-Acoustic-Sensing-of-Physiological-Parameters-Autoencoder-/blob/main/generate_tf_lite_model.py)

#### How to compare the results between lite model and og model

- run [measure_running_speed.ipynb](https://github.com/whsair/Wearable-Multimodal-Optical-and-Acoustic-Sensing-of-Physiological-Parameters-Autoencoder-/blob/main/measure_running_speed.ipynb) 




