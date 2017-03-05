import os
from time import time, sleep
from ulauncher.helpers import singleton
from ulauncher.config import CACHE_DIR
from ulauncher.utils.KeyValueDb import KeyValueDb
from ulauncher.utils.run_async import run_async


class FileQueries(KeyValueDb):
    __last_put_time = 0
    __last_save_time = 0

    @classmethod
    @singleton
    def get_instance(cls):
        db = cls(os.path.join(CACHE_DIR, 'file_borwser_queries.db'))
        db.open()
        return db

    def __init__(self, basename):
        super(FileQueries, self).__init__(basename)
        self._init_autosave()

    @run_async(daemon=True)
    def _init_autosave(self):
        """
        We don't want to trigger I/O on every insert to the DB,
        so we will commit changes asynchronously every 20 sec
        """
        while True:
            if self.__last_save_time < self.__last_put_time:
                self.commit()
                self.__last_save_time = time()
            sleep(20)

    def put(self, path):
        self.__last_put_time = time()
        super(FileQueries, self).put(path, self.__last_put_time)

    def find(self, path):
        return super(FileQueries, self).find(path) or 0
