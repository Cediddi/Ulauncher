from .BaseAction import BaseAction


class RenderResultListAction(BaseAction):

    def __init__(self, result_list):
        """
        :param list result_list: list of ResultItem objects
        """
        self.result_list = result_list

    def keep_app_open(self):
        return True

    def run(self):
        from ulauncher.ui.windows.UlauncherWindow import UlauncherWindow
        UlauncherWindow.get_instance().show_results(self.result_list)
