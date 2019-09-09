import json
import os
for i in range(1,63+1):
  jname = os.path.join('src','content','episodes',str(i)+'.json')
  with open(jname,'r') as f:
    data = json.load(f)
  iname = os.path.join('html','img','episodes',str(i),data['img-tile'])
  #print(iname)
  #print(os.system('convert {} -resize 100% {}'.format(iname,iname)))
