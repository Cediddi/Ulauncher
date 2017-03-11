
class EventListener(object):

    def on_event(self, event):
        pass


class BaseEvent(object):
    pass


class KeywordQueryEvent(BaseEvent):

    def get_query(self):
        pass
