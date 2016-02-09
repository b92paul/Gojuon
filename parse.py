#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
f = open('gojuon_raw.txt')
c = ''
data= {}

rows = 'aiueo'
cols = 'akstnhmyrw'

def norm(col):
    if col == '': return 'a'
    elif col == 'f': return 'h'
    elif col == 'ts': return 't'
    elif col == 'sh': return 's'
    elif col == 'ch': return 't'
    else: return col
for i, line in enumerate(f):
    if i%2 == 0:
        c = line.strip()
    else:
        obj = {}
        row = line.strip()[-1]
        col = line.strip()[:-1]
        col = norm(col)
        if i == 91:
            col = 'w'
        if row == 'n':
            row = 'u'
            col = 'w'
        if row not in data:
            data[row] = {}
        if col not in data[row]:
            data[row][col] = {}
        obj['chr'] = c
        obj['pro'] = line.strip()
        data[row][col] = obj
print data
for row in rows:
    out = ''
    for col in cols:
        if row in data and col in data[row]:
            out += data[row][col]['chr']
        else:out += '  '
    print out
'''
for row in data:
    out = ''
    for col in data[row]:
        out += data[row][col]['chr']
    print out
'''
json.dump(data,open('data.json','w'))
