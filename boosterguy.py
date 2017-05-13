#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:39:56 2017

@author: Pranavtadepalli
"""

import xgboost as xgb
# read in data
dtrain = xgb.DMatrix([1,1,1,2,3,4,5,3])
dtest = xgb.DMatrix([1,1,7,3,5,3,5,3])
# specify parameters via map
param = {'booster': 'dart',
         'max_depth': 5, 'learning_rate': 0.1,
         'objective': 'binary:logistic', 'silent': True,
         'sample_type': 'uniform',
         'normalize_type': 'tree',
         'rate_drop': 0.1,
         'skip_drop': 0.5}
num_round = 50
bst = xgb.train(param, dtrain, num_round)
# make prediction
# ntree_limit must not be 0
preds = bst.predict(dtest, ntree_limit=num_round)
print(preds)