from os import environ
import stock_reporter

def report_stocks():
  creds = {
    "PORTFOLIO" : environ.get("PORTFOLIO"),
    "SENDER" : environ.get("SENDER"),
    "RECEIVER" : environ.get("RECEIVER"),
    "CRED" : environ.get("CRED"),
    "TOKEN" : environ.get("EOD_TOKEN"),
  }
  if portfolio:
    stocks = portfolio.split(" ")
    stock_reporter.main(stocks, environ.get("EMAIL_TO", ""))
  else:
    print("Portfolio is empty, add some stocks to track!")