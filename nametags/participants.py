#!/usr/bin/env python

import csv,re

intent = 'list'
intent = 'tags'

replace = {
    'SFU': 'Simon Fraser University',
    'UBC': 'University of British Columbia',
    'Yukawa Institute for Theoretical Physics': 'YITP',
    'National Astronomical Observatories China': 'NAOC'
}

volunteers = {
    'soc': ['Frolov', 'Fujiwara', 'Picker', 'Pogosian', 'Pospelov', 'Psaltis', 'Scott'],
    'volunteer': ['Aftergood', 'Brush', 'Contreras', 'Coutts', 'Crowter', 'Fonseca', 'Hojjati', 'Galvez Ghersi', 'Grandy', 'Narimani', 'Pogosian', 'Talbot', 'Troester', 'Vdovkina', 'Yin', 'Zucca']
}

with open('Registration_Jan 07.csv', 'rU') as csvfile:
    participants = csv.reader(csvfile, dialect='excel')
    people = [p for p in participants if p[-1] == 'Yes' or (p[-1] == 'No' and intent == 'tags')]

for p in sorted(people, key=lambda p: (p[3].lower(), p[4].lower())):
    if (intent == 'tags' and len(p[3]+p[4]) > 24):
    	p[4] = re.sub('[a-z]+', '.', p[4])
    for k in replace.keys():
    	p[5] = p[5].replace(k, replace[k])
    label = ''
    for tag in sorted(volunteers.keys()):
        if p[3] in volunteers[tag]:
            label = '[' + tag + ']'
    print "\\nametag%s{%s %s}{%s}" % (label, p[4], p[3], p[5] if p[5] != 'None' else '')
