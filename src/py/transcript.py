import sys
import os
import re
import json
from collections import OrderedDict as odict
# file paths
episode = str(sys.argv[1])
ifile = os.path.join('.tmp',str(episode)+'.txt')
bfile = os.path.join('.tmp',str(episode)+'.bak.json')
ofile = os.path.join('src','content','transcripts',str(episode)+'.json')
# source txt file - from otter.ai
print('reading: {}'.format(ifile))
with open(ifile,'r') as f:
  raw = f.read()
# parse the file
print('parsing ...')
data = []
speakers = set()
for match in re.findall('(.*)  (\d*\:*\d*\:\d\d)  \n(.*)',raw):
  print(' > [{}] {}'.format(match[1],match[0]))
  speakers.add(match[0])
  data.append(odict([
      ('speaker', match[0].replace('Unknown Speaker','')),
      ('time', match[1]),
      ('text', match[2]),
    ]))
print('N: {}'.format(len(data)))
print('Speakers:\n > {}'.format('\n > '.join(speakers)))
# output file: save backup before overwriting
print('writing: {}'.format(ofile))
with open(ofile,'r') as fo:
  with open(bfile,'w') as fb:
    fb.write(fo.read())
with open(ofile,'w') as f:
  json.dump(data,f,indent=2)
