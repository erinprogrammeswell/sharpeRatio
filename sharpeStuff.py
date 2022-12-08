import yfinance as yf
import pandas as pd


def get_historical_data(ticker, start_date):
    # Pull Historical Data
    data = yf.download(ticker, start=start_date)
    # Calculate Daily Returns
    data['Daily Return'] = data['Adj Close'].pct_change()   
    return data.dropna()


def std_dev(data):
    # Get number of observations
    n = len(data)
    # Calculate mean
    mean = sum(data) / n
    # Calculate deviations from the mean
    deviations = sum([(x - mean)**2 for x in data])
    # Calculate Variance & Standard Deviation
    variance = deviations / (n - 1)
    s = variance**(1/2)
    return s

def sharpe_ratio(data, risk_free_rate=0.0):
    # Calculate Average Daily Return
    mean_daily_return = sum(data) / len(data)
    # Calculate Standard Deviation
    s = std_dev(data)
    # Calculate Daily Sharpe Ratio
    daily_sharpe_ratio = (mean_daily_return - risk_free_rate) / s
    # Annualize Daily Sharpe Ratio
    sharpe_ratio = 252**(1/2) * daily_sharpe_ratio
    
    return sharpe_ratio

AAPL = get_historical_data( 'AAPL', start_date= '2020-01-01')
print (sharpe_ratio (AAPL['Daily Return']))

