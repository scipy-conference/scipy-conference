#!/usr/bin/env python

import jinja2
import mimetypes
import numpy as np
import os
import smtplib
import sys
import getpass
import email
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

if len(sys.argv) < 3:
    print("Usage: ./send-reminder.py review_reminder.csv review_reminder.txt.in")

with open(sys.argv[2], "r") as fp:
    email_template = fp.read()
template = jinja2.Template(email_template)

pc_invitees = np.loadtxt(
    sys.argv[1],
    delimiter=",",
    dtype={"names": ("invitee", "email"), "formats": ("S128", "S128")},
)

username = "katyhuff@gmail.com"
password = getpass.getpass("password:")
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username, password)

for member in pc_invitees:
    email_body = template.render(name=member["invitee"])
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "SciPy2014 Abstract Reviews Due April 21"
    msg["From"] = "Katy Huff <katyhuff@gmail.com>"
    msg["To"] = member["email"]
    msg["Cc"] = "Serge Rey <sjsrey@gmail.com>,"
    msg["Date"] = email.utils.formatdate()
    msg.attach(MIMEText(email_body, "plain"))
    from_address = "Katy Huff <katyhuff@gmail.com>"
    to_address = ["Serge Rey <sjsrey@gmail.com>"]
    to_address.extend([em.strip() for em in member["email"].split(",")])

    print(email_body)
    server.sendmail(from_address, to_address, msg.as_string())
