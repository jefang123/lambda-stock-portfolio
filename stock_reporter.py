import requests

def stock_api(portfolio, api_token):
  base_url = "https://eodhistoricaldata.com/api/real-time/"
  if len(portfolio):
    base_url += f"${portfolio[0]}?api_token={api_token}fmt=json&s="
    base_url += ",".join(portfolio[1:])
  else:
    print("No stocks in portfolio, aborting.")
    return None
  data = requests.get(base_url)
  if data.status_code = 200:
    return data.json()
  else:
    print("Something went wrong with the api call. Check token rate limits")
    return None
    
def send_email(client, prices, receiver):
  current_prices = {}
  for stock in prices:
    current_prices[stock["code"]] = stock["open"]
  # client.send_email(receiver)

def main(portfolio, client, receiver, token):
  if receiver:
    prices = stock_api(portfolio, token)
    send_email(client, prices, receiver)
  else:
    print("No email given. Please update with an email address to receive emails.")

# free tier limit : 20 calls per/day
# = 10 stocks per day
# this can be changed via membership changes or api changes 
  # https://eodhistoricaldata.com/api/real-time/AAPL.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&fmt=json&s=VTI,EUR.FOREX