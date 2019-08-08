import os
import re
import utils

verbose = False
verb = {
  'rw':    1,
  'drill': 1,
  'sub':   2,
  'key':   3,
}

def make_key(string):
  return '{{{{{}}}}}'.format(string)

def key_regex():
  return re.escape(make_key('x')).replace('x','(.*?)')

def get_keys(string):
  return utils.unique(re.findall(key_regex(),string))

def make_name(path):
  return os.path.split(os.path.splitext(path)[0])[1]

def status(msg,level):
  if (verbose >= level) and (verbose is not None) and (level is not None):
    print([
      '-'*50+'\n{}\n'+'-'*50,
      '+ {}',
      '  > {}',
      '    - {}',
    ][level].format(msg))

def load_json(fname):
  status('Loading: {}'.format(fname),level=verb['rw'])
  return utils.load_json(fname)

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
    status('Loading: {}'.format(fname),level=verb['rw'])
    with open(fname,'r') as f:
      self.content = f.read()
    return self

  def to_file(self,fname,root='.'):
    status('Writing: {}'.format(fname),level=verb['rw'])
    with open(fname,'w') as f:
      f.write(self.get_sub_content({ 'root' : os.path.relpath(root,os.path.split(fname)[0]) }))

  def get_keys(self):
    return get_keys(self.content)

  def get_sub_content(self,subs,join=True,sortby=None,indent=True):
    # n.b.: {} yields self.content while [] yields empty conteny (zero repetitions)
    if subs == {}:
      return self.content
    if subs == []:
      return '' if join else []
    subs = utils.flatten(subs)
    if sortby is not None:
      subs = sorted(subs,key=sortby)
    content = [self.content for i in range(len(subs))]
    status('sub: {} ({})'.format(self.name,len(subs)),level=verb['sub'])
    for s,sub in enumerate(subs):
      for key,value in sub.items():
        fkey = make_key(key)
        if fkey in self.content:
          if indent:
            value = utils.indent(str(value),len(re.findall('( *)'+re.escape(fkey),self.content)[0]))
          status('key: {}'.format(key),level=verb['key'])
          content[s] = content[s].replace(fkey,value.rstrip())
    if join is True:
      return ''.join([''.join(cs) for cs in content])
    else:
      return [''.join(cs) for cs in content]

  def set_sub_content(self,subs,sortby=None,indent=True):
    self.content = self.get_sub_content(subs,join=True,sortby=sortby,indent=indent)
    return self

def drill(template,templates,contents,join=True):
  status('Drill: {}'.format(template.name),level=1)
  # adding templates: singleton -> subs = {}
  subs = {}
  for key in template.get_keys():
    if key in templates:
      subs.update({ key : drill(templates[key], templates, contents) })
  template = Template(template.get_sub_content(subs), name=template.name)
  # adding content: possibly repeated -> subs = []
  if template.name in contents:
    subs = []
    # assume the content is a list of dicts
    for isubs in utils.flatten(contents[template.name]):
      # the content may specify nested templates
      tmap = isubs.pop('templates',{})
      # note: please use odict to resolve content in nested templates (inner first)
      for ckey,tkey in tmap.items():
        itemplate = Template(templates[tkey].content,tkey)
        if ckey in isubs:
          itemplate.set_sub_content(isubs[ckey])
        # drill the nested template
        csub = Template(drill(itemplate,templates,contents),itemplate.name).get_sub_content(isubs)
        isubs.update({ ckey : csub })
      # append the content from this dict in the list
      subs += [isubs]
  else: # if no subs, make sure to return content at least once
    subs = {}
  return template.get_sub_content(subs,join=join)

def get_templates(path,exts='.html'):
  status('LOADING TEMPLATES',level=0)
  return {
    make_name(fname): Template(fname=fname)
    for fname in utils.iter_files(path,exts=exts)
  }

def get_content(path,exts='.json'):
  status('LOADING CONTENT',level=0)
  parts = path.split(os.path.sep)
  content = utils.path_dict(path,exts=exts,fun=load_json)
  for part in parts:
    content = content[part]
  return content
