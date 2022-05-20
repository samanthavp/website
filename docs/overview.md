`DNE`: do not edit!
`AG`: automatically generated - edits will be overwritten

Last updated: 2022-05-20, Jesse Knight

```
├── README.md                           # readme file
|
├── how-to/                             # guidance docs
|   ├── overview.md                     # overview of project files and folders
|   └── how-to.md                       # how-to guide for editing, building, publishing the site
|
├── web/                                # code which represents the live site
|   ├── css/                            # css files
|   |   ├── bootstrap.min.css           # DNE imported css
|   |   └── rawtalkpodcast.css          # custom css
|   ├── docs/                           # files that users might view/download - usually PDF
|   |   └── recruit/                    # position descriptions - PDF
|   ├── episode/                        # AG folder containing each pages for each episode
|   |   ├── 1.html                      # AG "Episode 1" page
|   |   ...                             # AG ...
|   ├── event/                          # AG folder containing each pages for each event
|   |   ├── ai.html                     # AG "ai" event page
|   |   ...                             # AG ...
|   ├── fonts/                          # DNE fonts
|   ├── img/                            # all images for the live site
|   |   ├── brand/                      # images related to "Raw Talk Podcast" brand
|   |   ├── episode/                    # images for episodes
|   |   |   ├── 1/                      # images for "Episode 1" (old style)
|   |   |   |   ├── tile.jpg            # horizontal (preview tile) image
|   |   |   |   └── vertical.jpg        # vertical (main episode page) image
|   |   |   ...                         # ...
|   |   |   ├── 97/                     # images for "Episode 97"
|   |   |   |   ├── tile.jpg            # horizontal (preview tile) image
|   |   |   |   └── first-last.jpg      # square image for guest "First Last"
|   |   |   ...                         # ...
|   |   ├── event/                      # images for events
|   |   |   ├── ai/                     # images for "ai" event
|   |   |   ...                         # ...
|   |   ├── icon/                       # small icons and logos (facebook, play-button, etc.)
|   |   ├── sponsors/                   # images from "sponsors" or collaborators
|   |   └── team/                       # images of the team
|   |       ├── first-last-rt.jpg       # "raw-talk (rt)" image of "First Last" for modal
|   |       ├── first-last-tq.jpg       # "three-quarters (tq)" image of "First Last" for tiles
|   |       ...                         # ...
|   ├── js/                             # javascript files
|   |   ├── audioplayer.js              # custom js - for player on episode pages
|   |   ├── bootstrap-4.3.1.min.js      # DNE imported js - framework
|   |   ├── fuse-3.4.5.min.js           # DNE imported js - for search
|   |   ├── jquery-3.4.1.min.js         # DNE imported js - jquery
|   |   └── rawtalkpodcast.js           # custom js - basically just search (consider renaming)
|   ├── latest/index.html               # AG redirect page pointing to most recent episode
|   ├── search/                         # AG json files for performing search using fuse.js
|   |   └── episodes.json               # AG json file of search-able episode content
|   ├── 404.html                        # AG "error 404" page
|   ├── about.html                      # AG "about" page
|   ├── CNAME                           # DNE url redirect file
|   ├── contact.html                    # AG "contact" page
|   ├── episodes.html                   # AG "episode" overview page
|   ├── events.html                     # AG "events" overview page
|   ├── index.html                      # AG "home page" (default landing)
|   ├── team.html                       # AG "team" overview page, contains modal for each member
|   └── test.py                         # python script for local testing of site
|
└── src/                                # template and content files 
    ├── content/                        # json files containing only "data" for AG files
    |   ├── episodes/                   # json files of "data" for all episodes
    |   |   ├── 1.json                  # json file of "data" for "Episode 1"
    |   |   ...                         # ...
    |   ├── events/                     # json files of "data" for all events
    |   |   ├── ai.json                 # json file of "data" for "ai" event
    |   |   ...                         # ...
    |   ├── team/                       # json files of "data" for all team members
    |   |   ├── first-last.json         # json file of "data" for "First Last"
    |   |   ...                         # ...
    |   ├── transcripts/                # json files of transcripts for all episodes
    |   |   ├── 1.json                  # json file of transcript for "Episode 1"
    |   |   ...                         # ...
    |   ├── announcement.json           # json announcement to display at top of index.html
    |   ├── pages.json                  # list of main pages and meta-data for social media previews
    |   ├── players.json                # list of linked apps where you can listen to the podcast
    |   ├── positions.json              # list of positions we are currently recruiting
    |   └── socials.json                # list of our social media
    ├── py/                             # python files for building the site
    |   ├── build.py                    # main script for generating any AG files in web/
    |   ├── transcript.py               # script for parsing txt from Otter -> json file
    |   └── utils.py                    # utility functions
    └── templates/                      # html files into which content "data" will be substituted
        ├── 404.html                    # complete error 404 page
        ├── about.html                  # main content of the "about" page
        ├── contact.html                # main content of the "contact" page
        ├── episode-old.html            # main content of any single "episode" page - old style
        ├── episode.html                # main content of any single "episode" page - new style
        ├── episodes.html               # main content of the "episodes" overview page
        ├── event-panel.html            # core content of any single "event" page - panel style
        ├── event-series.html           # core content of any single "event" page - series style
        ├── event.html                  # main content or any single "event" page - (wrapper)
        ├── event.html                  # main content of the "events" overview page
        ├── index.html                  # main content of the "index" (home) page
        ├── page.html                   # wrapper for all pages, including meta-data, header, footer
        ├── redirect.html               # snippet for redirecting links
        └── team.html                   # main content of the "team" page
```
