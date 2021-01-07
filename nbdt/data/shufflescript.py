# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:12:22 2021

@author: Matthew Chen
"""


import shutil, random, os


def shuffle_images(image_class):
    dirpath = '../../data/NeuronData/' + image_class + '/'
    destDirectory = '../../data/NeuronData/' + image_class + '_test/'
    
    filenames = random.sample(os.listdir(dirpath), 50)
    for fname in filenames:
        srcpath = os.path.join(dirpath, fname)
        shutil.move(srcpath, destDirectory + fname)


shuffle_images("visam")
shuffle_images("visp")
    