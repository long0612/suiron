import numpy as np

#Map function from arduino
def arduino_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Converts raw values to target (Y) values
# for the convolutional neural network
def raw_to_cnn(y, min_arduino=-150.0, max_arduino=150.0):
    # Map from R to -1,1
    # Conversion because output activation is tanh
    y_ = arduino_map(y, min_arduino, max_arduino, -1.0, 1.0)
    return [y_] 

# Converts convolutional neural network outputs 
# to raw outputs
def cnn_to_raw(y, min_arduino=-150.0, max_arduino=150.0):
    # Get highest index value and map
    # it back
    y_ = y[np.argmax(y)]

    # degrees to output
    y_ = arduino_map(y_, -1.0, 1.0, min_arduino, max_arduino)

    return y_

# Motor to RGB color based on speed
def raw_motor_to_rgb(x):
    if x <= 90:
        if x < 70:
            return (255, 0, 0)        
        elif x < 80:
            return (255, 165, 0)
        else:
            return (0, 255, 0)
    elif x > 90:
        if x > 120:
            return (255, 0, 0)
        elif x > 110:
            return (255, 165, 0)
        else:
            return (0, 255, 0)
