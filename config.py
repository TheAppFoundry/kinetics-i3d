#!/usr/bin/env python

FRAME_DATA_PATH = '/trainingData/videos/frames'
NUM_GPUS = 1
CROP_SIZE = 224
NUM_CLASSES = 101
BATCH_SIZE = 1 # Regularly 3
NUM_FRAMES = 64 
FRAME_STRIDE = NUM_FRAMES
QUEUE_CAPACITY = 32

DROPOUT_KEEP_PROB = 0.5
MAX_ITER = 200 # This was regularly 100,000

CHECKPOINT_PATHS = {
    'rgb': 'data/checkpoints/rgb_scratch/model.ckpt',
    'flow': 'data/checkpoints/flow_scratch/model.ckpt',
    'rgb_imagenet': 'data/checkpoints/rgb_imagenet/model.ckpt',
    'flow_imagenet': 'data/checkpoints/flow_imagenet/model.ckpt',
}

LR = 0.01 # can change it to exponentially decay with global steps
TMPDIR = './tmp'
LOGDIR = './log'

TRAIN_DATA = 'train_data.txt'
VAL_DATA = 'val_data.txt'

DISPLAY_ITER = 100 
SAVE_ITER = 100 #How often it saves? normally 1000
VAL_ITER = 1000 #When it peforms validation?
THROUGH_PUT_ITER = 99

SAVER_MAX_TO_KEEP = 10
