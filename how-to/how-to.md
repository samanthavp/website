# How-To: Raw Talk Podcast Website

## Overview
- this site is live right now at https://rawtalkpodcast.com
- pages are hosted through github pages at: https://raw-talk-podcast.github.io/website
- the source code is on github at: https://github.com/raw-talk-podcast/website

## Building

### Requirements
- [python 3](https://www.python.org/downloads/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- GitHub account on the [RTP organization](https://github.com/raw-talk-podcast)
- [Jekyll](https://jekyllrb.com/docs/installation/) (for testing)

### First Time
Open a terminal and type the `commands` below
- `cd <dir>`, where `<dir>` is the folder where you want the project to live 
- `git clone https://github.com/raw-talk-podcast/website .` will download the git repo to `<dir>`. Do not miss the `.`

### Testing
Open a terminal and type the `commands` below
- `cd <dir>`, where `<dir>` is the folder where the project lives
- `cd html`
- `jekyll serve` will launch the website for testing on your computer.
- open a web browser and enter the url: `http://localhost:4000`
- `CTRL+C` to close the jekyll session when you're done.
- Hard refresh (`CRLT+F5` in browser) to see any changes during the session.

## Meta-Data
Authors:
- [Jesse Knight](jesse.x.knight@gmail.com)

Last updated:
2019-09-24
