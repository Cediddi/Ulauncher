

class ExtensionRequestHandler(object):

    request_queue = None

    def __init__(self):
        self.request_queue = PriorityQueue()
