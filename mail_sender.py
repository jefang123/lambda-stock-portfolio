import smtplib, starttls
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

SERVERS = {
  "GMAIL": "smtp.gmail.com",
  "HOTMAIL": "smtp.live.com",
  "YAHOO": "smtp.mail.yahoo.com"
}

# possible ports: 465 (SSL), 587 (TLS)

smtp_server = "smtp.gmail.com"
port = 465
# port = 587

sender = "you@gmail.com"
password = "pw"

if port == 465:
  context = ssl.create_default_context()
  with smtplib.STMP_SSL(stmp_server, port, context=context) as server:
    try:
      server.login(sender, password)
      server.sendmail(from_addr, to_addr_list, message)
    except smtplib.STMPAuthenticationError as e:
      print("Incorrect Credentials")

elif port == 587:
    try:
      server = smtplib.SMTP(smtpserver)
      server.starttls()
      server.login(login,password)
      problems = server.sendmail(from_addr, to_addr_list, message)
      server.quit()
    except smtplib.STMPAuthenticationError as e:
      print("Incorrect Credentials")
      