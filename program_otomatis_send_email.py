# -*- coding: utf-8 -*-
"""Program otomatis send email.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j39ozSJFMhWfUSznET-ZpVnLA6KXr30W
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from email.mime.base import MIMEBase

pengirim_email = input(str('from:'))
pasword_email = input(str('masukan password:'))

# with open('receiver_list.txt', 'r') as file:
#   penerima = file.read().replace('\n', ',')

sent_from = pengirim_email
sent_to = input(str('masukan email penerima lalu akhiri dengan enter:'))
sent_subject = input(str('masukan subjek atau judul lalu akhiri dengan enter:'))
sent_body = input(str('masukan pesan yang akan dikirim lalu akhiri dengan enter:'))

# Commented out IPython magic to ensure Python compatibility.
email_text = """\
From: %s
To: %s
Subject: %s

# %s
""" % (sent_from, ",".join(sent_to), sent_subject, sent_body)

# ==============================================================================
# Mengirim Email atau Gagal
# ==============================================================================

try:
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.ehlo()
  server.login(pengirim_email, pasword_email)
  server.sendmail(sent_from, sent_to, email_text)
  server.close()
  print('Email Terkirim')
except Exception as exception:
  print("Error: %s!\n\n" % exception)

