#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

RELATIVE_URLS=True
SITEURL = "https://www.peterka.me/preview"

FEED_DOMAIN = SITEURL

OUTPUT_PATH="/srv/http/html/peterka.me/preview"
DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
DISQUS_SITENAME = "preview-peterka-me"
