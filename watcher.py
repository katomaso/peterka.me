#!/usr/bin/env python

import sys
import time
import subprocess
import threading
import logging
import inotify.adapters
import datetime as dt
from pathlib import Path

CONTENT_FOLDER = Path("content")
logger = logging.getLogger("watcher")

class Regen:
    TIMEOUT = dt.timedelta(seconds=3600)
    SLEEP_TIME = 2.0 # sec

    def __init__(self, trigger, config):
        self.locked = False
        self.trigger = trigger
        self.config = config
        self.end = None
        self.thread = None

    def __run(self):
        while dt.datetime.now() < self.end:
            time.sleep(Regen.SLEEP_TIME)
            if not self.trigger.exists():
                self.regen()
                continue
            if self.trigger.stat().st_size <= 1:
                self.regen()
                continue
        logger.info(f"Thread watching {self.trigger} quits because time {self.end} is up!")
        self.thread = None

    def watch(self):
        if self.locked:
            logger.debug(f"Watch called but {self.trigger} is locked because generation is in progress")
            return
        self.end = dt.datetime.now() + Regen.TIMEOUT
        if self.thread is not None:
            logger.debug(f"End updated to {self.end} for {self.trigger} and quit")
            return
        self.thread = threading.Thread(target=lambda: self.__run())
        logger.info(f"Starting thread to watch {self.trigger}")
        self.thread.start()

    def regen(self):
        logger.debug("Regenerate called")
        if self.locked:
            logger.debug(f"Regenerate for {self.trigger} already in progress - quit")
            return

        self.locked = True
        try:
            logger.info(f"Regenerating site for trigger {self.trigger}")
            trigger_file = self.trigger.open("wt")
            trigger_file.write(f"Generation started at {dt.datetime.now()}")
            subprocess.call(["pelican", "-s" , self.config], stdout=trigger_file, stderr=trigger_file)
        finally:
            trigger_file.close()
            time.sleep(0.001)
            self.locked = False
        logger.info("Regenerating completed")

def main():
    i = inotify.adapters.Inotify()
    i.add_watch(str(CONTENT_FOLDER))
    
    publish = Regen(CONTENT_FOLDER / ".publish", "publishconf.py")
    publish.watch()

    preview = Regen(CONTENT_FOLDER / ".preview", "previewconf.py")
    preview.watch()

    while True:
        for event in i.event_gen(yield_nones=False):
            (_, type_names, path, filename) = event
            logger.debug("{:%Y-%m-%d %H:%M:%S} PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
              dt.datetime.now(), path, filename, type_names))

        publish.watch()
        preview.watch()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
