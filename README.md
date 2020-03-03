# lambda-stock-portfolio
Simple lambda that reports a given portfolio of stocks

Requirements:
Install serverless and plugin requirements

npm install serverless
npm install serverless-python-requirements

if needed:
npm install serverless-prune-plugin

setup aws credentials:
serverless config credentials --provider aws --key AKIAIOSFODNN7EXAMPLE --secret wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

The lambda uses the EOD Historical Data for real time stock prices.
A free account is rate limited to 20 calls a day.
Lambda can keep track of 10 stocks on a free account token.