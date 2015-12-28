#!/usr/bin/env python

"""
The goal is to find all metadata.yaml files, and decide which should be used
for automated documentation and which should be uploaded.

Scans the current directory, looking for all studies. If a study was lifted
over to a new assembly -- or possibly multiple successive assemblies -- uses
the original metadata for documentation and uses the last lifted-over one to
upload.
"""

import yaml
import os
import glob
from textwrap import dedent
from hubward import models
from jinja2 import Template


def was_lifted_over(y):
    """
    If lifted over, returns the `liftover` dictionary; otherwise None.
    """
    return yaml.load(
        open(os.path.join(y, 'metadata.yaml'))
    )['study'].get('liftover')


def find_metadata(start='.'):
    """
    Recursively find metadata.yaml files.
    """
    metadata = []
    for root, dirs, files in os.walk(start):
        for filename in files:
            if filename == 'metadata.yaml':
                metadata.append(root)
    return metadata

start = '.'


def normpath(p):
    return os.path.relpath(p, start)

metadata = find_metadata(start)
to_remove = []
to_document = []
for m in metadata:
    w = was_lifted_over(m)
    if w:
        to_remove.append(normpath(w['previous_study']))
        to_document.append(normpath(w['original_study']))
    else:
        to_document.append(normpath(m))

to_document = set(to_document)
to_remove = set(to_remove)

to_upload = set(map(normpath, metadata)).difference(to_remove)
print('These should be uploaded:')
print('\n'.join(sorted(to_upload)))
print('\nThese should be documented:')
print('\n'.join(sorted(to_document)))

genomes = []
template = Template(open('manifest_template.rst').read())
with open('manifest.rst', 'w') as fout:
    studies = []
    for study in sorted(to_document):
        study = models.Study(study)
        study.underline = '=' * (len(study.dirname) + 4)
        study.genomes = ', '.join(
            sorted(list(set([i.genome for i in study.tracks]))))
        genomes.extend([i.genome for i in study.tracks])
        studies.append(study)
    fout.write(template.render(studies=studies))

with open('to_process.sh', 'w') as fout:
    fout.write('#!/bin/bash\n')
    for study in sorted(to_document):
        fout.write('hubward process {0}\n'.format(study))
    fout.write('./do_liftovers.py')

    mode = os.stat(fout.name).st_mode
    mode |= (mode & 0444) >> 2
    os.chmod(fout.name, mode)

with open('to_upload.txt', 'w') as fout:
    for study in sorted(to_upload):
        fout.write(study + '\n')
