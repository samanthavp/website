import os
import re
import json

VERBOSE = 2
SRC = 'src'
OUT = 'html'

def make_key(string):
  return "{{{{{}}}}}".format(string)

def make_slug(string):
  return str(string).replace(" ","-").lower()

def fname_content(name,ext=".json"):
  return os.path.join(SRC,"content",str(name)+ext)

def fname_page(name,ext=".html"):
  return os.path.join(OUT,make_slug(name)+ext)

def fname_episode(name,ext=".html"):
  return os.path.join(OUT,"episodes",make_slug(name)+ext)

def slen(obj):
  return len(obj) if isinstance(obj,list) else \
         1 if isinstance(obj,str) else 0

def load_json(fname):
  status("Loading: {}".format(fname),level=1)
  with open(fname,"r") as f:
    return json.load(f)

def status(message,level=1):
  if VERBOSE is not False and (level <= VERBOSE):
    print([
      "-"*50+"\n{}\n"+"-"*50,
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
  return {
      os.path.splitext(file)[0]: Template(os.path.join(base,file))
      for base,dirs,files in os.walk(folder)
      for file in files
    }

def dictpop(d,k):
  d.pop(k)
  return d

def dictmerge(d,*ds):
  for di in ds:
    d.update(di)
  return d

if __name__ == "__main__":
  # ================================================================================================
  status("Loading: Content",level=0)
  content = {
    key: load_json(fname_content(key))
    for key in ["pages","team","listen-on"]
  }
  content["episodes"] = [
    load_json(os.path.join(path,fname))
    for path,_,fnames in os.walk(fname_content("episodes",ext=""))
    for fname in sorted(fnames, key = lambda fn: int(re.split('(\d*)\.json',fn)[1]))
  ][::-1]
  templates = {
    key: get_templates(os.path.join(SRC,"templates",key))
    for key in ["pages","parts","nav"]
  }
  # ================================================================================================
  status("Building: parts",level=0)
  # ------------------------------------------------------------------------------------------------
  status("Building: navbar",level=1)
  html = ""
  for page in content["pages"]:
    html += templates["nav"]["li"].get_sub_content(page)
  templates["parts"]["nav"].set_sub_content({
      "li": html,
    })
  # ------------------------------------------------------------------------------------------------
  status("Building: team",level=1)
  html = ""
  for profile in content["team"]:
    profile.update({
        "id": make_slug(profile["name"]),
      })
    html += templates["parts"]["tile-profile"].get_sub_content(profile)
  templates["parts"]["team"].set_sub_content({
      "tile-profile": html,
    })
  # ------------------------------------------------------------------------------------------------
  status("Building: episode-content",level=1)
  for episode in content["episodes"]:
    episode.pop("links")
    episode.update({
      "authors": ", ".join(episode["authors"]),
    })
  # ------------------------------------------------------------------------------------------------
  status("Building: tile-episodes",level=1)
  html = ""
  for episode in content["episodes"]:
    html += templates["parts"]["tile-episode"].get_sub_content(episode)
  templates["parts"]["episodes"].set_sub_content({
      "tile-episode": html,
    })
  # ------------------------------------------------------------------------------------------------
  status("Building: episodes",level=1)
  for episode in content["episodes"]:
    episode.update({"root":".."})
    subs = {
      key: temp.get_sub_content({
          "title":episode["title"],
          "root": episode["root"],
        })
        for key,temp in templates["parts"].items()
      }
    subs.update({
        "episode": templates["parts"]["episode"].get_sub_content(episode)
      })
    with open(fname_episode(episode["no"]),"w") as f:
      f.write(templates["pages"]["episode"].get_sub_content(subs))
  # ------------------------------------------------------------------------------------------------
  status("Building: Listen-On",level=1) # TODO: listen-on & social from same template, different content
  html = ""
  for listen in content["listen-on"]:
    html += templates["parts"]["listen-on"].get_sub_content(listen)
  templates["parts"]["listen-on"].content = html # HACK
  # ================================================================================================
  status("Building: Pages",level=0)
  for page in content["pages"]:
    # ----------------------------------------------------------------------------------------------
    status("Building: {}".format(page["href"]),level=1)
    key = os.path.splitext(page["href"])[0]
    subs = {
      key: temp.get_sub_content({
          "title": page["title"],
          "root": ".",
        })
        for key,temp in templates["parts"].items()
      }
    subs.update({
        "root": ".",
      })
    if page["title"] == "HOME":
      subs.update({
          "blubrry": content["episodes"][0]["blubrry"]
        })
    with open(fname_page(page["href"],ext=""),"w") as f:
      f.write(templates["pages"][key].get_sub_content(subs))
  # ================================================================================================
  status("Done",level=0)

# TODO: head needs to resolve relative links for nested pages
