# Stock_Market_Predicition_Application
This project demonstrates stock price trend prediction using LSTM (Long Short-Term Memory) neural networks and provides an interactive dashboard built with Streamlit for visualization.

🚀 Features

Fetches historical stock data (using Yahoo Finance API)

Interactive Streamlit UI for stock ticker input

Data exploration with descriptive statistics

Time-series visualization of closing prices

LSTM-based stock trend prediction (trained in LSTM.ipynb)

Easy deployment as a web app

🛠️ Tech Stack

Python (NumPy, Pandas, Matplotlib)

Streamlit (for web-based dashboard)

yFinance (for stock data fetching)

Keras/TensorFlow (for LSTM model)

pandas_datareader (additional data sources)

📂 Project Structure
├── app.py          # Streamlit web app for stock trend visualization
├── LSTM.ipynb      # Notebook for training LSTM model
└── requirements.txt # Dependencies list (optional)

⚡ Installation

Clone the repository and install dependencies:

git clone https://github.com/yourusername/stock-trend-prediction.git
cd stock-trend-prediction
pip install -r requirements.txt


Or install individually:

pip install streamlit yfinance keras pandas matplotlib pandas_datareader

▶️ Usage

Run the Streamlit app:

streamlit run app.py


Enter a stock ticker (e.g., AAPL, TSLA, GOOG) to visualize trends and predictions.

📊 Example Output

Stock data summary (2010–2025)

Closing price vs. time chart

Predicted vs. actual stock trends (from LSTM model)
