#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marissa Utterberg'
SITENAME = 'CLE.pyd Pelican Theme Demo'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }
FAVICON = 'favicon.ico'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = './clepyd-theme'

PLUGINS_PATHS = ['./pin_to_top']
PLUGINS = ['pin_to_top']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('PyLadies', 'https://www.pyladies.com'),
        ('Cleveland PyLadies', 'https://clepyladies.github.io/pyladies-official/'),
        ('CLE.py', 'https://www.clepy.org'),
        ('PSF', 'https://www.python.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True