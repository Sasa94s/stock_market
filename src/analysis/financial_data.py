#!/usr/bin/python3

import pandas as pd
from datetime import datetime
import quandl

def get_data(symbol):
    """Gets .csv data from quandl API by stock symbol
    Returns a dataframe"""

    # Setting start, end date
    start = "1970-01-01"
    end = datetime.utcnow().strftime('%Y-%m-%d')

    # Getting data from quandl
    data = quandl.get("WIKI/%s" % symbol, start_date=start, end_date=end)
    return data

def get_local_data(symbol, path):
    """Gets .csv data from local source
    Returns a dataframe"""

    data = pd.read_csv('%s/%s.csv' % (path,symbol), index_col='Date', parse_dates=True)
    return data