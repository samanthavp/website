# How-To:
# Editing the Raw Talk Podcast Website

Author: [Jesse Knight](jesse.x.knight@gmail.com)

Last updated: 2019-09-25

----------------------------------------------------------------------------------------------------
## Overview
- the site is hosted through github pages at: https://raw-talk-podcast.github.io/website
- the domain name https://rawtalkpodcast.com simply points to the above link
- the source code is on github at: https://github.com/raw-talk-podcast/website
- the site pages are static `html` pages
- the site pages are generated using python in based on `html` templates and `json` data
----------------------------------------------------------------------------------------------------
## Building the site

### Requirements
- [python~3](https://www.python.org/downloads/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [GitHub](https://github.com/join) account on the [RTP organization](https://github.com/raw-talk-podcast)
- [Jekyll](https://jekyllrb.com/docs/installation/) (for testing, requires [Ruby](https://www.ruby-lang.org/en/downloads/))

### Getting started
After installing the requirements...
Open a terminal and enter the `commands` below
- `cd <dir>`, where `<dir>` is the folder where you want the project to live
- `git clone https://github.com/raw-talk-podcast/website .` will download the git repo to `<dir>`; do not miss the `.`
- review the folder structure in `how-to/overview.md`; briefly:
  - `html/` contains the static html pages and resources (js, css, images, etc.) which are the site
  - `src/` contains `html` template chunks and `json` data which are used to generate pages in `html/`
  - `py/` contains python code to generate pages in `html/` from the contents of `src/`

### Building the site
From a terminal at `<dir>` enter the `commands` below
- `python py/make.py`

Depending on the value of `ct.verbose` in `py/make.py`, a printout of steps during the site build will appear.
Set the value of `ct.verbose = None` for no printout, `ct.verbose = 3` for maximum printout.

### Testing
From a terminal at `<dir>` enter the `commands` below
- `cd html`
- `jekyll serve` will launch the website for testing on your computer.
- open a web browser and enter the url: `http://localhost:4000`
- when you're done, press `CTRL+C` to close the jekyll session
- to see changes during the session, press `CRLT+F5` in browser to reload any cached data

### Publishing
Only after verifying your changes via testing:
From a terminal at `<dir>` enter the `commands` below
- `git diff` to view your changes; use arrows to scroll and type `q` to quit
- `git add .` to collect all changes you made
- `git commit -m "<message>"` where `<message>` is a short description of the changes you made
- `git push origin master` to push your changes to the online github repository; this will not change the live site yet
- `git subtree push --prefix html origin gh-pages` this will push your changes to the live site

If you know what you're doing, feel free use more advanced `git` commands, etc.

It may take 10 - 90 seconds for changes to appear on https://rawtalkpodcast.com.
Make sure you're not loading from the cache by refreshing with  `CTRL+F5` in your browser.

----------------------------------------------------------------------------------------------------
## Adding an episode
To add episode number ##, you need to add 2 images and 1 json file,
based on the info in the Comms notes on Dropbox;
and update the announcements.
1. images: 
  - make a new folder `html/img/episodes/##/`
  - add to this folder:
    - the horizontal preview or "tile" image (`512 x 342`)
    - the vertical main image (`683 x 1024`)
  - filenames should be `first-last-description.jpg` or similar, and note (image sizes) above
2. json:
  - copy an existing json file in `src/content/episodes/` and name it `##.json`
  - update the fields for the new episode
    - not all episodes have `links`; browse a few json files to see how to format them
    - `blubrry` is the 8-digit episode ID which appears after `https://blubrry.com/rawdataims/` on the new Blubrry episode page; please wrap in `"quotes"` even though it is a number
    - `tags` is unused; please leave empty `[]` for now
    - `authors` are the author(s) of the `notes`
  - json format is not forgiving; consider validating your json [with this](https://jsonlint.com)
3. update the announcements:
  - edit the file `src/content/announcements.json`
4. re-build & test the site:
  - See [Building the site] and [Testing] above
  - The changed files should be:
    - `src/content/episodes/##.json` - new file
    - `html/img/episodes/##/(horizontal).jpg` - new tile image
    - `html/img/episodes/##/(vertical).jpg` - new main image
    - `html/episodes.html` - new episode tile within page
    - `html/episode/##.html` - new episode page
    - `html/episode/(##-1).html` - new left arrow for next episode
    - `html/index.html` - updated announcements
    - `html/search/episodes.json` - updated search-able episode data
5. Publish the changes
  - Are you sure?
  - See [Publishing] above
