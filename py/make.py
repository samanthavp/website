import os
from copy import copy
import contempt as ct
import utils

def make_slug(string):
  return str(string).replace(' ','-').lower()

def make_fname(*args,ext='.html'):
  return os.path.join(*args[:-1],os.path.splitext(args[-1])[0]+ext)

def sort(dicts,reverse=False):
  def key(item):
    for cast,key in [(float,'no'),(float,'sort'),(str,'name'),(str,'title')]:
      if key in item:
        return cast(item[key])
    return None
  return sorted(dicts,key=key,reverse=reverse)

def get_content():
  path = os.path.join('src','content')
  c = ct.get_content(path)
  # sort episodes & team
  episodes = sort(c['episodes'].values(),reverse=True)
  team     = sort(c['team'].values())
  # collect the navbar before adding episodes to pages
  navpages = ['HOME','EPISODES','TEAM','CONTACT']
  c['nav-item'] = [page for page in c['page'] if page['title'] in navpages]
  write_index(episodes,'episodes')
  # clean up some fields on the fly
  for page in c['page']:
    page['next'] = None
    page['prev'] = None
  for member in team:
    member['id'] = make_slug(member['name'])
  for episode in episodes:
    episode['title']     = '#{}: {}'.format(episode['no'],episode['title'])
    episode['templates'] = utils.odict([('links','link'),('body','episode')])
    episode['href']      = os.path.join('episodes',str(episode['no'])+'.html')
    episode['authors']   = ' and '.join(episode['authors'])
    episode['next']      = episode['no']+1 if episode['no'] < len(episodes) else None
    episode['prev']      = episode['no']-1 if episode['no'] > 1 else None
    c['page'].append(episode)
  # duplicate some content TODO: is this expensive?
  c['tile-episode'] = episodes
  c['tile-profile'] = team
  return c

def make_pages():
  ct.status('GENERATING PAGES',level=0)
  # pre-compute some elements
  templates['navbar'].content = ct.drill(templates['navbar'],templates,contents)
  templates['footer'].content = ct.drill(templates['footer'],templates,contents)
  # generate complete templates
  return ct.drill(templates['page'],templates,contents,join=False)

def write_pages():
  # write to file
  ct.status('WRITING PAGES',level=0)
  for page,spec in zip(pages,contents['page']):
    ct.Template(page).to_file(make_fname(root,spec['href']),root=root)

def write_index(content,name):
  ct.status('Writing index: {}'.format(name),level=1)
  utils.save_json(content,make_fname(root,'search',name,ext='.json'),indent=1)

ct.verbose = None
root = 'html'
templates = ct.get_templates(os.path.join('src','templates'))
contents  = get_content()
pages     = make_pages()
write_pages()
ct.status('DONE',level=0)
