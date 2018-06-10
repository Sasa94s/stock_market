#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import Figure, output_file, show, save
from bokeh.io import push_notebook, show, output_notebook
from bokeh.models import HoverTool, ColumnDataSource
import financial_statistics

def plot_prices(df, template_name='stock', notebook=False, x='Date', y='Adj. Close', title="Stock prices", xlabel="Date", ylabel="Price"):
    """
    Bokeh Plot for stock prices with a custom title and meaningful axis labels.
    template_name: output file name of plot
    notebook: boolean for showing plot on jupyter notebook
    """
    source = ColumnDataSource(df)
    # create a new plot with a title and axis labels
    p = Figure(title=title,
               x_axis_label=xlabel,
               y_axis_label=ylabel,
               x_axis_type='datetime',
               plot_height=500,
               plot_width=950,
               tools=['pan','wheel_zoom'],
               toolbar_location='below',)
   
    # configure so that Bokeh chooses what (if any) scroll tool is active
    p.toolbar.active_scroll = "auto"
    
    # add a line renderer with legend and line thickness
    p.line(x=x, y=y, line_width=2, legend='Adj Close', source=source)
    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    hover = HoverTool(
        tooltips=[
            ( 'Date',   '@Date{%F}'            ),
            ( 'Close',  '$@{Adj. Close}{%0.2f}' ), # use @{ } for field names with spaces
            ( 'Volume', '@Volume{0.00 a}'      ),
        ],

        formatters={
            'Date'      : 'datetime', # use 'datetime' formatter for 'date' field
            'Adj. Close' : 'printf',   # use 'printf' formatter for 'adj close' field
                                      # use default 'numeral' formatter for other fields
        },

        # display a tooltip whenever the cursor is vertically in line with a glyph
        mode='vline'
    )
    p.add_tools(hover)
    
    if notebook:
        # show the results
        show(p, notebook_handle=True)
        push_notebook()
    else:
        # output the results
        output_file('%s.html' % template_name)
        save(p)

def plot_return(df, returnFunc, notebook=False, x='Date', y='Adj. Close', title="Return prices", xlabel="Date", ylabel="Price"):
    """
    Bokeh Plot for return prices with a custom title and meaningful axis labels.
    template_name: output file name of plot
    notebook: boolean for showing plot on jupyter notebook
    """    
    stock_return = returnFunc(df[y])
    
    # create a new plot with a title and axis labels
    p = Figure(title=title,
               x_axis_label=xlabel,
               y_axis_label=ylabel,
               x_axis_type='datetime',
               plot_height=500,
               plot_width=950,
               tools=['pan','wheel_zoom'],
               toolbar_location='below')
    
    # configure so that Bokeh chooses what (if any) scroll tool is active
    p.toolbar.active_scroll = "auto"
    # add a line renderer with legend and line thickness
    p.line(stock_return.index, stock_return, line_width=2, legend='Return')
    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    
    if notebook:
        # show the results
        show(p, notebook_handle=True)
        push_notebook()
    else:
        # output the results
        output_file('%s.html' % title)
        save(p)

def plot_return_dist(df, returnFunc, title='Daily Return Prices Distribution'):
    """Matplotlib for return prices distribution"""   
    # Calculate the daily percentage change for `daily_close_px`
    pct_change = returnFunc(df['Adj. Close'])
    #pct_change = close_px.pct_change()
    
    # Plot the distributions
    ax = pct_change.hist(bins=50, figsize=(12,8), align='mid')
    ax.set_title(title)
    #ax.set_xlim(-0.3,0.3)
    # Show the resulting plot
    plt.show()

