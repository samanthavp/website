import os
from copy import copy
import contempt as ct
from utils import odict

def make_slug(string):
  return str(string).replace(' ','-').lower()

def make_fname(*args,ext='.html'):
  return os.path.join(*args[:-1],os.path.splitext(args[-1])[0]+ext)

def sort(dicts,reverse=False):
  def key(item):
    for cast,key in [(int,'no'),(int,'sort'),(str,'name'),(str,'title')]:
      if key in item:
        return cast(item[key])
  return sorted(dicts,key=key,reverse=reverse)

def get_content():
  path = os.path.join('src','content')
  c = ct.get_content(path)
  # sort episodes & team
  episodes = sort(c['episodes'].values(),reverse=True)
  team     = sort(c['team'].values())
  # collect the navbar before adding episodes to pages
  c['navitem'] = copy(c['page'])
  # clean up some fields on the fly
  for member in team:
    member['id'] = make_slug(member['name'])
  for episode in episodes:
    episode['title']     = '#{}: {}'.format(episode['no'],episode['title'])
    episode['templates'] = odict([('links','link'),('body','episode')])
    episode['href']      = os.path.join('episodes',str(episode['no'])+'.html')
    episode['authors']   = ' and '.join(episode['authors'])
    c['page'].append(episode)
  # duplicate some content TODO: is this expensive?
  c['tile-episode'] = episodes
  c['tile-profile'] = team
  return c

def make_pages(root='html'):
  # pre-compute some elements
  templates['navbar'].content = ct.drill(templates['navbar'],templates,contents)
  templates['footer'].content = ct.drill(templates['footer'],templates,contents)
  # generate complete templates
  pages = ct.drill(templates['page'],templates,contents,join=False)
  # and write to file
  for page,spec in zip(pages,contents['page']):
    ct.Template(page).to_file(make_fname(root,spec['href']),root=root)

templates = ct.get_templates(os.path.join('src','templates'))
contents  = get_content()
make_pages()
