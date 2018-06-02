#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def preprocessing(df):
    """Preprocesses data by filling missing values"""
    # Forward and Backward filling missing values
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

def daily_return(series):
    """Computes Daily log return"""
    daily_log_returns = np.log(series / series.shift(1))
    return daily_log_returns

def monthly_return(series):
    """Computes Monthly log return"""
    # Resample `stock` to business months, take last observation as value 
    monthly = series.resample('BM').apply(lambda x: x[-1])

    # Calculate the monthly percentage change
    monthly.pct_change()
    return monthly

def quarter_return(series):
    """Computes Quarter log return"""
    # Resample `stock` to quarters, take the mean as value per quarter
    quarter = series.resample("4M").mean()

    # Calculate the quarterly percentage change
    quarter.pct_change()
    return quarter

def cum_return(series):
    """Computes Cumulative daily return"""
    daily_pct_change = daily_return(series)
    cum_daily_return = (1 + daily_pct_change).cumprod()
    return cum_daily_return

def monthly_cum_return(series):
    """Computes Cumulative monthly return"""
    cum_daily_return = cum_return(series)
    # Resample the cumulative daily return to cumulative monthly return 
    cum_monthly_return = cum_daily_return.resample("M").mean()
    return cum_monthly_return

