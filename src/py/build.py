import os
import utils
import jinja2 as ji

utils.log('loading',1)

C = utils.json_drill('src/content')
T = ji.FileSystemLoader('src/templates')
E = ji.Environment(
  loader=T,
  trim_blocks=True,
  lstrip_blocks=True,
)

sorter = lambda e: e['no']
X = dict(
  listfun     = lambda l: ', '.join(l[0:-1])+', and '+l[-1],
  slugfun     = lambda s: s.lower().replace(' ','-'),
  announce    = C['announcement'],
  navitems    = C['pages'],
  socials     = C['socials'],
  players     = C['players'],
  positions   = C['positions'],
  team        = sorted(C['team'].values(),key=sorter),
  events      = sorted(C['events'].values(),key=sorter,reverse=True),
  episodes    = sorted(C['episodes'].values(),key=sorter,reverse=True),
  root        = 'http://www.rawtalkpodcast.com',
)
def ogfun(href,img='brand/logo.png',width=512,height=342,descr=''):
  return {
    'url':    X['root']+'/'+href,
    'img':    X['root']+'/img/'+img,
    'width':  width,
    'height': height,
    'descr':  descr,
  }

utils.log('saving',1)

utils.search_save('episodes',X['episodes'])
for episode in X['episodes']:
  no = str(episode['no'])
  href = 'episode/'+no
  descr = episode['notes'][0:episode['notes'].find(' ',150)]
  episode.update(
    href        = href,
    title       = '#{} {}'.format(no,episode['title']),
    og          = ogfun(href,href+'/'+episode['img_tile'],descr=descr),
    transcripts = C['transcripts'][no],
  )
  utils.page_save(E,T,episode,**X)
for event in X['events']:
  href = 'event/'+event['slug']
  event.update(
    template = 'event-'+event['template'],
    href     = href,
    og       = ogfun(href,href+'/'+event['img'],width=512,height=287),
  )
  utils.page_save(E,T,event,**X)
for page in C['pages']:
  href = page['slug']
  page.update(
    template = page['slug'],
    href     = href,
    og       = ogfun(href,**page['og'])
  )
  utils.page_save(E,T,page,**X)
latest = dict(
  template = 'redirect',
  href     = 'latest/index',
  to       = '/episode/'+str(X['episodes'][0]['no']),
)
utils.page_save(E,T,latest)
E404 = dict(
  template = '404',
  href     = '404',
  og       = ogfun('404'),
)
utils.page_save(E,T,E404)
