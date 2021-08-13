# Wearable-Multimodal-Optical-and-Acoustic-Sensing-of-Physiological-Parameters-Autoencoder



#### Director: [Professor Sri-Rajasekhar (Raj) Kothapalli](https://www.bme.psu.edu/department/directory-detail-g.aspx?q=szk416) & PHD. SUMIT AGRAWAL
#### Range: 05/2021 - 08/2021
###### Only includes code 

Aurther: Hongshuo Wang


How to check the storage of the pi:
cmd: df

how to run the trained tensorflow-lite model:

1. open the command windows

2. type cmd: cd /home/pi/tflite1 (go to the tflite1 directory)

3. type cmd: source tflite-env/bin/activate (activate python visual-envir)

4. type cmd: jupyter notebook (open jupyter notebook)
	* demo2.ipynb (short demo to show the final workout)
	* load_lite_model_new.py (testing tensorflow lite model on testing set)
	* measure_running_speed.ipynb (compare normal tensorflow model vs tensorflow lite model in running speed)
	* Plotter_test.py (live demo on input streaming signal)
	* X_test.csv (X value)
	* y_test.csv (y value)
	* converted_model.tflite (converted tensorflow lite model)
	* my_model_80_5000.h5 (og version of tensorflow model)

how display live data(running Plotter_test.py or Plotter_test_og)

1. open the command windows

2. type cmd: cd /home/pi/tflite1 (go to the tflite1 directory)

3. type cmd: sudo thonny Plotter_test_og.py
	or
   type cmd: sudo thonny Plotter_test.py

4. click run(green) icon

How to train the tensorflow model using given X and y 

How to convert h5 trained weight to tensorflow-lite version

look at my github repo: https://github.com/whsair/Wearable-Multimodal-Team-1




