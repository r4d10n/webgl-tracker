from ast import Not
from simple_websocket_server import WebSocketServer, WebSocket
import socketserver, threading, time
import queue
import json

q = queue.Queue(1024)

class SimpleEcho(WebSocket):
    def handle(self):
        while not q.empty():
            self.send_message(q.get())
    
    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')

class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        opts = {}
        data = self.request[0].strip()
        opts['received_string'] = data.decode("utf-8")
        q.put(json.dumps(opts))
#        socket = self.request[1]
#        current_thread = threading.current_thread()
#        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, data))
#        socket.sendto(data.upper(), self.client_address)

class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8888

    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    
    wsserver = WebSocketServer('', 8000, SimpleEcho)

    try:
        server_thread.start()
        wsserver.serve_forever()
        print("Server started at {} port {}".format(HOST, PORT))
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        exit()


