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
    print('Usage: ./send-decisions.py decisions.csv decision.txt.in')

with open(sys.argv[2], 'r') as fp:
    email_template = fp.read()
template = jinja2.Template(email_template)

pc_invitees = np.loadtxt(sys.argv[1],
        delimiter=',',
        dtype={'names': ('author1', 'email1','author2','email2',),
            'formats': ('S128', 'S128', 'S128')})

track_name_map = {
        'poster' : 'Poster Session',
        'gen' : 'General',
        'edu': 'Scientific Computing Education',
        'geo': 'Geophysics',
        'gis': 'Geospatial Data In Science',
        'astro': 'Astronomy and Astrophysics',
        'viz': 'Visualization',
        'soc': 'Computational Social Sciences',
        'bioinfo': 'Bioinformatics',
        'eng': 'Engineering'
        }

track_time_map = {
        'poster' : [tues,'5 - 7pm']
        'gen1' : [tue, am],
        'gen2' : [tue, pm],
        'gen3' : [wed, am],
        'gen4' : [thu, am],
        'edu1': [tue, am],
        'edu2': [tue, pm],
        'edu3': [wed, am],
        'edu4': [thu, am],
        'gis1': [tue, am], 
        'gis2': [tue, pm], 
        'gis3': [twed, am], 
        'gis4': [thu, pm], 
        'astro': [wed, pm], 
        'bioinfo': [wed, pm],
        'geo': [wed, pm], 
        'viz': [thu, pm],
        'soc': [thu, pm],
        'eng': [thu, pm] 
        }


tue = 'Tuesday, July 8'
wed = 'Wednesday, July 9'
thu = 'Thursday, July 10'
am = '10:00 - 12:15am' 
pm = '2:15 - 4:15pm'



def get_list(submission, pat):
    to_ret = []
    for key, val in submission.iteritems() :
        if key.find(pat) != -1:
            to_ret.append(val)
    return to_ret

def get_fields(fields):
    split_fields = fields.split(" ")
    if len(split_fields) == 1:
        fieldstr = track_name_map[split_fields[0]]
        is_are_str = "is"
    if len(split_fields) == 2:
        fieldstr = track_name_map[split_fields[0]] +\
        " and " +\
        track_name_map[split_fields[1]]
        is_are_str = "are"
    if len(split_fields) > 2:
        raise Exception("Too many fields in"+fields)
    return fieldstr, is_are_str
    
username = 'katyhuff@gmail.com'
password = getpass.getpass('password:')
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)

for submission in pc_invitees:
    authors = ", ".join(get_list(submission, 'author'))
    emails = ", ".join(get_list(submission, 'email'))
    comments = get_list(submission, 'comment')
    day = track_time_map[submission['track'][0]
    time = track_time_map[submission['track'][1]
    track = track_name_map[submission['track'].strip('0').strip('1').strip('2')]
    email_body = template.render(submitters=authors, 
        abstract_title = submission['title'],
        slot_day = day,
        slot_time = time,
        is_poster =  bool(submission['poster']),
        reviewers_comments = comments 
        ) 
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'SciPy2014 Abstract Decision - Action Requested'
    msg['From'] = 'Katy Huff <katyhuff@gmail.com>'
    msg['To'] = emails
    msg['Cc'] = 'Serge Rey <sjsrey@gmail.com>,'
    msg['Date'] = email.utils.formatdate()
    msg.attach(MIMEText(email_body, 'plain'))
    from_address = 'Katy Huff <katyhuff@gmail.com>'
    to_address = ['Serge Rey <sjsrey@gmail.com>']
    to_address.extend([em.strip() for em in submission['email'].split(',')])

    print(email_body)
    server.sendmail(from_address, to_address, msg.as_string())
