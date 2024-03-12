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
    print("Usage: ./send-call.py all_accepted.csv call_for_papers.rst.in")

with open(sys.argv[2], "r") as fp:
    email_template = fp.read()
template = jinja2.Template(email_template)

authors = np.loadtxt(
    sys.argv[1],
    delimiter=",",
    dtype={"names": ("paper", "invitee", "email"), "formats": ("i4", "S128", "S128")},
)

username = "yourname@gmail.com"
password = getpass.getpass("password:")
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username, password)

for author in authors:
    email_body = template.render(name=author["invitee"])
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Invitation to Submit Full Paper to SciPy 2014"
    msg["From"] = "Katy Huff <yourname@gmail.com>"
    msg["To"] = author["email"]
    msg["Cc"] = (
        "Serge Rey <othername@gmail.com>,Stefan van der Walt<theirname@gmail.com>"
    )
    msg["Date"] = email.utils.formatdate()
    msg.attach(MIMEText(email_body, "plain"))
    from_address = "Katy Huff <yourname@gmail.com>"
    to_address = ["Stefan van der Walt<theirname@gmail.com>"]
    to_address.extend([em.strip() for em in author["email"].split(",")])

    print(email_body)
    server.sendmail(from_address, to_address, msg.as_string())
