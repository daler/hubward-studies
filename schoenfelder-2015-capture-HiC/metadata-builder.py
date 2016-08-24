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
    for inter in ['promoter-other', 'promoter-promoter']:
        inter_cap = inter.capitalize()
        inter_und = inter.replace('-', '_')
        block = {
            'genome': 'mm9',
            'short_label': '{celltype} {inter} bait'.format(**locals()),
            'long_label': inter.capitalize() + '{inter_cap} capture regions in {celltype}'.format(**locals()),
            'original': 'raw-data/{celltype}_{inter_und}_significant_interactions.txt'.format(**locals()),
            'processed': 'processed-data/{celltype}_{inter_und}_significant_interactions.bigbed'.format(**locals()),
            'script': 'src/process-bait.py',
            'source': SOURCE,
            'trackinfo': {
                'tracktype': 'bigBed 9',
                'visibility': 'dense',
                'color': '128,0,0',
            },
            'type': 'bigbed',
        }
        d['tracks'].append(block)

for celltype in ['ESC', 'FLC'][-1:]:
    for gene in [
        'Runx1-204|Runx1-201|Runx1-205|Runx1-203|Runx1-202|Runx1-206',
        'Rgs10-001|Rgs10-003',
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
        'Cnnm2-201|Cnnm2-202',
        'Galns-201|Galns-202',
        'Klf13-202|Klf13-201',
        'Dapk2-001',
        'Add3-203|Add3-202|Add3-201',
        'Foxo3-001|Foxo3-002|Foxo3-003',
        'Ifnar2-001|Ifnar2-002|Ifnar2-005|Ifnar2-006|Ifnar2-007|Ifnar2-009|Ifnar2-201',
        'Junb-201',
        'Mylip-201',
        'Bmp2k-001|Bmp2k-002',
        'Abhd16a-004|Abhd16a-001|Abhd16a-008|Abhd16a-007|Abhd16a-006',
        'Rab43-001|Rab43-003|Rab43-002|Rab43-202|Rab43-201',
        'Rhbdf1-006|Rhbdf1-009|Rhbdf1-001|Rhbdf1-003',
        'Grina-201',
        'Rhof-001',
        'Fads2-201',
        'Bcl2l1-001|Bcl2l1-003|Bcl2l1-004|Bcl2l1-002|Bcl2l1-007|Bcl2l1-005|Bcl2l1-006|Bcl2l1-201|Bcl2l1-202',
        'Nfe2l1-001|Nfe2l1-008|Nfe2l1-002|Nfe2l1-005|Nfe2l1-006|Nfe2l1-201|Nfe2l1-202|Nfe2l1-205|Nfe2l1-204|Nfe2l1-206|Nfe2l1-203',
        'Ccnb1-001|Ccnb1-002|Ccnb1-007',
        'St3gal5-201|St3gal5-202',
        'Ube2f-201|Ube2f-203|Ube2f-202',
        'Amd1-201',

    ]:
        sanitized_gene = list(set([i[:-4] for i in gene.split('|')]))
        sanitized_gene = '_'.join(sanitized_gene)
        block = {
            'genome': 'mm9',
            'short_label': sanitized_gene + ', ' + celltype,
            'long_label': 'Promoter-other interactions for {sanitized_gene} in {celltype} cells'.format(**locals()),
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
