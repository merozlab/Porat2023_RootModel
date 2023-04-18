#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:58:49 2023

@author: Mathieu Riviere

This is a minimal piece of code to read the experimental data used
in "A quantitative model for spatio-temporal dynamics of root gravitropism" by
Porat et al. (2023) and stored in 'experimental_data_Porat2023.pkl'

"""

import _pickle as pkl

#%%

def load_experimental_data(input_path):

    with open(input_path, 'rb') as f:
        dictin = pkl.load(f, encoding='latin1')

    t = dictin['t']     # array, time (h)
    all_theta_tip = dictin['all_theta_tip']     # array, each row contains theta_tip(t) for a single root (rad)
    all_theta_base = dictin['all_theta_base']    # array, each row contains theta_base(t) for a single root (rad)
    all_R = dictin['all_R']     # array, radius of each root (mm)
    all_vg = dictin['all_vg']   # array, average tip velocity for each root (mm/h)
    all_maxDelta = dictin['all_maxDelta']   # array, maximum gravitropic response for each root (dimensionless)
    all_Lgz = dictin['all_Lgz'] # array, estimated growth zone length for each root (mm/h)

    return t, all_theta_tip, all_theta_base, all_R, all_vg, all_maxDelta, all_Lgz


#%%

input_path = './experimental_data_Porat2023.pkl'

t, all_theta_tip, all_theta_base, all_R, all_vg, all_maxDelta, all_Lgz = load_experimental_data(input_path)