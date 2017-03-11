

class Config(object):

    manifest = None
    settings = None

    def __init__(self, manifest):
        self.manifest = manifest
        self.settings = get_settings()
