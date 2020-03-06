from os import environ
import stock_reporter

def report_stocks():
  creds = {
    "SENDER" : environ.get("SENDER"),
    "RECEIVER" : environ.get("RECEIVER"),
    "CRED" : environ.get("CRED"),
    "TOKEN" : environ.get("EOD_TOKEN"),
  }
  portfolio = environ.get("PORTFOLIO").split(",")
  if portfolio:
    stock_reporter.main(stocks, creds)
  else:
    print("Portfolio is empty, add some stocks to track!")