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
  team        = sorted(C['team'].values(),key=sorter),
  events      = sorted(C['events'].values(),key=sorter,reverse=True),
  episodes    = sorted(C['episodes'].values(),key=sorter,reverse=True),
)

utils.log('saving',1)

for episode in X['episodes']:
  episode.update(
    template    = 'episode',
    href        = 'episode/'+str(episode['no']),
    title       = '#{} {}'.format(episode['no'],episode['title']),
    transcripts = C['transcripts'][str(episode['no'])],
  )
  utils.page_save(E,T,episode,**X)
for event in X['events']:
  event.update(
    template    = 'event-'+event['template'],
    href        = 'event/'+event['slug'],
  )
  utils.page_save(E,T,event,**X)
for page in C['pages']:
  page.update(
    template    = page['slug'],
    href        = page['slug'],
  )
  utils.page_save(E,T,page,**X)

utils.search_save('episodes',X['episodes'])