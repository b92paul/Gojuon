#!/usr/bin/python
import json
import random
import time
data = json.load(open('data.json'))

rows = 'aiueo'
cols = 'akstnhmyrw'

rc = 'col'
print 'row or col? :',
tmp = raw_input().strip()
if tmp != '':
    rc = tmp

if rc == 'row':
    print 'input rows:(%s)' % rows,
    rows = raw_input().strip()
else:
    print 'input cols:(%s)' % cols,
    cols = raw_input().strip()

print 'pass number:',
num = int(raw_input())

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
while len(lst) != 0:
    pcnt += 1
    idx = random.randint(0, len(lst)-1)
    print lst[idx]['chr'],':',
    
    ans = raw_input().strip()
    
    if ans == lst[idx]['pro']:
        lst[idx]['cnt'] += 1
    else:
        lst[idx]['cnt'] = 0
        print 'Wrong!!!, ans is %s' % lst[idx]['pro']

    if lst[idx]['cnt'] == num:
        del lst[idx]
end_time = time.time()
res_time = (float)(end_time - start_time)
print res_time, res_time/pcnt 
