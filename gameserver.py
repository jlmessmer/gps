import socketserver

graph = None

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
            result = 0
            while True:
                pmove, omove = self.makemove(result)
                print(str(pmove) + " : " + str(omove))
                result = self.resolve(pmove, omove)

    def makemove(self, startplayer = 0):
        input("Press any key to continue")
        if startplayer == 0:
            self.move = input("Please make your move: ")
            self.request.sendall(bytes("Simultaneous Move", "utf-8"))
            self.request.sendall(bytes("MOVE", "utf-8"))
            omove = str(self.request.recv(1024).strip(), "utf-8").split(',')
            omove = int(omove[1])
            self.move = int(self.move)
            print(omove)
            #self.resolve(self.move, omove)
        elif startplayer == 1:
            self.move = input("Please make your move: ")
            self.request.sendall(bytes("Your opponent played " + self.move, "utf-8"))
            self.request.sendall(bytes("MOVE", "utf-8"))
            omove = str(self.request.recv(1024).strip(), "utf-8").split(',')
            omove = int(omove[1])
            self.move = int(self.move)
            print(omove)
            #self.resolve(self.move, omove)
        else:
            self.request.sendall(bytes("It's your turn to go first", "utf-8"))
            self.request.sendall(bytes("MOVE", "utf-8"))
            omove = str(self.request.recv(1024).strip(), "utf-8").split(',')
            omove = int(omove[1])
            print("Your opponent played " + str(omove))
            self.move = input("Please make your move: ")
            self.move = int(self.move)
            #self.resolve(self.move, omove)
        return (self.move, omove)
    def resolve(self, m1, m2):
        global graph
        graph.print()
        result = graph.resolve(m1, m2)
        if result == 0:
            print("Tie: %d ties %d" % (m1, m2))
            self.request.sendall(bytes("%d ties %d" % (m2, m1), "utf-8"))
        elif result == 1:
            print("Win: %d beats %d" % (m1, m2))
            self.request.sendall(bytes("Loss: %d loses to %d" % (m2, m1), "utf-8"))
        else:
            print("Loss: %d loses to %d" % (m1, m2))
            self.request.sendall(bytes("Win: %d beats %d" % (m2, m1), "utf-8"))
        return result
        
def start(host, port, gr):
    print("Hosting game")
    global graph
    graph = gr
    server = socketserver.TCPServer((host, int(port)), GameHandler)
    # Need to change this eventually
    server.serve_forever()
