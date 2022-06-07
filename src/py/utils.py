import os
import json

verbose = 3
root = 'web'

def log(msg,level):
  if verbose & verbose >= level:
    print({
      0: lambda msg: '-'*64+'\n'+msg+'\n'+'-'*64,
      1: lambda msg: '+ '+msg.upper(),
      2: lambda msg: '  > '+msg,
      3: lambda msg: '    - '+msg,
    }[level](msg),flush=True)

def key_drill(D,keys):
  # Given D={} and keys=['a','b']:
  # Updates D={'a':{'b':{}}} and returns D['a']['b']
  if len(keys):
    key = keys.pop(0)
    if key in D:
      return key_drill(D[key],keys)
    else:
      D.update({key:{}})
      return D[key]
  else:
    return D

def json_load(path):
  with open(path,'r', encoding="utf8") as f:
    return json.load(f)


def json_drill(path,ext='.json'):
  # clean path
  path = path.rstrip(os.path.sep)+os.path.sep
  D = {}
  for root,dirs,files in os.walk(path):
    # prepare for key_drill
    base = root.replace(path,'')
    keys = base.split(os.path.sep) if base else []
    Dk = key_drill(D,keys)
    # load the files (assume all .json)
    for file in files:
      if file.endswith(ext):
        Dk.update({file.replace(ext,''):json_load(os.path.join(root,file))})
  return(D)

def json_save(path,content,**kwargs):
  log('save: '+path, level=2)
  with open(path,'w') as f:
    json.dump(content,f,**kwargs)

def file_save(path,string):
  log('save: '+path, level=2)
  with open(path,'w', encoding="utf8") as f:
    f.write(string)

def page_save(E,T,page,ext='.html',**kwargs):
  path = os.path.join(root,page['href']+ext)
  file_save(path,T.load(E,page['template']+ext).render(this=page,**kwargs))

def search_save(path,content):
  path = os.path.join(root,'search',path)+'.json'
  json_save(path,content,indent=1)