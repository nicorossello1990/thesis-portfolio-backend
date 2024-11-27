import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Descargar los datos históricos de AAPL, MSFT y GOOGL
tickers = yf.Tickers('MSFT AAPL GOOGL')

# Obtener los datos históricos de cada ticker
data_aapl = tickers.tickers['AAPL'].history(start="2015-01-01", end="2024-11-01", actions=True, auto_adjust=True, back_adjust=False)
#data_msft = tickers.tickers['MSFT'].history(start="2015-01-01", end="2024-11-01", actions=True, auto_adjust=True, back_adjust=False)
#data_googl = tickers.tickers['GOOGL'].history(start="2015-01-01", end="2024-11-01", actions=True, auto_adjust=True, back_adjust=False)

data_aapl.to_csv('historical_stock_data.csv', index=True)
data_aapl['Close'].plot(label='AAPL', title='Precio de Cierre de AAPL')
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre')
plt.legend()
plt.show()