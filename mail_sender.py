import smtplib, starttls
 
SERVERS = {
  "GMAIL": "smtp.gmail.com",
  "HOTMAIL": "smtp.live.com",
  "YAHOO": "smtp.mail.yahoo.com"
}
# possible ports: 465 (SSL), 587 (TLS)
PORT = 465
# PORT = 587


def send(sender, to_addr, subject, message, password, service="GMAIL"):
  header  = 'From: %s\n' % sender
  header += 'To: %s\n' % ','.join(to_addr_list)
  header += 'Subject: %s\n\n' % subject
  message = header + message

  smtp_server = SERVERS.get(service, "smtp.gmail.com")
  if PORT == 465:
    context = ssl.create_default_context()
    with smtplib.STMP_SSL(stmp_server, port, context=context) as server:
      try:
        server.login(sender, password)
        server.sendmail(from_addr, to_addr_list, message)
      except smtplib.STMPAuthenticationError as e:
        print("Incorrect Credentials")

  elif PORT == 587:
    try:
      server = smtplib.SMTP(smtpserver)
      server.starttls()
      server.login(login,password)
      problems = server.sendmail(from_addr, to_addr_list, message)
      server.quit()
    except smtplib.STMPAuthenticationError as e:
      print("Incorrect Credentials")
  print("Email sent!")