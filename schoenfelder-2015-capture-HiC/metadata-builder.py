#!/usr/bin/env python

import yaml

d = {
    'study': {
        'label': 'schoenfelder-2015',
        'long_label': 'Promoter-capture Hi-C from Schoenfelder et al 2015',
        'reference': 'Schoenfelder, S. et al. The pluripotent regulatory circuitry connecting promoters to their long-range interacting elements. Genome Res. (2015). doi:10.1101/gr.185272.114',
        'PMID': "25752748"},
    'tracks': [],
}

SOURCE = {
        'url': 'http://www.ebi.ac.uk/arrayexpress/files/E-MTAB-2414/E-MTAB-2414.additional.1.zip',
        'fn': 'E-MTAB-2414.additional.1.zip',
    }

for celltype in ['ESC', 'FLC']:
    for inter in ['promoter-other', 'promoter-promoter']:
        inter_cap = inter.capitalize()
        inter_und = inter.replace('-', '_')

        block = {
            'genome': 'mm9',
            'short_label': '{celltype} {inter}'.format(**locals()),
            'long_label': inter.capitalize() + '{inter_cap} interactions in {celltype} cells'.format(**locals()),
            'original': 'raw-data/{celltype}_{inter_und}_significant_interactions.txt'.format(**locals()),
            'processed': 'processed-data/{celltype}_{inter_und}_significant_interactions.bam'.format(**locals()),
            'script': 'src/process.py',
            'source': SOURCE,
            'trackinfo': {
                'tracktype': 'bam',
                'visibility': 'dense',
                'pairEndsByName': '.',
                'pairSearchRange': 2000000
            },
            'type': 'bam',
        }
        d['tracks'].append(block)


for celltype in ['ESC', 'FLC']:
    for gene in [
        'Cpeb4-001',
        'Myb-203',
        'Plcl2-201',
        'Bcl11a-003',
        'Car2-201',
        'Meis1-001',
        'Tmco1-201',
        'Hbb-b1-001',
        'Hbb-b2-001',
        'Hbb-bh1-001',
        'Hbb-y-001',
        'Hba-a1-001',
        'Hba-x-001',
        'Mgst3-001',
        'Gypa-201',
        'Ppox-001',
        'Add2-202|Add2-201',
        'Pcx-201|Pcx-202|Pcx-203',
        'Clk3-201',
        'Stx11-201|Stx11-202',
    ]:
        sanitized_gene = gene.replace('|', '_')
        block = {
            'genome': 'mm9',
            'short_label': gene + ', ' + celltype,
            'long_label': 'Promoter-other interactions for {gene} in {celltype} cells'.format(**locals()),
            'original': 'raw-data/{celltype}_promoter_other_significant_interactions.txt'.format(**locals()),
            'processed': 'processed-data/{celltype}_promoter_other_significant_interactions_for_{sanitized_gene}.bigbed'.format(**locals()),
            'script': 'src/per-gene.py',
            'source': SOURCE,
            'trackinfo': {
                'tracktype': 'bigBed 9',
                'visibility': 'hide',
                'itemRgb': 'on',
            },
            'type': 'bigbed',
        }
        d['tracks'].append(block)

yaml.dump(d, open('metadata.yaml', 'w'), default_flow_style=False)
