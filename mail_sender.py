import smtplib, starttls

def setup_service(service="GMAIL", port=465):
  SERVERS = {
    "GMAIL": "smtp.gmail.com",
    "HOTMAIL": "smtp.live.com",
    "YAHOO": "smtp.mail.yahoo.com"
  }
  # possible ports: 465 (SSL), 587 (TLS)
  PORT = port
  smtp_server = SERVERS.get(service, "smtp.gmail.com")
  return PORT, smtp_server

def send_ssl(stmp_server, login, pw, send_to, message):
  context = ssl.create_default_context()
  with smtplib.STMP_SSL(stmp_server, 465, context=context) as server:
    server.login(login, pw)
    server.sendmail(login, send_to, message)

def send_tls(stmp_server, login, pw, send_to, message):
  server = smtplib.SMTP(smtpserver)
  server.starttls()
  server.login(login,pw)
  problems = server.sendmail(login, send_to, message)
  server.quit()

def create_message(sender, receiver, subject, message)
  header  = f'From: {sender}\n' 
  header += f'To: {to_addr}\n' 
  header += f'Subject: {subject}\n\n' 
  message = header + message
  return message

def send(sender, to_addr, subject, message, password):
  message = create_message(sender, to_addr, subject, message)
  PORT, smtp_server = setup_service()
  try:
    if PORT == 465:
      send_ssl(smtp_server, sender, passord, to_addr, message)
    elif PORT == 587:
      send_tls(smtp_server, sender, passord, to_addr, message)
  except smtplib.STMPAuthenticationError as e:
    print("Incorrect Credentials")
    return -1 
  print("Email sent!")
