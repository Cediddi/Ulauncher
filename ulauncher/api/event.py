
class EventListener(object):

    def on_event(self, event):
        pass


class BaseEvent(object):
    pass


class KeywordQueryEvent(BaseEvent):

    def __init__(self, query):
        self.query = query

    def get_keyword(self):
        return self.query.get_keyword()

    def get_argument(self):
        """
        Returns None if arguments were not specified
        """
        return self.query.get_argument()


class PreferencesUpdateEvent(BaseEvent):

    def __init__(self, key, old_value, new_value):
        self.key = key
        self.old_value = old_value
        self.new_value = new_value

    def get_key(self):
        return self.key

    def get_old_value(self):
        return self.old_value

    def get_new_value(self):
        return self.new_value


class PreferencesEvent(BaseEvent):

    def __init__(self, preferences):
        self.preferences = preferences

    def get_preferences(self):
        return self.preferences
