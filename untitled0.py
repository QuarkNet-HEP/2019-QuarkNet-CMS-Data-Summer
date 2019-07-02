#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:32:16 2019

@author: alecderwent
"""

import uproot
import numpy as np
import matplotlib.pyplot as plt
import math
import collections

file = uproot.open("ttbar.root")