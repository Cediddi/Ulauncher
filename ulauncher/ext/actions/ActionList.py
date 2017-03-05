class ActionList(list):

    def keep_app_open(self):
        """
        Retruns True if ulauncher window should remain open once all actions are done
        """
        # return true if there no actions in the list
        if not self:
            return True
        else:
            return any([i.keep_app_open() for i in self])

    def run_all(self):
        list(map(lambda i: i.run(), self))
