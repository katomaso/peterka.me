#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path

AUTHOR = 'Tomas Peterka'
SITENAME = 'Tomas Peterka'
SITEURL = 'localhost:8000'

DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
LOCALE = 'en_GB.UTF-8'
APP_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = '/srv/apps/peterka.me/content'
ARTICLE_PATHS = ('articles', 'contributions', 'projects', 'coding')
STATIC_PATHS = ('static', )
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

# theme is private to pelican instance
#THEME = os.path.join(APP_DIR, "themes", "twenty-html5up")
THEME=os.path.join(APP_DIR, "themes", "Peli-Kiera")

# plugins are shared for all pelican instances
PLUGIN_PATHS = ['/srv/apps/pelican/plugins']
PLUGINS = ['readtime', 'neighbors']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = [
   # ("Resume", "author/tomas-peterka.html"),
]

# Template variables
NAME = AUTHOR
TAGLINE = SITESUBTITLE = 'Software Researcher'
ADDRESS = "Prague, Czechia"
MAIL = EMAIL = "tomas@peterka.me"
PHONE = "+420605437994"

SOCIAL = [
    ('twitter', 'https://twitter.com/almo_cz'),
    ('linkedin', 'https://linkedin.com/in/tpeterka'),
    ('github', 'https://github.com/katomaso'),
]
TWITTER = 'almo_cz'
LINKEDIN = 'tpeterka'
GITHUB = 'katomaso'
WEBSITE = 'peterka.me'

COPYRIGHT = AUTHOR
DEFAULT_PAGINATION = 30
LAST_ARTICLE_COUNT = 9

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

AUTHOR_CSS = 'resume.css'
PROFILE = """
I was born in Prague. Studied part of my Master's degree in Linköping, Sweden. Moved to Montreal, Canada to work for
Guavus as a big data developer. Returned to Prague to work as a researcher in machine learning for search engine Seznam.cz.
Then I moved to Lille, France to work for Nexedi S.A. as a R&amp;D Assistant. After a social burnout I returned to Prague
to work for Deutsche Telekom in software innovations.
<br><br>
I have ENFP personality thus I am more on the "having overview" side rather than "digging in details". I am talkative extravert
that is easily getting by with people. I am good in wrapping my head around complicated problems and simple them down. Luckily,
I can then explain comprehensively to interested parties and - moreover - I love writing documentation and presenting.
"""

CAREER =""" 
I consider myself a software engineer, researcher and evangelist. Having worked in different fields from big data applications
modern web development to machine learning gave me a broad skillset and a technological overview. My favourite technologies 
are Go, Python, Javascript, no/SQL databases, Docker, cloud, CI/CD pipelines and any tool for automatisation that makes your 
flow less error prone.
<br><br>
I work with multiple technologies such as Big data (Spark, Flink, Nifi, Kafka), Machine Learning (Python, Tensorflow,
scikit-learn), Backends (Python, Go), Frontends (Web Components, Vue.js), Databases (PostgreSQL, MongoDB, CouchDB,
Impala) and Cloud (Docker, lxc, CI/CD pipelines).
"""

OPINIONS = """
I love making complex things simple and intuitive. When I build software I build it for people - usable, intuitive and performant.
Computers are here to help not to annoy us.
<br><br>
I value companies working toward better future. In order to get there, we need guaranteed freedom, equal access to information and  education.
All that is possible thanks to amazing initiatives and companies that share knownledge, support development and creativity and
inspire people by showing new ways of doing things. Just to name a few: Julia Evans, Rob Pike, Kurzgezagt, Ocean Cleanup and of course Elon!
<br><br>
I care about health and the environment. Sustainability, together with education, is the key to human survival. I believe that 
the future is local-oriented and inevitably distributed. I think that we should clean up our planet and submit to the Paris Climate Agreement. 
I believe in smaller, more local, and sustainable farming using novel approaches like permaculture or fish-plant cooperation. Going smaller 
would strenghten position of cities and divide the power. That would increase accountability and transparency in the governmental process.
"""

PROJECT_INTRO = 'Open source projects and contributions.'

PROJECTS = [
    {
        'title': 'django-market',
        'tagline': 'Web based virtual marketplace supporting multiple shops, products and offers.',
        'url': 'https://github.com/katomaso/django-market'
    },
    {
        'title': 'django-bit-category',
        'tagline': 'Category implementation using bit-wise ID for fast sub-categories selection.',
        'url': 'https://github.com/katomaso/django-bit-category'
    },
    {
        'title': 'cowyo',
        'tagline': 'Simple wiki server in Go lang.',
        'url': 'https://github.com/schollz/cowyo'
    }
]

LANGUAGES = [
    {
        'name': 'Czech',
        'description': 'Native'
    },
    {
        'name': 'English',
        'description': 'Professional'
    },
    {
        'name': 'Français',
        'description': 'Conversational'
    }
]


EXPERIENCES = [
    {
        'job_title': 'Software Engineer',
        'time': 'Jun 2018 - present',
        'company': 'Deutche Telekom IT, Prague',
        'details': """<ul>
<li>Transition to cloud;</li>
<li>Designing and implementing CI/CD pipeline in Gitlab;</li>
<li>Packaging and installation tool for Mediation Zone</li>
</ul>
"""
    },
    {
        'job_title': 'Assistant R&D/CTO',
        'time': 'Feb 2017 - Apr 2018',
        'company': 'Nexedi S.A, France',
        'details': """<ul>
<li>Porting user interface of a complex ERP system to single-page web application;</li>
<li>ERP system develppment in Python;</li>
<li>Contributing to multiple free projects;</li>
<li>Integration of fully software defined LTE base station into cloud management platform (vRAN).</li>
</ul>
"""
    },
    {
        'job_title': 'Researcher Programmer',
        'time': 'Dec 2016 - Feb 2018',
        'company': 'Seznam.cz, Czechia',
        'details': """<ul>
<li>Basic research in machine learning and notably neural networks using TensorFlow;</li>
<li>Natural Language Processing using embedded representation;</li>
<li>Steering future direction of research topics.</li>
</ul>
"""
    },
    {
        'job_title': 'Software Engineer',
        'time': 'Sep 2014 - Sep 2015',
        'company': 'Guavus Inc, Canada',
        'details': """<ul>
<li>Big Data pipeline using mainly Spark and Impala from the Apache stack;</li>
<li>Construction of Data Warehouse (Oracle), ingestion procedures (Kafka, Oracle) and Data Lakes (Oracle).</li>
</ul>
"""
    },
    {
        'job_title': 'Fullstack Developer',
        'time': 'Mar 2010 - Apr 2013',
        'company': 'WebExpo s.r.o., Czechia',
        'details': """Python+Django Web development of a conference site where core components
comprise mass mailing, online payments, REST communication with accounting backend and others.
"""
    }
]

EDUCATIONS = [
    {
        'degree': "MSc in Machine Learning, CTU",
        'meta': "Master's thesis on astronomical spectra classification using neural networks",
        'time': '2016'
    },
    {
        'degree': "Bachalors in Software Engineering, CTU",
        'meta': "Bachelor's thesis on ETL system design according to astronomical data standards",
        'time': '2012'
    }
]

LINKS = []
