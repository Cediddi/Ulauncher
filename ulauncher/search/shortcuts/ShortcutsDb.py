import os
from uuid import uuid4
from time import time
from operator import itemgetter
from ulauncher.helpers import singleton
from ulauncher.config import CONFIG_DIR, get_default_shortcuts
from ulauncher.utils.KeyValueJsonDb import KeyValueJsonDb
from .ShortcutResultItem import ShortcutResultItem


class ShortcutsDb(KeyValueJsonDb):

    @classmethod
    @singleton
    def get_instance(cls):
        dbPath = os.path.join(CONFIG_DIR, 'shortcuts.json')
        isFirstRun = not os.path.exists(dbPath)
        db = cls(dbPath)
        db.open()

        if isFirstRun:
            db._records = get_default_shortcuts()
            db.commit()

        return db

    def get_sorted_records(self):
        return [rec for rec in sorted(iter(self.get_records().values()), key=lambda rec: rec['added'])]

    def get_result_items(self):
        return [ShortcutResultItem(**rec) for rec in self.get_records().values()]

    def put_shortcut(self, name, keyword, cmd, icon, is_default_search, id=None):
        """
        If id is not provided it will be generated using uuid4() function
        """
        id = id or str(uuid4())
        self._records[id] = {
            "id": id,
            "name": name,
            "keyword": keyword,
            "cmd": cmd,
            "icon": icon,
            "is_default_search": bool(is_default_search),
            # use previously added time if record with the same id exists
            "added": self._records.get(id, {"added": time()})["added"]
        }
        return id
