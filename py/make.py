import os
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
  episodes    = sort(c['episodes'].values(),reverse=True)
  transcripts = c['transcripts']
  team        = sort(c['team'].values())
  # collect the navbar before adding episodes to pages
  navpages = ['HOME','ABOUT','TEAM','EPISODES','JOIN US','CONTACT']
  c['nav-item'] = [page for page in c['page'] if page['title'] in navpages]
  write_index(episodes,'episodes')
  # clean up / build some fields on the fly
  for page in c['page']:
    page['next'] = None
    page['prev'] = None
  for i,member in enumerate(team):
    member['id'] = make_slug(member['name'])
    member['title'] = utils.splitfmt(member['title'],' & ','<span class="no-wrap">{}</span>')
    header = (i == 0) or (member['team-name'] != team[i-1]['team-name'])
    member.update({'templates':{'maybe-header-team':'header-team' if header else 'none'}})
  c['redirect'] = []
  for i,episode in enumerate(episodes):
    episode['title']     = '#{} {}'.format(episode['no'],episode['title'])
    episode['templates'] = utils.odict([('links','link'),('transcripts','transcript'),('body','episode')])
    episode['href']      = os.path.join('episode',str(episode['no']))
    episode['authors']   = ' and '.join(episode['authors'])
    episode['prod-team'] = ', '.join(episode['prod-team'])
    episode['next']      = episode['no']+1 if episode['no'] < len(episodes) else None
    episode['prev']      = episode['no']-1 if episode['no'] > 1 else None
    header = (episode['no'] == len(episodes)) or (episode['season'] < episodes[i-1]['season'])
    episode['templates'].update({'maybe-header-season':'header-season' if header else 'none'})
    episode['description'] = episode['notes'][0:256].replace('\"','\'')
    episode['img-meta']    = 'http://www.rawtalkpodcast.com/img/episodes/'+str(episode['no'])+'/'+episode['img-tile']
    episode['transcripts'] = transcripts[str(len(episodes)-i)]
    c['page'].append(episode)
    hrefold = episode['href-old'] if 'href-old' in episode else None
    c['redirect'].append({'href-old':hrefold,'href-new':'{{root}}/'+episode['href']})
  c['redirect'].append({'href-old':'latest/index.html','href-new':'{{root}}/'+episodes[0]['href']})
  c['tile-highlight'] = [episode for episode in episodes if episode['no'] in c['highlights']]
  # duplicate some content TODO: is this expensive?
  c['tile-episode'] = episodes
  c['tile-profile'] = team
  c['tile-announce'] = c['announcements']
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
  for redirect in contents['redirect']:
    if redirect['href-old'] is not None:
      page = templates['redirect'].get_sub_content(redirect)
      ct.Template(page).to_file(make_fname(root,redirect['href-old']),root=root)

def write_index(content,name):
  ct.status('Writing index: {}'.format(name),level=1)
  utils.save_json(content,make_fname(root,'search',name,ext='.json'),indent=1)

ct.verbose = 2
root = 'web'
templates = ct.get_templates(os.path.join('src','templates'))
contents  = get_content()
pages     = make_pages()
write_pages()
ct.status('DONE',level=0)
