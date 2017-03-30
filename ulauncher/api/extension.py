import os
import sys
from json import load
from ulauncher.api.event import EventListener, PreferencesUpdateEvent
from ulauncher.api.preferences import Config
from ulauncher.extension.communication.Client import Client


class Extension(object):

    _manifest = None
    preferences = None

    def __init__(self):
        self.listeners = []

    def on_connect(self):
        self.subscribe(PreferencesUpdateEvent, PreferencesUpdateListener(self))
        self.subscribe(PreferencesEvent, PreferencesListener(self))

    def subscribe(self, event_class, listener):
        self.listeners.append((event_class, listener))

    def _get_listeners_of_type(self, cls):
        return [l for event_cls, l in self.listener if event_cls is cls]

    def trigger_event(self, event):
        result = None
        for listener in self._get_listeners_of_type(type(event)):
            result = listener.on_event(event)

        return result

    def get_manifest(self):
        if not self._manifest:
            with(os.path.dirname(sys.argv[0]), 'r') as f:
                self._manifest = load(f)

        return self._manifest


class PreferencesUpdateListener(EventListener):

    def __init__(self, extension):
        self.extension = extension

    def on_event(self, event):
        self.extension.preferences[event.key] = event.new_value


class PreferencesListener(EventListener):

    def __init__(self, extension):
        self.extension = extension

    def on_event(self, event):
        self.extension.preferences = event.preferences


def run(extension):
    Client(extension).connect()
