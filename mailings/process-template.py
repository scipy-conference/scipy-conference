#!/usr/bin/env python

"""Process a jinja2 template with values specified in a YAML file."""

import argparse
import os
import yaml

from jinja2 import Template

def main(template_text, template_vars, output_file):
    template = Template(template_text)
    output_file_text = template.render(**template_vars)
    output_file.write(output_file_text)
    output_file.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('template_text', type=argparse.FileType('r'),
            help="Jinja2 template text file.")
    parser.add_argument('template_vars', type=argparse.FileType('r'),
            help="YAML file with values for the template variables.")
    parser.add_argument('--outfile', '-o', type=argparse.FileType('w'),
            help="Output processed template.")

    args = parser.parse_args()

    template_text = args.template_text.read()
    args.template_text.close()
    if not args.outfile:
        output_filepath = os.path.splitext(args.template_text.name)[0]
        output_file = open(output_filepath, 'w')
    else:
        output_file = args.outputfile

    template_vars = yaml.load(args.template_vars)
    args.template_vars.close()
    
    main(template_text, template_vars, output_file)
