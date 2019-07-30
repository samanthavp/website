import os, shutil, json, copy

VERBOSE = 3

def make_key(str):
  return "{{{{{}}}}}".format(str)

def slen(obj):
  return len(obj) if isinstance(obj,list) else \
         1 if isinstance(obj,str) else 0

def load_json(fname):
  with open(fname,"r") as f:
    return json.load(f)

def status(message,level=1):
  if VERBOSE is not False and (level <= VERBOSE):
    print([
      "-"*50+"\n {}\n"+"-"*50,
      " + {}",
      "   > {}",
      "     . {}",
    ][level].format(message),flush=True)

class Template:
  def __init__(self,src):
    self.src = src
    self.name = os.path.split(os.path.splitext(src)[0])[1]
    self.load_content()
  
  def get_content(self):
    return self.content

  def load_content(self):
    if not os.path.exists(self.src):
      raise FileNotFoundError("Cannot find Template file: {}".format(self.src))
    with open(self.src,"r") as f:
      self.content = f.read()

  def get_sub_content(self,subs):
    status("sub: {}".format(self.name),level=2)
    # TODO: implement subs as a list
    sublens = list(set(map(slen,subs.values())))
    assert len(sublens) <= 2, "Cannot substitute lists of different lengths."
    N = max(sublens)
    content = [self.get_content()[:] for i in range(N)]
    for key,value in subs.items():
      if slen(value) <= 1:
        value = [value for i in range(N)]
      fkey = make_key(key)
      if content[0].find(fkey) is not -1: # TODO: slow
        status("key: {}".format(key),level=3)
      for i in range(N):
        content[i] = content[i].replace(make_key(key),str(value[i]))
    return "".join(content)

  def set_sub_content(self,subs):
    self.content = self.get_sub_content(subs)

def get_templates(folder):
  return {os.path.splitext(file)[0]: Template(os.path.join(base,file))
    for base,dirs,files in os.walk(folder)
      for file in files}

def dictpop(d,k):
  d.pop(k)
  return d

def dictmerge(d,*ds):
  for di in ds:
    d.update(di)
  return d

if __name__ == "__main__":
  outpath = os.path.join("html") # TODO -> config file
  inpath  = os.path.join("src")
  status("Loading: Content",level=0)
  # TODO: -> content dict
  pages    = load_json(os.path.join(inpath,"content","pages.json"))
  episodes = load_json(os.path.join(inpath,"content","episodes.json"))
  profiles = load_json(os.path.join(inpath,"content","team.json"))
  listens  = load_json(os.path.join(inpath,"content","listen-on.json"))
  templates = {
    "pages": get_templates(os.path.join(inpath,"templates","pages")),
    "parts": get_templates(os.path.join(inpath,"templates","parts")),
    "nav":   get_templates(os.path.join(inpath,"templates","nav")),
  }
  
  status("Building: parts",level=0)
  
  status("Building: navbar",level=1)
  content = ""
  for page in pages:
    content += templates["nav"]["li"].get_sub_content(page)
  templates["parts"]["nav"].set_sub_content({"li":content})

  status("Building: team",level=1)
  content = ""
  for profile in profiles:
    profile.update({"id":profile["name"].replace(' ','-')})
    content += templates["parts"]["profile-tile"].get_sub_content(profile)
  templates["parts"]["team"].set_sub_content({"profile-tile":content})

  status("Building: episode-tiles",level=1)
  content = ""
  for episode in episodes:
    content += templates["parts"]["episode-tile"].get_sub_content(episode)
  templates["parts"]["episodes"].set_sub_content({"episode-tile":content})

  status("Building: episodes",level=1)
  for episode in episodes:
    episode.update({"root":".."})
    # epi = copy.copy(episode)
    # links = "".join([
    #   templates["parts"]["link"].get_sub_content(link)
    #   for link in epi.pop("links")
    # ])
    subs = {k:t.get_sub_content({
        "title":episode["title"],
        "root": episode["root"],
        # "links": links,
      }) for k,t in templates["parts"].items()}
    subs.update({"episode": templates["parts"]["episode"].get_sub_content(episode)})
    with open(os.path.join(outpath,"episodes",str(episode["no"])+".html"),"w") as f:
      f.write(templates["pages"]["episode"].get_sub_content(subs))
  
  status("Building: Listen Links",level=1)
  links = ""
  for listen in listens:
    links += templates["parts"]["listen-on"].get_sub_content(listen)
  templates["parts"]["listen-on"].content = links

  status("Building: Pages",level=0)
  for page in pages:
    status("Building: {}".format(page["href"]),level=1)
    key = os.path.splitext(page["href"])[0]
    subs = {k:t.get_sub_content({
        "title": page["title"],
        "root": ".",
      }) for k,t in templates["parts"].items()}
    subs.update({"root":"."})
    if page["title"] == "HOME":
      subs.update({"blubrry":episodes[0]["blubrry"]})
    with open(os.path.join(outpath,page["href"]),"w") as f:
      f.write(templates["pages"][key].get_sub_content(subs))
  status("Done",level=0)

# TODO: head needs to resolve relative links for nested pages
