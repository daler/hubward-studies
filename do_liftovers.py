#!/usr/bin/env python
"""
Reads the liftovers.tsv file to perform each liftover.

Also adds the lifted-over directory to .gitignore if it's not already there to
avoid clutter.
"""
import os
import subprocess as sp

manifest = [
    i.strip().split('\t')
    for i in open('liftovers.tsv')
    if not i.startswith('#')
]

ignored = [i.strip() for i in open('.gitignore')]
add_to_gitignore = []
for dirname, from_assembly, to_assembly, newdir in manifest:
    sp.check_call([
        'hubward',
        'liftover',
        '--from_assembly',
        from_assembly,
        '--to_assembly',
        to_assembly,
        dirname,
        newdir,
    ])

    if newdir not in ignored:
        add_to_gitignore.append(newdir)

if add_to_gitignore:
    with open('.gitignore', 'a') as fout:
        fout.write('\n'.join(add_to_gitignore) + '\n')
