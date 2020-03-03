from datetime import datetime, timedelta
import imaplib
import logging
from os import environ
import stock_reporter

def login_email():
    # Email login vars
    user = environ.get("EMAIL_TO", "")
    password = environ.get("EMAIL_CRED", "")
    client = environ.get("MAIL_CLIENT", "")

    # Login to email
    conn = imaplib.IMAP4_SSL(client)
    conn.login(user, password)
    return conn

def report_stocks():
  portfolio = environ.get("PORTFOLIO")
  token = environ.get("EOD_TOKEN")
  if portfolio:
    stocks = portfolio.split(" ")
    client = login_email()
    stock_reporter.main(stocks, client, environ.get("EMAIL_TO", ""))
  else:
    print("Portfolio is empty, add some stocks to track!")