import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st


# Define time range
start = '2010-01-01'
end = '2025-07-01'

st.title('Stock Trend Prediction')

import yfinance as yf
# Download stock data (Apple in this case)
user_input = st.text_input('Entre Stock Ticker', 'AAPL')
df = yf.download('AAPL', start=start, end=end)

# Describing data
st.subheader('Data from 2010 - 2025')
st.write(df.describe())
st.subheader('Data from 2010 - 2025')
st.write(df.describe())
st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)  

pip install streamlit
pip install yfinance
pip install keras