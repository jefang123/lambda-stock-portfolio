from os import environ
import stock_reporter

def report_stocks():
  portfolio = environ.get("PORTFOLIO")
  token = environ.get("EOD_TOKEN")
  if portfolio:
    stocks = portfolio.split(" ")
    client = login_email()
    stock_reporter.main(stocks, client, environ.get("EMAIL_TO", ""))
  else:
    print("Portfolio is empty, add some stocks to track!")