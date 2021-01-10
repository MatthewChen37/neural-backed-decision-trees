# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 20:08:38 2021

@author: Matthew Chen
"""

import os
import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import Dataset


__all__ = names = ('NeuronData',)


class NeuronData(Dataset):
    
    
    def __init__(self, root="./data", *args, train=True, download=False, transform, **kwargs):
        super().__init__()
        dataset = None 
        
        if train:
            dataset = NeuronDataTrain(transform=transform)
        else:
            dataset = NeuronDataTest(transform=transform)
            
        self.dataset = dataset
        self.classes = self.dataset.classes
        self.root = root
        self.transform = transform
    
    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        return self.dataset[idx]
    

class NeuronDataTrain(datasets.ImageFolder):
    
    def __init__(self, transform, root='./data', *args, **kwargs):
        return super().__init__(os.path.join(root, 'NeuronData/train'), transform=transform, *args, **kwargs) 

class NeuronDataTest(datasets.ImageFolder):
    
    def __init__(self, transform, root='./data', *args, **kwargs):
        return super().__init__(os.path.join(root, 'NeuronData/test'), transform=transform, *args, **kwargs)

