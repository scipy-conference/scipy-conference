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

if len(sys.argv) < 5:
    print('Usage: ./send-decisions.py decisions.csv template.txt.in title_authors.csv author_comments.csv')

decisions = np.loadtxt(sys.argv[1],
        delimiter='\t',
        dtype={'names': ('id', 'decision'),
            'formats': ('S32', 'S32')})

def decision_to_poster_talk(decision):
    if decision.strip() == 'poster':
        return 'poster'
    return 'talk'

with open(sys.argv[2], 'r') as fp:
    email_template = fp.read()
template = jinja2.Template(email_template)

title_authors = np.loadtxt(sys.argv[3],
        delimiter='\t',
        dtype={'names': ('id', 'title', 'authors', 'emails'),
            'formats': ('S32', 'S1024', 'S512', 'S128')})

track_mini_name_map = {'gen': 'General Track',
        'tfr': 'Reproducibility Track',
        'ml': 'Machine Learning Track',
        'gis': 'GIS Mini-symposium',
        'met': 'Meteorology, Climatology, and Atmospheric and Oceanic Science Mini-symposium',
        'ast': 'Astronomy and Astrophysics Mini-symposium',
        'img': 'Medical Imaging Mini-symposium',
        'bio-f': 'Bioinformatics Mini-symposium',
        'bio-s': 'Bioinformatics Mini-symposium',
        'bio-m': 'Bioinformatics Mini-symposium',
        'poster': 'Poster Session'}

def decision_is_poster(decision):
    if decision.strip() == 'poster':
        return True
    return False

with open(sys.argv[4], 'r') as fp:
    author_comments = []
    lines = fp.readlines()
    for line in lines:
        author_comments.append(line.split('\t'))

def get_standard_id(_id):
    return _id.lower().strip()

def get_author_comments(_id, author_comments):
    id_ = get_standard_id(_id)
    comments = []
    for review in author_comments:
        if get_standard_id(review[0]) == id_:
            comments.append(review[1])
    if len(comments) == 0:
        comments.append('No comments')

    return comments

def get_decision(_id, decisions):
    _id = get_standard_id(_id)
    for decision in decisions:
        if get_standard_id(decision['id']) == _id:
            return decision['decision']

    raise IndexError('Could not find id: ' + _id + ' decision')


username = 'matthew.m.mccormick@gmail.com'
password = getpass.getpass('password:')
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
for submission in title_authors:
    decision = get_decision(submission['id'], decisions)
    authors = submission['authors'].split(';')
    submitters = ''
    for author in authors:
        name_split = author.split(',')
        if len(name_split) == 1:
            submitters += name_split[0] + ', '
        else:
            submitters += name_split[1] + ' ' + name_split[0] + ', '

    email_body = template.render(submitters=submitters,
            abstract_title=submission['title'],
            poster_talk=decision_to_poster_talk(decision),
            track_mini_name=track_mini_name_map[decision],
            is_poster=decision_is_poster(decision),
            reviewers_comments=get_author_comments(submission['id'], author_comments))
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Abstracts to review for SciPy 2013'
    msg['From'] = 'Matthew McCormick <matthew.m.mccormick@gmail.com>'
    msg['To'] = submission['emails']
    msg['Cc'] = 'Katy Huff <katyhuff@gmail.com>, Andy Terrel <andy.terrel@gmail.com>'
    msg['Date'] = email.utils.formatdate()
    msg.attach(MIMEText(email_body, 'plain'))
    from_address = 'Matthew McCormick <matthew.m.mccormick@gmail.com>'
    to_address = ['Katy Huff <katyhuff@gmail.com>', 'Andy Terrel <andy.terrel@gmail.com>']
    to_address.extend([em.strip() for em in submission['emails'].split(',')])

    print(email_body)
    server.sendmail(from_address, to_address, msg.as_string())
