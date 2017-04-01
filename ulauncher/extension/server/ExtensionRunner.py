import os
import logging
from StringIO import StringIO
from ulauncher.helpers import singleton
from ulauncher.config import CACHE_DIR
from subprocess import Popen, PIPE, STDOUT

ETENSIONS_DIR = os.path.join(CACHE_DIR, 'extensions')


class ExtensionRunner(object):

    @classmethod
    @singleton
    def get_instance(cls):
        return cls()

    def __init__(self):
        self.extensions_dir = ETENSIONS_DIR
        self.logger = logging.getLogger(type(self))
        self.running_extensions = set()

    def run(self, extension_id):
        stdout = StringIO()
        stderr = StringIO()
        proc = Popen(['python', os.path.join(self.extensions_dir, extension_id, 'main.py')],
                     stdout=PIPE,
                     stderr=PIPE)
        for line in iter(proc.stdout.readline, b''):
            self.logger.log(line.rstrip)

    def stop(self, extension_id):
        pass

    def is_running(self, extension_id):
        return extension_id in self.running_extensions
