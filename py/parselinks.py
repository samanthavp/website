import re
import json
import clipboard
from collections import OrderedDict as odict

# 1. copy the div on the old raw talk podcast containing the links
# 2. run this script (reads from / writes to your clipboard)
# 3. paste the result into the #.json file

html = clipboard.paste()
links = []
for link in re.findall("<h3><a href=\"(.*?)\">(.*?)<\/a><\/h3>",html):
  links.append(odict([
    ("title", link[1]),
    ("href", link[0])
  ]))
clipboard.copy(json.dumps(links,indent=2).replace("{\n    ","{ "))
