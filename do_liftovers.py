#!/usr/bin/env python
import os
import yaml
import subprocess as sp

manifest = [
    ('sexton-2012', 'dm3', 'dm6'),

    # vanBemmel is in dm2; need to do incremental liftOver since there's no
    # direct dm2 -> dm6 chainfiles available.
    ('vanBemmel-2010', 'dm2', 'dm3'),
    ('vanBemmel-2010-dm3', 'dm3', 'dm6'),

]


ignored = [i.strip() for i in open('.gitignore')]
add_to_gitignore = []
for dirname, from_assembly, to_assembly in manifest:
    newdir = dirname + '-' + to_assembly
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

with open('.gitignore', 'a') as fout:
    fout.write('\n'.join(add_to_gitignore) + '\n')
