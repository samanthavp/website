# How-To: Raw Talk Podcast Website

## Overview
- the site is hosted through github pages at: https://raw-talk-podcast.github.io/website
- the domain name https://rawtalkpodcast.com points to the above link
- the source code is on github at: https://github.com/raw-talk-podcast/website
- the site pages are static `html` pages
- the site pages are generated using python based on `html` templates and `json` data

## Building the site

### Requirements
- [python 3](https://www.python.org/downloads/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- GitHub account on the [RTP organization](https://github.com/raw-talk-podcast)
- [Jekyll](https://jekyllrb.com/docs/installation/) (for testing)

### Getting started
Open a terminal and type the `commands` below
- `cd <dir>`, where `<dir>` is the folder where you want the project to live
- `git clone https://github.com/raw-talk-podcast/website .` will download the git repo to `<dir>`. Do not miss the `.`
- review the folder structure in `how-to/overview.md`. Briefly:
  - `html/` contains the static html pages and resources (js, css, images, etc.) which are the site
  - `src/` contains `html` template chunks and `json` data which are used to generate pages in `html/`
  - `py/` contains python code to generate pages in `html/` from the contents of `src/`

### Building the site
Open a terminal and type the `commands` below
- `cd <dir>`, where `<dir>` is the folder where the project lives
- `python py/make.py`
Depending on the value of `ct.verbose` in `py/make.py`, a printout of steps during the site build will appear.
Set the value of `ct.verbose = None` for no printout, `ct.verbose = 3` for maximum printout.

### Testing
Open a terminal and type the `commands` below
- `cd <dir>`, where `<dir>` is the folder where the project lives
- `cd html`
- `jekyll serve` will launch the website for testing on your computer.
- open a web browser and enter the url: `http://localhost:4000`
- when you're done, press `CTRL+C` to close the jekyll session
- to see changes during the session, press `CRLT+F5` in browser to reload any cached data

### Publishing
Only after verifying the results of your changes using Testing:
Open a terminal and type the `commands` below
- `cd <dir>`, where `<dir>` is the folder where the project lives
- `git add .` to collect all changes you made
- `git commit -m "<message>"` where `<message>` is a short description of the changes you made
- `git push origin master` to push your changes to the online github repository. This will not change the live site yet.
- `git subtree push --prefix html origin gh-pages` this will push your changes to the live site.
If you know what you're doing, feel free use more advanced `git` commands, etc.

## Blame
Authors:
- [Jesse Knight](jesse.x.knight@gmail.com)

Last updated:
2019-09-25
