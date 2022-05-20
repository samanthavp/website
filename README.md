# Raw Talk Podcast Website

This site is live now at: https://rawtalkpodcast.com

Last updated: 2022-05-20

Maintainer:
  - [Mauro Mendez Mora](mauro.mendez@mail.utoronto.ca) - current
  - [Jesse Knight](mailto:jesse.x.knight@protonmail.com) - retired

## About Taw Talk

> Raw Talk is a graduate student-run podcast at the University of Toronto
  about medical science, and the people who make it happen.
  We focus on the journeys, perspectives, and expertise of
  health researchers, professionals, students, patients, and community members
  at the University of Toronto and beyond.

## About the Website

- **web/**: static files that are pushed to `gh-pages` branch, then accessible by
  [GitHub Pages](https://raw-talk-podcast.github.io/website)
- **src/**: files to build the site using
  [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
  - **content/**: `json` content, e.g. episode info
  - **templates/**: `html` templates, e.g. page layouts
  - **py/**: Python code to combine the above and write non-asset files to `web`
- **docs/**: guide for how to edit & maintain the site
- Audio files are hosted & distributed by
  [PodBean](https://rawtalkims.podbean.com)
