# Editing + Maintaining the Raw Talk Podcast Website

Author: [Jesse Knight](mailto:jesse.x.knight@protonmail.com)

Last updated: 2022-05-24

*Some terminal commands may need modification for Windows*

----------------------------------------------------------------------------------------------------
## Overview
- the site is hosted through github pages at: https://raw-talk-podcast.github.io/website
- the domain name https://rawtalkpodcast.com simply points to the above link
- the source code is on github at: https://github.com/raw-talk-podcast/website
- the site pages are static html pages within `web`
- the site pages are generated using python in based on html templates and json data (content)
- see also: the [overview](https://github.com/raw-talk-podcast/website/blob/master/docs/overview.md) page
----------------------------------------------------------------------------------------------------
## Building the site

### Requirements
- [python~3.7+](https://www.python.org/downloads/)
  - [jinja2](https://pypi.org/project/Jinja2/) package
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [GitHub](https://github.com/join) account with access to the [RTP organization](https://github.com/raw-talk-podcast)

### Getting started
After installing the requirements...
Open a terminal and enter the `commands` below
- `cd <dir>`, where `<dir>` is the folder where you want the project to live
- `git clone https://github.com/raw-talk-podcast/website .` will download the git repo to `<dir>`; do not miss the `.`
- review the folder structure in `docs/overview.md`; briefly:
  - `html/` contains the static html pages and resources (js, css, images, etc.) which are the site
  - `src/` contains `html` template snippets and `json` data which are used to generate pages in `html/`
  - `py/` contains python code to generate pages in `html/` from the contents of `src/`

### Building the site
From a terminal at `<dir>` enter the `commands` below
- `python src/py/build.py`

Depending on the value of `utils.verbose` in `src/py/utils.py`, a printout of steps during the site build will appear.
Set the value of `utils.verbose = None` for no printout, `utils.verbose = 3` for maximum printout.

If you get an error like `json.decoder.JSONDecodeError`, you have a syntax error in a json file. Set `utils.verbose = 1` or higher to find the offending file, and you can paste the file contents into https://jsonlint.com to help find the error.

### Testing
To check the files in `web/` are ready to go live...
From a terminal at `<dir>` enter the `commands` below
- `cd web`
- `python test.py` will launch the website for testing on your computer.
- open a web browser and enter the url: `http://localhost:4000`
- test whatever you need to - everything should work as if the site were live, but it is not yet
- when you're done, press `CTRL+C` to close the local server session
- to see changes during the session, press `CRLT+F5` in browser to reload any cached data

### Publishing
Only after verifying your changes via testing:
From a terminal at `<dir>` enter the `commands` below
- `git diff` to view your changes; use arrow keys to scroll up and down and type `q` to quit
- `git add .` to collect all changes you made
- `git commit -m "<message>"` where `<message>` is a short description of the changes you made
- `git push origin master` to push your changes to the online github repository; this will not change the live site yet
- `git subtree push --prefix web origin gh-pages` this will push your changes to the live site (the `gh-pages` branch)

If you know what you're doing, feel free use more advanced `git` commands, etc.

It may take 10 - 90 seconds for changes to appear on https://rawtalkpodcast.com.
Make sure you're not loading from the cache by refreshing with  `CTRL+F5` in your browser.

### Oh Sh*t

Something broke? Don't panic...
The live site won't be affected by any goofs
unless you've executed the last step of **Publishing**;
even then, most goofs can be easily rolled back.

Depending when you realize you made a goof,
there are different ways you can take with git to fix things.
Please see [here](https://git.seveas.net/undoing-all-kinds-of-mistakes.html)
for a great resource on this topic.

In case the goof was pushed to `gh-pages`,
simply repeat the last step of **Publishing** after fixing things locally
to overwrite the goofed files on `gh-pages` branch.

----------------------------------------------------------------------------------------------------
## Adding an episode
To add episode number ##, you need to add a few images and 2 json files,
based on the info in the Promotions doc on Drive;
and update the announcements.
1. images: 
  - make a new folder `web/img/episodes/##/`
  - add to this folder:
    - the horizontal preview or "tile" image (`512 x 342` pixels)
    - one square image per guest (`512 x 512` pixels)
      - filenames should be `first-last.jpg` and you *must* use the (image sizes) above
2. episode json:
  - copy an existing json file >97 in `src/content/episodes/` and name it `##.json`
    - episodes <97 use an old format with slightly different required content
  - update the fields for the new episode
    - `mp3` is the full url for the hosted mp3 file (must be published on podbean):
      - go to https://rawtalkims.podbean.com/
      - click the "Download" button for episode ##
      - right-click the big green "Download" button on the new page
      - select "copy link (address)"
      - replace `/download/` with `/web/`
    - `notes`: be sure to replace any `"` within the notes with `\"`
    - `authors`, `prod_team` and `tags` are currently unused.
  - json format is not forgiving; consider validating your json (https://jsonlint.com) before trying to build the site
3. transcript json:
  - at release: copy 0.json in `src/content/transcripts/` and name it `##.json`
    - this is a temporary file
  - when the transcript is ready: see **Adding a Transcript** (below)
4. update the announcements:
  - edit the file `src/content/announcements.json`
    - title: "Now Live! ## (title)"
    - date: "YYYY, MMM, DD"
    - href: "/episode/##"
5. re-build & test the site:
  - See **Building the site** and **Testing** above
  - The changed files (using `git diff`) should be:
    - `src/content/episodes/##.json` - new file
    - `web/img/episodes/##/*` - some new images
    - `web/episodes.html` - new episode tile within page
    - `web/episode/##.html` - new episode page
    - `web/episode/(##-1).html` - new left arrow for next episode
    - `web/index.html` - updated announcement
    - `web/latest/intex.html` - points to the new episode
    - `web/search/episodes.json` - updated search-able episode data
6. Publish the changes
  - Are you sure?
  - See **Publishing** above

## Adding a Transcript

The episode team uses [Otter](https://otter.ai) to generate a rough transcript
and then cleans it manually within Otter.
The transcript should be exported to .txt with default settings.

- rename & move the .txt file to `.tmp/##.txt`
- run `python src/py/transcript.py ##`; this will:
  - parse the .txt file and print some log info;
    - ensure the duration looks right and speaker names are correct & unique
  - copy the current `src/content/transcripts/##.json` to `.tmp/##.bak.json` (backup)
  - overwrite the (temporary) `src/content/transcripts/##.json` with the complete transcript
- (re)-**Build** & **Publish** the site
