import sys
import json
import numpy as np

import tensorflow as tf

from suiron.utils.file_finder import get_latest_filename
from suiron.core.SuironML import get_cnn_model, get_nn_model
from suiron.core.SuironVZ import visualize_data

# Image settings
with open('settings.json') as d:
    SETTINGS = json.load(d)


# Load up our CNN
cnn_model = None
cnn_model = get_cnn_model(SETTINGS['cnn_name'], SETTINGS['width'], SETTINGS['height'], SETTINGS['depth'], SETTINGS['out_dim'])
try:    
    cnn_model.load(SETTINGS['cnn_name'] + '.ckpt')
except Exception as e:
    print(e)
    
# If we specified which file
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    # Visualize latest filename
    filename = get_latest_filename() 

# Visualize it
visualize_data(filename, SETTINGS['width'], SETTINGS['height'], SETTINGS['depth'], cnn_model=cnn_model)
