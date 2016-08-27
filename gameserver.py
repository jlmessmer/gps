import socketserver

class GameHandler(socketserver.BaseRequestHandler):
    name = ""
    def handle(self):
        self.data = self.request.recv(1024).strip()
        # Connection query types:
        #   1) Init
        #   2) Move
        # Structures:
        #   Init:
        #       INIT,<name>
        #   Move:
        #       MOVE,<move>
        conninfo = self.data.decode("utf-8").split(',')
        if conninfo[0] == "INIT":
            self.name = conninfo[1]
            print(self.name + " has joined the game.")
def start(host, port):
    print("Hosting game")
    server = socketserver.TCPServer((host, int(port)), GameHandler)
    # Need to change this eventually
    server.serve_forever()