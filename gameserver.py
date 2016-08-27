import socketserver

class GameHandler(socketserver.BaseRequestHandler):
    name = ""
    move = ""
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
            self.move(0)
    def move(self, startplayer):
        if startplayer == 0:
            self.move = input("Please make your move: ")
            self.request.sendall(bytes("Please make your move: ", "utf-8"))
            omove = self.request.recv(1024).strip()

        
def start(host, port):
    print("Hosting game")
    server = socketserver.TCPServer((host, int(port)), GameHandler)
    # Need to change this eventually
    server.serve_forever()
