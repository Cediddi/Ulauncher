from ulauncher.api.event import EventListener, SettingsUpdateEvent
from ulauncher.api.Config import Config


class Extension(object):

    def __init__(self):
        self.listeners = []

    def on_connect(self, config):
        self.subscribe(SettingsUpdateEvent, SettingsUpdateListener(config))

    def subscribe(self, event_class, listener):
        self.listeners.append((event_class, listener))


class SettingsUpdateListener(EventListener):

    def __init__(self, config):
        self.config = config

    def on_event(self, event):
        key, old_value, new_value = event.get_update()
        self.config.settings[key] = new_value


def run(extension):
    manifest = read_manifest()
    config = Config(manifest)
    extension.on_connect(config)
