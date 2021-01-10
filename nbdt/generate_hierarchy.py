# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 23:23:44 2021

@author: Matthew Chen
"""

from nbdt import models

from nbdt.models import wrn28_10_cifar10
from nbdt.hierarchy import generate_hierarchy

model = wrn28_10_cifar10(pretrained=True)
generate_hierarchy(dataset='NeuronData', arch='wrn28_10_cifar10', model=model, method='random')