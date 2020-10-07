Title: Creating administration for backend-less blog
Description: One step on my path to native-paid articles on backend-less blog is to create administration interface for ordinary users and a convenient interface for myself
Status: draft
Date: 2020-07-15

# The question

How do you publish an article on backend-less blog?

Things I tried

## inotify

iNotify is linux kernel feature to observe events happening on iNodes. It reports event such as IN_OPEN, IN_DIR, IN_CLOSE_WRITE, IN_CLOSE_NOWRITE, IN_MOVE. I was planning
to bind re-generation of a blog on IN_CLOSE_WRITE event. Unfortunetely, this event is not triggered every time a change is made. I suspect internal buffering that
prevents this event from ocuring. Quite often, I see IN_CLOSE_NOWRITE when I edit a file through WebDAV. I consulted documentation and thought that the issue is
that WebDAV was accessing the folder via `symlink` but this has proven false. To be completely honest - the event IN_CLOSE_WRITE happens most of the time but not always.

Seriously I don't understand

```
katomaso@havel:/srv/apps/peterka.me/content/articles$ ls -lc
-rw-rw---- 1 www-data www-data 1459 Jul 15 19:21 2020-07_Creating-an-admin-panel.md
```
See the change-time of the last item? 19:21. 

Now watch the events with timestamps.

```
2020-07-15 19:27:42 PATH=[content/articles/] FILENAME=[] EVENT_TYPES=['IN_OPEN', 'IN_ISDIR']
2020-07-15 19:27:42 PATH=[content/articles/] FILENAME=[] EVENT_TYPES=['IN_ACCESS', 'IN_ISDIR']
2020-07-15 19:27:42 PATH=[content/articles/] FILENAME=[] EVENT_TYPES=['IN_CLOSE_NOWRITE', 'IN_ISDIR']
2020-07-15 19:28:28 PATH=[content/articles/] FILENAME=[2020-07_Creating-an-admin-panel.md] EVENT_TYPES=['IN_MOVED_TO']
2020-07-15 19:28:28 PATH=[content/articles/] FILENAME=[2020-07_Creating-an-admin-panel.md] EVENT_TYPES=['IN_CLOSE_WRITE']
CRITICAL: TypeError: can't compare offset-naive and offset-aware datetimes
2020-07-15 19:28:31 PATH=[content/projects/] FILENAME=[] EVENT_TYPES=['IN_OPEN', 'IN_ISDIR']
2020-07-15 19:28:31 PATH=[content/projects/] FILENAME=[] EVENT_TYPES=['IN_ACCESS', 'IN_ISDIR']
2020-07-15 19:28:31 PATH=[content/projects/] FILENAME=[] EVENT_TYPES=['IN_CLOSE_NOWRITE', 'IN_ISDIR']
```

```
katomaso@havel:/srv/apps/peterka.me/content/articles$ ls -lc
-rw-rw---- 1 www-data www-data 1827 Jul 15 19:28 2020-07_Creating-an-admin-panel.md
```

Now the change-time is 19:28 as you can see that IN_CLOSE_WRITE event got through while editing this article you are reading now.

But When I do a small change that fits in some buffer? Really small?

```
2020-07-15 19:37:15 PATH=[content/articles/] FILENAME=[2020-07_Creating-an-admin-panel.md] EVENT_TYPES=['IN_MOVED_TO']
```

Then I `ls -lc` that flushes the buffer.

```
2020-07-15 19:37:29 PATH=[content/articles/] FILENAME=[2020-07_Creating-an-admin-panel.md] EVENT_TYPES=['IN_CLOSE_WRITE']
```

Tiny change does not even trigger any iEvent on the file being edited! _2020-04_ChromeOS-Linux.md_ is a different article.
```
2020-07-15 19:38:34 PATH=[content/articles/] FILENAME=[2020-04_ChromeOS-Linux.md] EVENT_TYPES=['IN_OPEN']
```

When I `cat 2020-07_Creating-an-admin-panel.md` I don't get IN_CLOSE_WRITE for my file but the content is correct. Buffers again I suppose?

```
2020-07-15 19:40:13 PATH=[content/articles/] FILENAME=[2020-04_ChromeOS-Linux.md] EVENT_TYPES=['IN_CLOSE_NOWRITE']
2020-07-15 19:40:13 PATH=[content/articles/] FILENAME=[2018-06_LTE-overview.md] EVENT_TYPES=['IN_OPEN']
2020-07-15 19:40:13 PATH=[content/articles/] FILENAME=[2018-06_LTE-overview.md] EVENT_TYPES=['IN_ACCESS']
```

and issuing `ls -lc` does not flush the buffer either but displays correct modification time `19:38`.

```
katomaso@havel:/srv/apps/peterka.me/content/articles$ ls -lc
-rw-rw---- 1 www-data www-data 3294 Jul 15 19:38 2020-07_Creating-an-admin-panel.md
```

Whatever I do, no matter how big chunks of text I am adding (not appending - inserting), I cannot force IN_WRITE_CLOSE event on my file.
I always see events on different files that do not make sense. Maybe an error in the pyinotify library? Improbable. Therefor I turned down
the idea of using iNotify. So what's next possibility? Well scanning the files for changes "manually".

## File watch

Watching all files in a folder for change seems to me as a big overhead. Imagine having hundreds of blogs and scanning all files for changes
each second or so. That would generate quite lot of spinning of my SSDs! So let's watch `.deploy` and `.preview` files instead. For example
if they are empty let's regenerate and fill them with some useful information such as when the last re-generation happened and which articles
were processed.

