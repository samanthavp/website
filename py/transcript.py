import os
import re
import json
from collections import OrderedDict as odict
# file paths
episode = 66
ifile = os.path.join('resources','transcripts','raw',str(episode)+'.txt')
ofile = os.path.join('src','content','transcripts',str(episode)+'.json')
# source txt file - from otter.ai
print('reading: {}'.format(ifile))
with open(ifile,'r') as f:
  raw = f.read()
# parse the file
print('parsing ...')
data = []
for match in re.findall('(.*)  (\d*\:*\d*\:\d\d)  \n(.*)',raw):
  print(' > [{}] {}'.format(match[1],match[0]))
  data.append(odict([
      ('speaker', match[0].replace('Unknown Speaker','')),
      ('time', match[1]),
      ('text', match[2]),
    ]))
# output file - warning: will overwrite existing json
print('writing: {}'.format(ofile))
with open(ofile,'w') as f:
  json.dump(data,f,indent=2)
