from ulauncher.helpers import singleton
from ulauncher.search.DefaultSearchMode import DefaultSearchMode
from ulauncher.search.file_browser.FileBrowserMode import FileBrowserMode
from ulauncher.search.calc.CalcMode import CalcMode
from ulauncher.extension.server.ExtensionSearchMode import ExtensionSearchMode


class Search(object):

    @classmethod
    @singleton
    def get_instance(cls):
        return cls(DefaultSearchMode(), [FileBrowserMode(), CalcMode(), ExtensionSearchMode()])

    def __init__(self, default_search_mode, search_modes):
        self.default_search_mode = default_search_mode
        self.search_modes = search_modes

    def on_query_change(self, query):
        """
        Iterate over all search modes and run first enabled. Fallback to DefaultSearchMode
        """
        for mode in self.search_modes:
            mode.on_query_change(query)

        self.choose_search_mode(query).on_query(query).run_all()

    def choose_search_mode(self, query):
        return next((mode for mode in self.search_modes if mode.is_enabled(query)), self.default_search_mode)

    def on_key_press_event(self, widget, event, query):
        self.choose_search_mode(query).on_key_press_event(widget, event, query)