def calc_volatility(df, returnFunc, min_periods=75, template_name='volatility', notebook=False, xlabel='Date', ylabel='Volatility', title='AAPL Volatility of Daily Returns'):
    """
    Bokeh plot for computed volatility of stock return price
    min_periods: Define the minumum of periods to consider
    template_name: output file name of plot
    notebook: boolean for showing plot on jupyter notebook
    """
    pct_change = returnFunc(df['Adj. Close'])
    
    
    # create a new plot with a title and axis labels
    p = Figure(title=title,
               x_axis_label=xlabel,
               y_axis_label=ylabel,
               x_axis_type='datetime',
               plot_height=500,
               plot_width=950,
               tools=['pan','wheel_zoom'],
               toolbar_location='below')
    
    # configure so that Bokeh chooses what (if any) scroll tool is active
    p.toolbar.active_scroll = "auto"
    
    # Calculate the volatility
    vol = pct_change.rolling(min_periods).std() * np.sqrt(min_periods) 
    
    # add a line renderer with legend and line thickness
    p.line(vol.index, vol, line_width=2, legend='Volatility')
    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    
    if notebook:
        # show the results
        show(p, notebook_handle=True)
        push_notebook()
    else:
        # output the results
        output_file('%s.html' % template_name)
        save(p)


def combine_stocks(data, tickers):
    # Concatenating dataframes for each ticker
    return pd.concat(data, keys=tickers, names=['Ticker', 'Date'])

def transform_stocks(data, tickers):    
    df = combine_stocks(data,tickers)
    
    # Isolate the `Adj Close` values and transform the DataFrame
    return df[['Adj. Close']].reset_index().pivot('Date', 'Ticker', 'Adj. Close')

def hist_returns(all_data):
    # Calculate the daily percentage change for `daily_close_px`
    daily_pct_change = financial_statistics.daily_return(all_data)

    # Plot the distributions
    daily_pct_change.hist(bins=50, sharex=True, figsize=(12,8))

    # Show the resulting plot
    plt.show()

def scatter_returns(data):
    # Plot a scatter matrix with the `daily_pct_change` data 
    pd.plotting.scatter_matrix(data, diagonal='kde', alpha=0.1,figsize=(12,12))

    # Show the plot
    plt.show()

def compute_multiple_volatility(data, returnFunc, tickers, template_name='volatility', notebook=False, min_periods=75):
    """
    Bokeh plot for computed moving historical standard deviation of the log returns
    data: list of dataframes
    min_periods: Define the minumum of periods to consider
    template_name: output file name of plot
    notebook: boolean for showing plot on jupyter notebook
    tickers: list of symbols
    """
    pct_change = returnFunc(data)
    
    # Calculate the volatility
    vol = pct_change.rolling(min_periods).std() * np.sqrt(min_periods) 

    # create a new plot with a title and axis labels
    p = Figure(title='Volatility of Historical prices',
               x_axis_label='Date',
               x_axis_type='datetime',
               plot_height=500,
               plot_width=950,
               tools=['pan','wheel_zoom'],
               toolbar_location='below')
   
    # configure so that Bokeh chooses what (if any) scroll tool is active
    p.toolbar.active_scroll = "auto"
    
    # add a line renderer with legend and line thickness
    for symbol, color in tickers:
        p.line(vol[symbol].index, vol[symbol], line_width=2, legend=symbol, line_color=color)    
        
    p.legend.location = "top_left"
    p.legend.click_policy="hide"

    if notebook:
        # show the results
        show(p, notebook_handle=True)
        push_notebook()
    else:
        # output the results
        output_file('%s.html' % template_name)
        save(p)

def plot_corr(group1, ticker1, group2, ticker2, template_name='volatility', notebook=False):
    """
    Bokeh plot for computed correlation between two stocks
    group1: dataframe of first company profile
    ticker1: symbol of first company profile
    group2: dataframe of second company profile
    ticker2: symbol of second company profile
    template_name: output file name of plot
    notebook: boolean for showing plot on jupyter notebook
    """
    data = group1[ticker1].rolling(window=252).corr(group2[ticker2])
    
    # create a new plot with a title and axis labels
    p = Figure(title='Correlation of '+ticker1+' and '+ticker2+' stocks',
               x_axis_label='Date',
               x_axis_type='datetime',
               plot_height=500,
               plot_width=950,
               tools=['pan','wheel_zoom'],
               toolbar_location='below')
   
    # configure so that Bokeh chooses what (if any) scroll tool is active
    p.toolbar.active_scroll = "auto"
    
    # add a line renderer with legend and line thickness
    p.line(data.index, data, template_name='volatility', notebook=False, line_width=2, legend='Corr')    
        
    p.legend.location = "top_left"
    p.legend.click_policy="hide"

    if notebook:
        # show the results
        show(p, notebook_handle=True)
        push_notebook()
    else:
        # output the results
        output_file('%s.html' % template_name)
        save(p)

        
