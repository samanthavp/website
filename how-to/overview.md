```
├── README.md                           # readme file
|
├── how-to/                             # guidance docs
|   ├── overview.md                     # overview of project files and folders
|   └── how-to.md                       # how-to guide for editing, building, publishing the site
|
├── html/                               # code which renders the live site
|   ├── CNAME                           # DNE url redirect file
|   ├── css/                            # css files
|   |   ├── bootstrap.min.css           # DNE imported css
|   |   └── style.css                   # custom css
|   ├── fonts/                          # DNE fonts
|   ├── js/                             # javascript files
|   |   ├── bootstrap-4.3.1.min.js      # DNE imported js
|   |   ├── fuse-3.4.5.min.js           # DNE imported js
|   |   ├── jquery-3.4.1.min.js         # DNE imported js
|   |   └── main.js                     # custom js
|   ├── index.html                      # AG "home page"
|   ├── about.html                      # AG "about" page
|   ├── contact.html                    # AG "contact" page
|   ├── episodes.html                   # AG "episode" overview page
|   ├── team.html                       # AG "team" overview page, contains popups
|   ├── episode/                        # AG folder containing each pages for each episode
|   |   ├── 1.html                      # AG "Episode 1" page
|   |   ...                             # AG ...
|   ├── 2016/                           # AG ugly redirect pages for compatibility with legacy links
|   ...                                 # AG ...
|   ├── 2019/                           # AG ugly redirect pages for compatibility with legacy links
|   ├── img/                            # all images for the live site
|   |   ├── brand/                      # images related to "Raw Talk Podcast" brand
|   |   ├── episodes/                   # images for episodes
|   |   |   ├── 1/                      # images for "Episode 1"
|   |   |   |   ├── horizontal.jpg      # horizontal (preview tile) image
|   |   |   |   └── vertical.jpg        # vertical (main episode page) image
|   |   |   ...                         # ...
|   |   ├── icons/                      # small icons and logos (facebook, play-button, etc.)
|   |   ├── sponsors/                   # images from our "sponsors" or collaborators
|   |   └── team/                       # images of the team
|   |       ├── first-last-rt.jpg       # "raw-talk (rt)" image of "First Last" for popup
|   |       ├── first-last-tq.jpg       # "three-quarters (tq)" image of "First Last" for tiles
|   |       ...                         # ...
|   └── search/                         # AG json files for performing search using fuse.js
|       └── episodes.json               # AG json file of search-able episode content
|
├── py/                                 # python files for building the site
|   ├── make.py                         # main script for generating any AG files in html/
|   ├── contempt.py                     # "content-template" framework for generating AG files
|   └── utils.py                        # utility functions
|
└── src/                                # template and content files 
    ├── content/                        # json files containing only "data" for AG files
    |   ├── announcements.json          # list of announcements to display at top of index.html
    |   ├── highlights.json             # episode numbers to highlight on about.html
    |   ├── listen-on.json              # list of linked apps where you can listen to the podcast
    |   ├── page.json                   # list of main pages and meta-data for social media previews
    |   ├── social.json                 # list of our social media
    |   ├── episodes/                   # json files of "data" for all episodes
    |   |   ├── 1.json                  # json file of "data" for "Episode 1"
    |   |   ...                         # ...
    |   └── team/                       # json files of "data" for all team members
    |       ├── first-last.json         # json file of "data" for "First Last"
    |       ...                         # ...
    └── templates/                      # html files into which content "data" will be substituted
        ├── about.html                  # main content of the "about" page
        ├── amazon.html                 # content explaining how the amazon program works
        ├── contact.html                # main content of the "contact" page
        ├── episode.html                # main content of any single "episode" page
        ├── episodes.html               # main content of the "episodes" overview page
        ├── footer.html                 # content of the footer
        ├── header.html                 # content of the header, including navbar, title, arrows
        ├── header-season.html          # snippet of season header on "episodes" page
        ├── header-team.html            # snippet of team header on "team" page (mobile only)
        ├── head.html                   # html <head>
        ├── home.html                   # main content of the "index" (home) page
        ├── link.html                   # snippet for any text links
        ├── listen-on.html              # snippet for a "listen-on" link with icon
        ├── modal-profile.html          # content to generate the team member popup (modal)
        ├── navbar.html                 # wrapper of the navbar list, including search
        ├── nav-item.html               # snippet for items in the navbar
        ├── none.html                   # a hack to produce no content if content is "None"
        ├── page.html                   # wrapper for all pages content
        ├── redirect.html               # snippet for redirecting from legacy links
        ├── social.html                 # snippet for each social media link
        ├── team.html                   # main content of the "team" page
        ├── tile-announce.html          # snippet for each announcement on "index" page
        ├── tile-episode.html           # snippet for each episode tile on "episodes" page
        ├── tile-highlight.html         # snippet for each highlighted episode on "about" page
        └── tile-profile.html           # snippet for each team member preview on "team" page
```
`DNE`: do not edit!
`AG`: automatically generated
