import pickle
from ulauncher.utils.SimpleWebSocketServer import WebSocket
from ulauncher.extension.objects.event import KeywordQueryEvent


class ExtensionController(object):

    def __init__(self, controllers, requestHandler):
        self.controllers = controllers
        self.requestHandler = requestHandler

    def on_query(self, query):
        event = KeywordQueryEvent(query)
        self.sendMessage(event)

    def handleMessage(self):
        """
        Inbound request
        """
        request = pickle.loads(self.data)
        self.requestHandler.handle(request)

    def handleConnected(self):
        print(self.address, 'connected')
        self.controllers.append(self)

    def handleClose(self):
        print(self.address, 'closed')
        self.controllers.remove(self)
