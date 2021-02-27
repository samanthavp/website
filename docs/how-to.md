# How-To:
# Editing the Raw Talk Podcast Website

Author: [Jesse Knight](mailto:jesse.x.knight@gmail.com)

Last updated: 2019-11-08

----------------------------------------------------------------------------------------------------
## Overview
- the site is hosted through github pages at: https://raw-talk-podcast.github.io/website
- the domain name https://rawtalkpodcast.com simply points to the above link
- the source code is on github at: https://github.com/raw-talk-podcast/website
- the site pages are static `html` pages
- the site pages are generated using python in based on `html` templates and `json` data (content)
----------------------------------------------------------------------------------------------------
## Building the site

### Requirements
- [python~3](https://www.python.org/downloads/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [GitHub](https://github.com/join) account on the [RTP organization](https://github.com/raw-talk-podcast)

### Getting started
After installing the requirements...
Open a terminal and enter the `commands` below
- `cd <dir>`, where `<dir>` is the folder where you want the project to live
- `git clone https://github.com/raw-talk-podcast/website .` will download the git repo to `<dir>`; do not miss the `.`
- review the folder structure in `how-to/overview.md`; briefly:
  - `html/` contains the static html pages and resources (js, css, images, etc.) which are the site
  - `src/` contains `html` template snippets and `json` data which are used to generate pages in `html/`
  - `py/` contains python code to generate pages in `html/` from the contents of `src/`

### Building the site
From a terminal at `<dir>` enter the `commands` below
- `python py/make.py`

Depending on the value of `ct.verbose` in `py/make.py`, a printout of steps during the site build will appear.
Set the value of `ct.verbose = None` for no printout, `ct.verbose = 3` for maximum printout.

If you get an error like `json.decoder.JSONDecodeError`, you have a syntax error in a json file. Set `ct.verbose = 1` or higher to find the offending file, and you can paste the file contents into https://jsonlint.com to help find the error.

### Testing
From a terminal at `<dir>` enter the `commands` below
- `cd html`
- `python test.py` will launch the website for testing on your computer.
- open a web browser and enter the url: `http://localhost:4000`
- when you're done, press `CTRL+C` to close the local server session
- to see changes during the session, press `CRLT+F5` in browser to reload any cached data

### Publishing
Only after verifying your changes via testing:
From a terminal at `<dir>` enter the `commands` below
- `git diff` to view your changes; use arrow keys to scroll up and down and type `q` to quit
- `git add .` to collect all changes you made
- `git commit -m "<message>"` where `<message>` is a short description of the changes you made
- `git push origin master` to push your changes to the online github repository; this will not change the live site yet
- `git subtree push --prefix html origin gh-pages` this will push your changes to the live site (the `gh-pages` branch)

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
    - the horizontal preview or "tile" image (`512 x 342` pixels)
    - the vertical main image (`683 x 1024` pixels)
  - filenames should be `first-last-description.jpg` or similar, and you must use the (image sizes) above
2. json:
  - copy an existing json file in `src/content/episodes/` and name it `##.json`
  - update the fields for the new episode
    - `blubrry` is the 8-digit episode ID which appears after `https://blubrry.com/rawdataims/` on the new Blubrry episode page; please wrap in `"quotes"` even though it is a number
    - `tags` is unused; please leave empty `[]` for now
    - `authors` are the author(s) of the `notes`, for now
    - not all episodes have `links`; browse a few json files to see how to format them
  - json format is not forgiving; consider validating your json (https://jsonlint.com) before trying to build the site
3. update the announcements:
  - edit the file `src/content/announcements.json`
4. re-build & test the site:
  - See [Building the site] and [Testing] above
  - The changed files (using `git diff`) should be:
    - `src/content/episodes/##.json` - new file
    - `html/img/episodes/##/(horizontal).jpg` - new tile image
    - `html/img/episodes/##/(vertical).jpg` - new main image
    - `html/episodes.html` - new episode tile within page
    - `html/episode/##.html` - new episode page
    - `html/episode/(##-1).html` - new left arrow for next episode
    - `html/index.html` - updated announcements
    - `html/latest/intex.html` - points to the new episode
    - `html/search/episodes.json` - updated search-able episode data
5. Publish the changes
  - Are you sure?
  - See [Publishing] above
