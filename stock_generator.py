import requests
import pandas as pd

# Set the Tiingo API key
api_key = 'enter the api key'
symbol = 'AMZN'
start_date = '1970-01-01'  # Adjusted start date to go back at least ten years
end_date = '2024-05-18'
url = f'https://api.tiingo.com/tiingo/daily/{symbol}/prices?startDate={start_date}&endDate={end_date}&token={api_key}'

try:
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    data = response.json()
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    csv_file_path = 'amzn_stock_data.csv'
    df.to_csv(csv_file_path, index=False)
    
    print(f"Data saved to {csv_file_path}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
