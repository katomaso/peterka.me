Title: Django BIT Category
Category: Projects
Summary: Fast category implementation using bit-wise IDs and according operations
Slug: django-bit-category
Status: published
Date: 2013-04-11
Modified: 2020-04-21

Django-bit-category was a necessity for faster category management using generic RDBMS.

When I started working on django-market back in 2009, this was one of the pain-points
of using django and python3 - pretty much nothing existed. I needed a fast tree-like
structure for categories and subcategories. I didn't know about (b)tree data storage
of databases so I implemented my own.

Bit-wise keys for categories work on binary prefixes. You count with 32bit integers
and set up how many levels of categories you need to support. Let's say we have
4 levels of categories. Then you have 8bit for items in each category which can
be either sub-categories or leaves. In this setup, you will have 256 root categories
and each can have 256 subcategories and so on.

An example of category keys


```
XXXXX000000000000000000000000000  # mask for the root category
00001000000000000000000000000000  # first root
00010000000000000000000000000000  # second root
00011000000000000000000000000000  # third root

00001000010000000000000000000000  # first child of the first root
00001000100000000000000000000000  # second child of the first root
```

I find this project quite elegant. Even though it does not count with keys in DBs.
It expects the database to do full-scan or some linear search through the keys.

I had a lot of fun working on this project. It is my first (and I think last as well)
project that I have published to pip https://pypi.org/project/django-bit-category/

The source is, of course, publicly available on https://github.com/katomaso/django-bit-category
I am especialy proud of the readme and usability of the project. I doubt anybody used it
except me but I am still proud of it as my first published project.