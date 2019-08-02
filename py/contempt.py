import os
import re
import utils

def make_key(string):
  return '{{{{{}}}}}'.format(string)

def key_regex():
  return re.escape(make_key('x')).replace('x','(.*?)')

def get_keys(string):
  return utils.unique(re.findall(key_regex(),string))

def make_name(path):
  return os.path.split(os.path.splitext(path)[0])[1]

class Template():
  def __init__(self,content=None,name=None,fname=None):
    self.content = content
    self.name = name
    if fname is not None:
      self.from_file(fname)
      if self.name is None:
        self.name = make_name(fname)

  def __str__(self):
    return '< Template \'{}\':\n{}\n>'.format(self.name,self.content)

  def __repr__(self):
    return '< Template \'{}\'>'.format(self.name)

  def from_file(self,fname):
    with open(fname,'r') as f:
      self.content = f.read()
    return self

  def to_file(self,fname,root='.'):
    with open(fname,'w') as f:
      f.write(self.get_sub_content({ 'root' : os.path.relpath(root,fname) }))

  def get_keys(self):
    return get_keys(self.content)

  def get_sub_content(self,subs,join=True,sortby=None,indent=True):
    if not subs:
      return self.content
    subs = utils.flatten(subs)
    if sortby is not None:
      subs = sorted(subs,key=sortkey)
    keys = self.get_keys()
    content = [self.content for i in range(len(subs))]
    for s,sub in enumerate(subs):
      for key,value in sub.items():
        fkey = make_key(key)
        if fkey in self.content:
          if indent:
            value = utils.indent(str(value),len(re.findall('( *)'+re.escape(fkey),self.content)[0]))
          content[s] = content[s].replace(fkey,value.rstrip())
    if join is True:
      return ''.join([''.join(cs) for cs in content])
    else:
      return [''.join(cs) for cs in content]

  def set_sub_content(self,subs,sortby=None,indent=True):
    self.content = self.get_sub_content(subs,join=True,sortby=sortby,indent=indent)
    return self

def drill(template,templates,contents,join=True):
  subs = {}
  for key in template.get_keys():
    if key in templates:
      subs.update({ key : drill(templates[key], templates, contents) })
  template = Template(template.get_sub_content(subs), name=template.name)
  subs = []
  if template.name in contents:
    for isubs in utils.flatten(contents[template.name]):
      tmap = isubs.pop('templates',{})
      for ckey,tkey in tmap.items():
        itemplate = templates[tkey]
        csub = Template(drill(itemplate,templates,contents),itemplate.name).get_sub_content(isubs)
        isubs.update({ ckey : csub })
      subs += [isubs]
  return template.get_sub_content(subs,join=join) 

def get_templates(path,exts='.html'):
  return {
    make_name(fname): Template(fname=fname)
    for fname in utils.iter_files(path,exts=exts)
  }

def get_content(path,exts='.json'):
  parts = path.split(os.path.sep)
  content = utils.path_dict(path,exts='.json',fun=utils.load_json)
  for part in parts:
    content = content[part]
  return content
