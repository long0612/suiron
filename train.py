import sys, os
import json
import numpy as np

from suiron.utils.datasets import get_dataset
from suiron.core.SuironML import get_cnn_model 

# Load image settings
with open('settings.json') as d:
    SETTINGS = json.load(d)

# Our datasets
print('[!] Loading dataset...')
X = []
Y = []
#DATA_FILES = ['data/output_0.csv', 'data/output_1.csv', 'data/output_2.csv', 'data/output_3.csv', 'data/output_4.csv']
DATA_FILES = ['data/'+s for s in os.listdir('data')]
for d in DATA_FILES:
    c_x, c_y = get_dataset(d,width=SETTINGS['width'],height=SETTINGS['height'],depth=SETTINGS['depth'])
    X = X + c_x
    Y = Y + c_y

X = np.array(X)
Y = np.squeeze(np.array(Y))
print('X.shape = '+str(X.shape))
print('Y.shape = '+str(Y.shape))
print('[!] Finished loading dataset...')

# One NN for servo, one for motor
# for now, outputs = 10
servo_model = get_cnn_model(SETTINGS['cnn_name'], SETTINGS['width'], SETTINGS['height'], SETTINGS['depth'],out_dim=SETTINGS['out_dim'])

# Loads previous model if specified
if len(sys.argv) > 1:
    servo_model.load(sys.argv[1])

servo_model.fit({'input': X}, {'target': Y}, n_epoch=10000,
                validation_set=0.1, show_metric=True, snapshot_epoch=False,
                snapshot_step=10000, run_id=SETTINGS['cnn_name'])
servo_model.save(SETTINGS['cnn_name'] + '.ckpt')
