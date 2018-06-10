import pandas as pd
import numpy as np

def backtest_crossover(data, short_window=40, long_window=100):
    # Initialize the `signals` DataFrame with the `signal` column
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Create short simple moving average over the short window
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Create long simple moving average over the long window
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()
    
    return signals
    
def backtest_bollinger(data):
    signals = pd.DataFrame(index=data.index)
    signals['positions'] = 0.0
    
    # Compute medium band, 20-day moving average
    signals['mediumband'] = data['Close'].rolling(window=20, min_periods=1, center=False).mean()
    
    # Compute rolling standard deviation
    data_rstd = np.round(data['Close'].rolling(window = 20, center=False).std(), 2)
    
    # Compute upper band
    signals['upperband'] = signals['mediumband'] + 2 * data_rstd
    
    # Compute lower band
    signals['lowerband'] = signals['mediumband'] - 2 * data_rstd
    
    signals['positions'] = np.where(signals['upperband'] < data['High'], -1.0, signals['positions'])
    signals['positions'] = np.where(signals['lowerband'] > data['Low'], 1.0, signals['positions'])
    
    return signals
