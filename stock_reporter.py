import requests

def stock_api(portfolio):

def send_email(client, prices, receiver):

def main(portfolio, client, receiver):
  if receiver:
    prices = stock_api(portfolio)
    send_email(client, prices, receiver)
  else:
    print("No email given. Please update with an email address to receive emails.")

if __name__ == "__main__":
  main()