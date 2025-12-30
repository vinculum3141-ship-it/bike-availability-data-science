"""
Modeling Module

This module contains functions for training and evaluating ML models.

TODO: Implement the following functions:
- train_test_split_temporal() - Split data respecting temporal order
- train_baseline_model() - Train simple baseline model
- train_linear_model() - Train linear regression
- train_tree_model() - Train decision tree/random forest/XGBoost
- cross_validate_model() - Perform time-series cross-validation
- save_model() - Save trained model to disk
- load_model() - Load saved model

Example usage:
    from src.modeling import train_tree_model
    
    model = train_tree_model(X_train, y_train, model_type='xgboost')
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from typing import Tuple, Any, Optional
import joblib


# TODO: Implement modeling functions below
