from functools import partial
from queue import PriorityQueue
from ulauncher.utils.run_async import run_async
from ulauncher.utils.SimpleWebSocketServer import SimpleWebSocketServer
from .ExtensionController import ExtensionController
from .ExtensionRequestHandler import ExtensionRequestHandler


class Server(object):

    def __init__(self, ws_port):
        self.controllers = []
        self.requestHandler = ExtensionRequestHandler()

    def get_port(self):
        return 8001

    @run_async
    def start(self):
        self.ws_server = SimpleWebSocketServer('',
                                               self.get_port(),
                                               partial(ExtensionController, self.controllers, self.requestHandler))
        self.serveforever()

    def stop(self):
        pass

    def send_event(self, extension_id, event):
        pass
