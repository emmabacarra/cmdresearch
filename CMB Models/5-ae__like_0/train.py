'''importing packages & necessary functions'''
import sys

import torch

sys.path.append('../')
from datasets import WMAP

# gpu
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

'''
======================================================================================================================================
'''
dataset_path = '../../../Local Data Files/WMAP/Datasets/SkymapK1_9yr_res9'

stochastic = False  # setting to False makes this deterministic (no sampling) - i.e. a normal autoencoder
batch_size = 100
train_split_percent = 0.8

image_channels=1  # setting to 1 since the images are grayscale
init_channels=8
kernel_size=14
padding=12
latent_dim=32
leak=0.99
drop=0.01

learning_rate = 1e-4
num_epochs = 150
save_every_n_epochs = 10
kl_weight = 1
weight_decay = 1e-10

latent_dims = (0, 1)  # dimensions to plot

def get_epochs(): # this is for comparison.ipynb
    return num_epochs

'''
======================================================================================================================================
'''

whole_dataset = WMAP(dataset_path)

# Import and run the generic training script
resume_timestamp = '09-09-24__19-51-23'     # set to None if training from start. example: '09-05-24__16-24-24'
resume_from_epoch = 30    # None if training from scratch/restarting
exec(open('../generic_trainer.py').read())

'''
======================================================================================================================================
'''
