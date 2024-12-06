from kiteconnect import KiteConnect
import pandas as pd
import datetime

# Initialize Kite Connect with your API key
api_key = "47ts5ou0jd3pldey"
kite = KiteConnect(api_key=api_key)

# Set your access token obtained from the login flow
kite.set_access_token("H1Q2SShI2eiMXUvXle2LcJVyCET2AXDf")

# Nifty 50's instrument token
nifty_token = "NSE:NIFTY"

# Define the time frame and the date range
from_date = datetime.datetime(2023, 10, 1)  # Starting date
to_date = datetime.datetime(2023, 10, 31)  # Ending date
interval = "5minute"

# Fetch historical data
historical_data = kite.historical_data(nifty_token, from_date, to_date, interval)

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(historical_data)

# Display the DataFrame
print(df)

# Optionally, save to a CSV file
df.to_csv("nifty_historical_data_5min.csv", index=False)
