#!/usr/bin/env python

import jinja2
import mimetypes
import numpy as np
import csv
import os
import smtplib
import sys
import getpass
import email
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def is_poster(entry):
    if entry == 'reject':
        raise Exception('A rejected abstract is being recorded')
    elif entry == 'poster':
        return True
    elif entry == 'talk':
        return False

if len(sys.argv) < 3:
    print('Usage: ./send-decisions.py decisions.csv decision.txt.in')

with open(sys.argv[2], 'r') as fp:
    email_template = fp.read()
template = jinja2.Template(email_template)

with open(sys.argv[1], 'rU') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    submissions = []
    for row in filereader:
        if row[5] == 'reject':
            continue
        submission = {}
        if len(row) > 7 :
            raise Exception("Too many columns in row with id "+row[0])
        submission['idnum'] = int(row[0])
        submission['title'] = row[1]
        submission['author'] = row[2]
        submission['email'] = row[3]
        submission['track'] = row[6]
        if row[5] != 'reject':
            submission['poster_talk'] = row[5]
            submissions.append(submission)


track_name_map = {
        'poster' : 'Poster',
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

tue = 'Tuesday, July 8'
wed = 'Wednesday, July 9'
thu = 'Thursday, July 10'
am = '10:15 - 12:15am'
pm = '2:15 - 4:15pm'

track_time_map = {
        'poster' : [wed,'in the afternoon'],
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
        'gis3': [wed, am],
        'gis4': [thu, am],
        'astro': [wed, pm],
        'bioinfo': [wed, pm],
        'geo': [wed, pm],
        'viz': [thu, pm],
        'soc': [thu, pm],
        'eng': [thu, pm]
        }


username = 'katyhuff@gmail.com'
password = getpass.getpass('password:')
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)

for submission in submissions:
    day = track_time_map[submission['track']][0]
    time = track_time_map[submission['track']][1]
    track = track_name_map[submission['track'].strip('1').strip('2').strip('3').strip('4')]
    email_body = template.render(
        author = submission['author'],
        abstract_title = submission['title'],
        track_name = track,
        poster_talk = submission['poster_talk'],
        slot_day = day,
        slot_time = time,
        )
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'SciPy2014 Abstract Decision - Action Requested'
    msg['From'] = 'Katy Huff <katyhuff@gmail.com>'
    msg['To'] = submission['email']
    msg['Cc'] = 'Serge Rey <sjsrey@gmail.com>,'
    msg['Date'] = email.utils.formatdate()
    msg.attach(MIMEText(email_body, 'plain'))
    from_address = 'Katy Huff <katyhuff@gmail.com>'
    to_address = ['Serge Rey <sjsrey@gmail.com>', 'Andy Terrel <andy.terrel@gmail.com>']
    to_address.extend([em.strip() for em in submission['email'].split(',')])

    print(email_body)
    server.sendmail(from_address, to_address, msg.as_string())
