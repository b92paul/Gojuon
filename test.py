#!/usr/bin/python
import json
import random
import time
data = json.load(open('data.json'))

rows = 'aiueo'
cols = 'akstnhmyrw'

rc = 'col'
print 'row or col? (Default col):',
tmp = raw_input().strip()
if tmp != '':
    rc = tmp

if rc == 'row':
    print 'input rows:(%s)' % rows,
    rows = raw_input().strip()
else:
    print 'input cols:(%s)' % cols,
    cols = raw_input().strip()

print 'pass number(Default 3):',
num = 3
tmp = raw_input()
if tmp != '' and tmp.isdigit():
    num = int(num)

lst = []
for row in rows:
    for col in cols:
        if row in data and col in data[row]:
            obj = data[row][col]
            obj['cnt'] = 0
            #print obj
            lst.append(obj)
start_time = time.time()
pcnt = 0
wcnt = 0

pchr = ''

while len(lst) != 0:
    while True:
        idx = random.randint(0, len(lst)-1)
        if len(lst) == 1 or lst[idx]['chr'] != pchr:
            pchr = lst[idx]['chr']
            break
    while True:
        pcnt += 1
        print lst[idx]['chr'],':',
    
        ans = raw_input().strip()
    
        if ans == lst[idx]['pro']:
            lst[idx]['cnt'] += 1
            break
        else:
            lst[idx]['cnt'] = 0
            wcnt += 1
            print 'Wrong!!!, ans is %s' % lst[idx]['pro']

    if lst[idx]['cnt'] == num:
        del lst[idx]
end_time = time.time()
res_time = (float)(end_time - start_time)
if pcnt == 0:
    print 'Please input rows or cols for the test!'
    exit(0)

print 'Total time: %.3f' % res_time
print 'Time per word: %.3f' % (res_time/pcnt)
print 'Accuracy: %.3f %%' % (100-float(wcnt)/pcnt*100)
