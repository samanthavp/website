import sys,os,re,json
slug = sys.argv[1]
# file paths
ifile = os.path.join('src','content','articles',slug+'.md')
ofile = os.path.join('src','content','articles',slug+'.json')
tfile = os.path.join('.tmp','body.html')
data = dict(slug=slug)
# pandoc
print('pandoc: {} -> html'.format(ifile))
os.system('pandoc --base-header-level=3 {} -o {}'.format(ifile,tfile))
# parse headerblock
print('reading: {}'.format(ifile))
with open(ifile,'r') as f:
  md = f.read()
print('parsing header')
header = re.findall('---(.*)---',md,re.S)[0]
data.update(
  title = re.findall('^title:\s\'?\"?(.*?)\'?\"?$',header,re.M)[0],
  authors = re.findall('^- (.*)',header,re.M),
  date = re.findall('^date:\s*(.*)',header,re.M)[0],
  no = int(re.findall('^no:\s*(.*)',header,re.M)[0]),
)
print('cleaning body')
with open(tfile,'r') as f:
  body = f.read()
body = re.sub('(?<=<h\d)\sid=\".*?\"(?<!>)','',body)
data.update(body=body)
print('writing: {}'.format(ofile))
with open(ofile,'w') as f:
  json.dump(data,f,indent=2)
