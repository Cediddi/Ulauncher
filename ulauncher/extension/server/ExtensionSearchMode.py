from ulauncher.ext.SearchMode import SearchMode
from ulauncher.ext.actions.ActionList import ActionList
from ulauncher.ext.actions.RenderResultListAction import RenderResultListAction
from ulauncher.extension.server.ExtensionRunner import ExtensionRunner


class ExtensionSearchMode(SearchMode):

    def __init__(self):
        self.extensionRunner = ExtensionRunner.get_instance()

    def is_enabled(self, query):
        """
        Return True if mode should be enabled for a query
        """
        return self.extensionRunner.get_extension_controller(query.get_keyword())

    def on_query_change(self, query):
        """
        Triggered when user changes a search query
        """
        self.extensionRunner.on_query_change(query)

    def on_key_press_event(self, widget, event, query):
        """
        @param widget Gdk.Widget
        @param event Gdk.EventKey
        @param query Query
        @return iterable with ActionList objects
        """

    def on_query(self, query):
        """
        @return ActionList object
        """
        controller = self.extensionRunner.get_extension_controller(query.get_keyword())

        if not controller:
            # TODO: this line shouldn't be entered
            return ActionList([])

        result_list = controller.on_query(query)
        return ActionList([RenderResultListAction(result_list)])
