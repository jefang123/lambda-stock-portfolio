# lambda-stock-portfolio
Simple AWS lambda that reports a given portfolio of stocks using [Serverless](https://serverless.com/) Framework

Instal Serverless-CLI:  
```npm install -g serverless ```

Install Requirements:  
```npm install```

setup aws credentials:  
```serverless config credentials --provider aws --key AKIAIOSFODNN7EXAMPLE --secret wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY```

This Lambda also utilizes env variables for sending emails:  
```
#.env file
PORTFOLIO = "APPL,VTI,MSFT" # (Comma separated) Stocks to keep track of
SENDER = # Email sender
RECEIVER = # Email receiver
CRED = # Sender pw 
EOD_TOKEN =  # AppToken for EOD API Calls
```

In `mail_sender.py`, the email service is set to `GMAIL`, and the port is set to `467` by default. Change these if necessary.
```
def setup_service(service="GMAIL", port=465):
  SERVERS = {
    "GMAIL": "smtp.gmail.com",
    "HOTMAIL": "smtp.live.com",
    "YAHOO": "smtp.mail.yahoo.com"
  }
  # possible ports: 465 (SSL), 587 (TLS)
  PORT = port
  return PORT, SERVERS["service"]
```

The lambda is set to run twice a day, at 14:30 and 21:30 UTC. You can configure this in the `serverless.yml` file:
```
custom:
  stages: # add for lambdas with different environments
    # - dev
    # - prod 
  report-schedule: cron(30 14-21/7 * * 2-6 *)
```

The lambda uses the [EOD Historical Data](https://eodhistoricaldata.com/knowledgebase/live-realtime-stocks-api/) for real time stock prices.
A free account is rate limited to 20 calls a day.
By default the lambda can keep track of 10 stocks on a free account token.

After configuring the `serverless config` and the `.env` file, deploy the lambda:
```
serverless deploy
```
