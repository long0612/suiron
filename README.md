# Suiron for Cozmo
### Vision-based, autonomous driving for Cozmo

<!--
### Prediction visualization (green = actual, blue = prediction)
![](https://thumbs.gfycat.com/DarlingForkedAcaciarat-size_restricted.gif)

### Click the video below to see it in action!
[![IMAGE ALT TEXT](http://img.youtube.com/vi/tFwCyHdAWf0/0.jpg)](https://youtu.be/tFwCyHdAWf0 "Machine Learning Car")
-->

## Dependencies

### Virtual Python environment
* To setup a virtual python environment, see https://sites.google.com/site/longle1illinois/blog/settinguppython34devinubuntu
* For virtualenv, must create additional symlinks. Note that the main class in the python API is named cv2 to avoid the namespace collision with another package, and not an indication of version 2
```
ln -s /usr/lib/python2.7/dist-packages/cv2.so ~/env2.7/lib/python2.7/site-packages/cv2.so
ln -s /usr/lib/python2.7/dist-packages/cv.py ~/env2.7/lib/python2.7/site-packages/cv.py
ln -s /usr/lib/python2.7/dist-packages/cv.pyc ~/env2.7/lib/python2.7/site-packages/cv.pyc
python -c 'import cv2'
```

### __Python 2.7__ is needed on the Suiron end
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-opencv python-dev

export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
pip install --upgrade $TF_BINARY_URL

pip install -r requirements.txt
```

### __Python 3.5__ is needed to use the Cozmo API
```
pip install cozmo[camera]
```
* For full setup instructions, see http://cozmosdk.anki.com/docs/install-linux.html
* *remote_control_cozmo.py* must be run in Python 3.5


## Collecting data from a USB camera (using OpenCV)
```
python collect.py
```
* Data are stored as *data/output_foo.csv*

## Collecting data from Cozmo (using a browser-based GUI)
```
./remote_control_cozmo.py
```
* Once started, data are immediately collected into a memory buffer. Click the *Record* button at the top of the GUI to save buffered data to a file as *data/cozmoData_foo.csv*. The buffer is then reset and data collection continues.


## Visualizing collected data
```
python visualize_collect.py data/cozmoData_foo.csv
```
* Press *q* to quit the visualization at anytime

## Training
```
vim settings.json # change training parameters, including output model name, here
python train.py
```
* All data under *data/* are used for training/testing/validation. Let *foo.ckpt* be a trained model.
* Exception *~/env2.7/lib/python2.7/site-packages/tflearn/helpers/trainer.py@134, tf.train.Saver (tensorflow/tensorflow/python/training/saver.py): No variables to save*. 
  * Set *allow_empty=True* option in the Saver constructor (this is new in tf, resulting in a bug in tflearn).

## Visualizing the predicted data
```
vim settings.json # choose the model to be used for prediction here
python visualize_predict.py data/foo.csv
```
* A *foo.gif* is generated at the end or on termination of the visualizer.

## Closing the loop
```
./remote_control_cozmo.py
```
* Auto-drive can be toggled using the 'AUTODRIVE' button at the top of the GUI. NOTE: Drive commands (WASD) still need to be transmitted to Cozmo for actuation. However, their values are ignore. Instead, the outputs of DNN are used to drive and steer Cozmo.

# References

Blog Post detailing how the hardware and software communicate - [Communicating between RC Car and the On-board Computer - Jabelone](http://jabelone.com.au/blog/make-autonomous-car-code-included/)

Communication between hardware and software repo - [car-controller](https://github.com/jabelone/car-controller)

Neural Network architecture was based on NVIDIA's Self-driving car paper - [End-To-End Learning for Self-Driving Cars](https://arxiv.org/pdf/1604.07316v1.pdf)