def plot_bollinger_signals(data, signals, ticker=None, notebook=False):
    # create a new plot with a title and axis labels
    p = Figure(title=ticker+' Bollinger Bands Strategy',
               x_axis_label='Date',
               x_axis_type='datetime',
               y_axis_label='Price in $',
               plot_height=500,
               plot_width=950,
               tools=['pan','wheel_zoom'],
               toolbar_location='below')
    
    inc = data['Close'] > data['Open']
    dec = data['Open'] > data['Close']
    w = 12*60*60*1000 # half day in ms
    
    p.segment(data.index, data['High'], data.index, data['Low'], color="black")
    p.vbar(data.index[inc], w, data['Open'][inc], data['Close'][inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(data.index[dec], w, data['Open'][dec], data['Close'][dec], fill_color="#F2583E", line_color="black")
    
    # configure so that Bokeh chooses what (if any) scroll tool is active
    p.toolbar.active_scroll = "auto"
    
    # add a line renderer with legend and line thickness
    p.line(signals.index, signals['mediumband'], line_width=2, legend='Mediumband', line_color='black')
    p.line(signals.index, signals['upperband'], line_width=2, legend='Upperband', line_color='orange')
    p.line(signals.index, signals['lowerband'], line_width=2, legend='Lowerband', line_color='blue')
    
    p.triangle(signals.loc[signals.positions == 1.0].index, 
             signals.lowerband[signals.positions == 1.0],
             size=15, fill_color='green', legend='Buy')
    p.inverted_triangle(signals.loc[signals.positions == -1.0].index, 
             signals.upperband[signals.positions == -1.0],
             size=15, fill_color='red', legend='Sell')
        
    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    
    if notebook:
        # show the results
        show(p, notebook_handle=True)
        push_notebook()
    else:
        # output the results
        output_file('%s Bollinger Bands Strategy.html' % ticker)
        save(p)


def plot_crossover_signals(data, signals, ticker=None, notebook=False):
    # create a new plot with a title and axis labels
    p = Figure(title=ticker+' Moving Crossover Strategy',
               x_axis_label='Date',
               x_axis_type='datetime',
               y_axis_label='Price in $',
               plot_height=500,
               plot_width=950,
               tools=['pan','wheel_zoom'],
               toolbar_location='below')
   
    # configure so that Bokeh chooses what (if any) scroll tool is active
    p.toolbar.active_scroll = "auto"
    
    # add a line renderer with legend and line thickness
    p.line(data.index, data['Close'], line_width=2, legend='Close', line_color='black')
    p.line(signals.index, signals['short_mavg'], line_width=2, legend='Slow MA', line_color='orange')
    p.line(signals.index, signals['long_mavg'], line_width=2, legend='Fast MA', line_color='blue')
    
    p.triangle(signals.loc[signals.positions == 1.0].index, 
             signals.short_mavg[signals.positions == 1.0],
             size=15, fill_color='green', legend='Bullish Crossover')
    p.inverted_triangle(signals.loc[signals.positions == -1.0].index, 
             signals.short_mavg[signals.positions == -1.0],
             size=15, fill_color='red', legend='Bearish Crossover')
        
    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    
    if notebook:
        # show the results
        show(p, notebook_handle=True)
        push_notebook()
    else:
        # output the results
        output_file('%s Moving Crossover Strategy.html' % ticker)
        save(p)