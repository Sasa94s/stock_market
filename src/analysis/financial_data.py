#!/usr/bin/python3

import pandas as pd
from datetime import datetime
import quandl
from sqlalchemy import create_engine

def get_csv_data(symbol):
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

def stockdb_connect():
    """Connects to stock database"""

    # connecting to database
    postgres_engine = create_engine(
        'postgresql+psycopg2://analyst:p1p2p3p4p5@localhost:5432/stock')
    conn = postgres_engine.connect()

    # returning connection
    return conn

def stockdb_close(conn):
    """Closes connection to stock database"""
    conn.close()
    return True

def get_db_data(stmt):
    """Retrieves data from stock database"""

    # openning a connection
    conn = stockdb_connect()

    # executing query
    results = conn.execute(stmt).fetchall()

    # closing connection
    stockdb_close(conn)

    # storing results in a dataframe
    df = pd.DataFrame(results)
    df.columns = results[0].keys()

    # returning dataframe
    return df