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

def was_lifted_over(y):
    # first line has comment saying it was lifted over. TODO: hubward should
    # add some additional metadata for this: from, to, original dir (abspath
    # or relpath)
    if 'lifting over' in open(y).readline():
        return True


def find_metadata(start='.'):
    """
    Recursively find metadata.yaml files.
    """
    metadata = []
    for root, dirs, files in os.walk(start):
        for filename in files:
            if filename == 'metadata.yaml':
                m = os.path.join(root, filename)
                metadata.append(m)
    return metadata


def resolve_root(y, path=None):
    """
    Returns the list of originals from which `y` was lifted over.

    If `y` itself is the original (i.e. it was not lifted over from anything),
    the list is empty.

    If `y` was lifted over, the first item of the list is the original.
    """
    if path is None:
        path = []
    if not was_lifted_over(y):
        return []
    first_line = open(y).readline()
    first_line = first_line.replace('# This config file was created when lifting over ', '')
    orig = first_line.split(' from')[0]
    if was_lifted_over(os.path.join(orig, 'metadata.yaml')):
        path = resolve_root(os.path.join(orig, 'metadata.yaml'), path)
    if orig not in path:
        path.append(orig)
    return path


if __name__ == "__main__":
    start = '.'
    metadata = find_metadata(start)
    to_remove = set()
    to_document = set()
    for m in metadata:
        chain = resolve_root(m)
        to_remove.update([os.path.join(start, i, 'metadata.yaml') for i in chain])
        if not chain:
            to_document.update([m])
        else:
            to_document.update([os.path.join(start, chain[0], 'metadata.yaml')])
    to_upload = set(metadata).difference(to_remove)
    print('These should be uploaded:')
    print('\n'.join(sorted(to_upload)))
    print('\nThese should be documented:')
    print('\n'.join(sorted(to_document)))
