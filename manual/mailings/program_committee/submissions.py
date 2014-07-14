import csv
import jinja2
from collections import namedtuple

Row = namedtuple('Row', ('id', 'title', 'body'))

with open('submissions.csv') as f:
    f.readline()
    reader = csv.reader(f)

    rows = [Row(row[0], row[1].decode('utf-8'), row[2].decode('utf-8')) for row in reader]

template = jinja2.Template(open('submissions.html').read())
rendered = template.render(abstracts=rows)

with open('submissions_rendered.html', 'w') as f:
    f.write(rendered.encode('utf-8'))
