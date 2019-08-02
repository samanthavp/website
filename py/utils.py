import os
import json
from collections import OrderedDict as odict
from functools import reduce

def status(message,level=1):
  if VERBOSE is not False and (level <= VERBOSE):
    print([
      "-"*50+"\n{}\n"+"-"*50,
      " + {}",
      "   > {}",
      "     . {}",
    ][level].format(message),flush=True)

def load_json(fname):
  with open(fname,'r') as f:
    return json.load(f)

def listlen(obj):
  return len(obj) if isinstance(obj,list) else 1 if isinstance(obj,str) else 0

def indent(string,n=0):
  spaces = ' '*n
  return string.replace('\n','\n'+spaces)

def flatten(obj):
  out = []
  if hasattr(obj,'__iter__') and not isinstance(obj,(str,dict)):
    for el in obj:
      out.extend(flatten(el))
  else:
    out.append(obj)
  return out

def unique(iterobj):
  u = set()
  return [obj for obj in iterobj if not (obj in u or u.add(obj))]

def iter_files(paths,exts=None):
  def checkext(path):
    return exts is None or os.path.splitext(path)[1] in flatten(exts)
  for path in flatten(paths):
    if os.path.isfile(path):
      if checkext(path):
        yield path
    elif os.path.isdir(path):
      for root,_,files in os.walk(path):
        for f in sorted(files):
          fpath = os.path.join(root,f)
          if checkext(fpath):
            yield fpath
    else:
      raise ValueError('Cannot find path: {}'.format(path))

def path_dict(paths,exts=None,fun=None):
  def drill_dict(dd,keys):
    def drill(d,key):
      if key not in d:
        d.update({key: odict()})
      return d[key]
    return reduce(drill,keys,dd)
  if fun is None:
    fun = lambda f: f
  pdict = odict()
  for file in iter_files(paths,exts=exts):
    split = file.split(os.path.sep)
    fname = os.path.splitext(split[-1])[0]
    drill_dict(pdict,split[:-1]).update({fname: fun(file)})
  return pdict
