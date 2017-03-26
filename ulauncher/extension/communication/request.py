class BaseRequest(object):
    pass


class InitExtensionRequest(object):

    def __init__(self, manifest):
        self.manifest = manifest
