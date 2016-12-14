# Suiron
### Machine Learning for RC Cars 

## Prediction visualization (green = actual, blue = prediction)
![](https://thumbs.gfycat.com/DarlingForkedAcaciarat-size_restricted.gif)

## Click the video below to see it in action!
[![IMAGE ALT TEXT](http://img.youtube.com/vi/tFwCyHdAWf0/0.jpg)](https://youtu.be/tFwCyHdAWf0 "Machine Learning Car")

## Dependencies
#### __Python 2.7__ was chosen as it was supported by all the libraries used at the time
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-opencv python-dev

export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
sudo pip install --upgrade $TF_BINARY_URL

sudo pip install -r requirements.txt
```

#### For virtualenv, must create additional symlinks. Note that the main class in the python API is named cv2 to avoid the namespace collision with another package, and not an indication of version 2
```
ln -s /usr/lib/python2.7/dist-packages/cv2.so ~/env2.7/lib/python2.7/site-packages/cv2.so
ln -s /usr/lib/python2.7/dist-packages/cv.py ~/env2.7/lib/python2.7/site-packages/cv.py
ln -s /usr/lib/python2.7/dist-packages/cv.pyc ~/env2.7/lib/python2.7/site-packages/cv.pyc
python -c 'import cv2'
```

## Collecting data from usb camera. Data are stored under data/
```
python collect.py
```

## Collecting data from Cozmo, using a browser-based GUI
```
./remote_control_cozmo.py
```
* Once started, data are immediately collected. Click the 'Record' button at the top of the GUI to save recorded data to a file under data/


## Visualizing collected data
```
python visualize_collect.py data/foo.csv
```

## Training data. Trained models are foo_model.ckpt
```
vim settings.json # change training parameters, e.g. output model name, here
python train.py
```

* Troubleshooting training
** __~/env2.7/lib/python2.7/site-packages/tflearn/helpers/trainer.py@134, tf.train.Saver (tensorflow/tensorflow/python/training/saver.py): No variables to save__

    Set __allow_empty=True__ option in the Saver constructor (this seems to be new in TF).

## Visualizing predicted data
```
vim settings.json # choose the model to be used for prediction here
python visualize_predict.py data/foo.csv
```

# Closing the loop
```
./remote_control_cozmo.py
```
* Auto-drive can be toggled using the 'AUTODRIVE' button at the top of the GUI. NOTE: Drive commands (WASD) still need to be transmitted to Cozmo to actuate. However, their values are ignore. Instead, the outputs of DNN are used to drive and steer Cozmo.

# References

Blog Post detailing how the hardware and software communicate - [Communicating between RC Car and the On-board Computer - Jabelone](http://jabelone.com.au/blog/make-autonomous-car-code-included/)

Communication between hardware and software repo - [car-controller](https://github.com/jabelone/car-controller)

Neural Network architecture was based on NVIDIA's Self-driving car paper - [End-To-End Learning for Self-Driving Cars](https://arxiv.org/pdf/1604.07316v1.pdf)
