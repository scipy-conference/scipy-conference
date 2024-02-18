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
    print('Usage: ./send-pc-thank-you.py pc_invitees.csv pc_invitation.txt.in')

with open(sys.argv[2], 'r') as fp:
    email_template = fp.read()
template = jinja2.Template(email_template)

pc_invitees = np.loadtxt(sys.argv[1],
        delimiter=',',
        dtype={'names': ('invitee', 'email','fields'),
            'formats': ('S128', 'S128', 'S128')})

expertise_name_map = {
        'cs': 'scientific computing with python',
        'edu': 'scientific computing education',
        'geo': 'geophysics',
        'gis': 'geospatial data',
        'gissci': 'geospatial data in science',
        'astro': 'astronomy and astrophysics',
        'viz': 'visualization',
        'soc': 'computational social sciences',
        'bioinfo': 'bioinformatics',
        'eng': 'engineering'}

def get_fields(fields):
    split_fields = fields.split(" ")
    if len(split_fields) == 1:
        fieldstr = expertise_name_map[split_fields[0]]
        is_are_str = "is"
    if len(split_fields) == 2:
        fieldstr = expertise_name_map[split_fields[0]] +\
        " and " +\
        expertise_name_map[split_fields[1]]
        is_are_str = "are"
    if len(split_fields) > 2:
        raise Exception("Too many fields in"+fields)
    return fieldstr, is_are_str

username = 'katyhuff@gmail.com'
password = getpass.getpass('password:')
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)

for member in pc_invitees:
    fieldstr, is_are_str =get_fields(member['fields'])
    email_body = template.render(name=member['invitee'],
        expertise=fieldstr,
        isare=is_are_str)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'SciPy2014 Program Committee Request for Full Paper Reviews'
    msg['From'] = 'Katy Huff <katyhuff@gmail.com>'
    msg['To'] = member['email']
    msg['Cc'] = 'Serge Rey <sjsrey@gmail.com>,Stefan van der Walt<stefan@sun.ac.za>,Aron Ahmadia<aron@ahmadia.net>'
    msg['Date'] = email.utils.formatdate()
    msg.attach(MIMEText(email_body, 'plain'))
    from_address = 'Katy Huff <katyhuff@gmail.com>'
    to_address = ['Serge Rey <sjsrey@gmail.com>']
    to_address.extend([em.strip() for em in member['email'].split(',')])

    print(email_body)
    server.sendmail(from_address, to_address, msg.as_string())
