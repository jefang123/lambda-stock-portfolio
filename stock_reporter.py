import requests
from mail_sender import send

def configure_url(portfolio, api_token):
  base_url = "https://eodhistoricaldata.com/api/real-time/"
  if len(portfolio):
    base_url += f"${portfolio[0]}?api_token={api_token}fmt=json"
    if len(portfolio) > 1:
      base_url += "&s=" + ",".join(portfolio[1:])
  return base_url  

def stock_api(portfolio, api_token):
  base_url = configure_url(portfolio, api_token)
  data = requests.get(base_url)
  if data.status_code = 200:
    if len(portfolio) == 1:
      return [data.json()]
    else:
      return data.json()
  else:
    print("Something went wrong with the api call. Check token rate limits")
    return None
    
def send_email(prices, creds):
  subject = "Portfolio prices for today"
  message = "Hello, the prices for your portfolio are: \n"
  for stock in prices:
    price = stock["stock"] + stock["change"]
    message += f"{stock['code']}: { price } \n"
  send(creds.get("SENDER"), creds.get("RECEIVER"), subject, message, creds.get("CRED"))

def check_creds(creds):
  sender = creds.get("SENDER")
  receiver = creds.get("RECEIVER")
  portfolio = creds.get("PORTFOLIO")
  length = portfolio.replace(" ","").split(",")
  if sender and receiver and length:
    return True
  else:
    if length < 1:
      print("No stocks in portfolio, aborting")
    if not sender:
      print("No email given to send with, aborting")
    if not receiver:
      print("No email given to receive email, aborting")
    return False

def main(portfolio, creds):
  check = check_creds(creds)
  if check:
    prices = stock_api(creds.get("PORTFOLIO"), creds.get("TOKEN"))
    send_email(prices, creds)
