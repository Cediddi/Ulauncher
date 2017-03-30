import os
import sys
import pickle
import websocket
from ulauncher.extension.communication.request import InitExtensionRequest
from ulauncher.utils.run_async import run_async


class Client(object):

    def __init__(self, extension, ws_port=os.environ['ULAUNCHER_WS_PORT']):
        self.ws_port = ws_port
        self.extension = extension

    def connect(self):
        websocket.enableTrace(True)
        websocket.WebSocketApp("ws://localhost:%s/" % self.ws_port,
                               on_message=run_async(self.on_message),
                               on_error=run_async(self.on_error),
                               on_open=run_async(self.on_open),
                               on_close=run_async(self.on_close))

    def on_message(self, ws, message):
        event = pickle.loads(message)
        self.extension.trigger_event(event)

    def on_error(self, ws, error):
        print error

    def on_close(self, ws):
        print("Connection closed")
        sys.exit(1)

    def on_open(self, ws):
        manifest = self.extension.get_manifest()
        ws.send(pickle.dumps(InitExtensionRequest(manifest)))
