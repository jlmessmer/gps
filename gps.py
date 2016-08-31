import rgraph
import computer
import os
import sys
import socket
import random
import server
import gameserver

class Game:
    # Choose a size for the rps game
    def __init__(self, size):
        self.size = size
        self.computer = computer.Computer("CPU")
        self.graph = rgraph.Rgraph()
        self.graph.gennodes(self.size)
        self.graph.genedges()
        self.graph.print()
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def setup(self):
        self.clear()
        print("Welcome to Graph-Paper-Scissors")
        print("Press any key to continue")
        input()
        self.clear()
        self.mainmenu()
    def mainmenu(self):
        print("Main Menu")
        print("[1] New Game")
        print("[2] About This")
        print("[3] Quit Game")
        print("[4] See Graph")
        sel = input("Please enter a selection ")
        sel = int(sel)
        if sel == 1:
            self.newgame()
        elif sel == 2:
            self.about()
        elif sel == 3:
            sys.exit()
        elif sel == 4:
            self.graph.print()
            self.mainmenu()

    def gameloop(self):
        print("This game of Graph-Paper-Scissors has %d possible moves (moves 0 - %d)" % (self.size, self.size - 1))
        winner = 0
        while True:
            if winner == 0:
                pmove = input("Please make your move, or enter Q to quit ")
                pmove = int(pmove)
                if pmove < 0 or pmove >= self.size:
                    print("Invalid move")
                    continue
                cmove = random.randint(0, self.size - 1)
                result = self.graph.resolve(pmove, cmove)                
            elif winner == 1:
                self.clear()
                pmove = input("Please make your move ")
                pmove = int(pmove)
                if pmove < 0 or pmove >= self.size:
                    print("Invalid move")
                    continue
                cmove = random.randint(0, self.size - 1)
                result = self.graph.resolve(pmove, cmove)
            else:
                self.clear()
                cmove = random.randint(0, self.size - 1)
                print("CPU Move: %d" % cmove)
                pmove = input("Please make your move ")
                pmove = int(pmove)
                if pmove < 0 or pmove >= self.size:
                    print("Invalid move")
                    continue

                result = self.graph.resolve(pmove, cmove)


            if result == 0:                
                print("Tie: %d ties %d" % (pmove, cmove))
                winner = 0
            elif result == 1:
                print("Win: %d beats %d" % (pmove, cmove))
                winner = 1
            else:
                print("Loss: %d loses to %d" % (pmove, cmove))
                winner = 2
            pmove = input("Press any key to continue or Q to quit")
            if pmove.upper() == "Q":
                break

        self.clear()
        self.mainmenu()

    def about(self):
        self.clear()
        abt = open('about.txt', 'r')
        for line in abt:
            print(line)
        input("Press any key to continue")
        self.clear()
        self.mainmenu()
    def newgame(self):
        self.clear()
        print("Game Creation")
        print("[1] Local Game vs CPU")
        print("[2] Online Multiplayer")
        sel = input("Please enter a selection, or press any key to return ")
        sel = int(sel)
        if sel == 1:
            self.gameloop()
        elif sel == 2:
            self.clear()
            print("[1] Find Game")
            print("[2] Host Game")
            sel = input("Please enter a selection, or press Q to return")
            if sel.upper() == "Q":
                self.mainmenu()
            else:
                if int(sel) == 1:                    
                    self.getgames()
                else:
                    self.hostgame()
        else:
            self.mainmenu()


    def hostgame(self):
        name = input("Game name: ")
        ip = input("Your IP address (google \"What is my ip\" if you don't know): ")
        port = input("Port number: ")
        HOST, PORT = '98.26.17.47', 8000
        data = " ".join(sys.argv[1:])

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((HOST, PORT))
            sock.sendall(bytes("START,"+ name +"," + ip + "," + port, "utf-8"))

            received = str(sock.recv(1024), "utf-8")
        finally:
            sock.close()
        self.startserver(ip, port)

    def startserver(self, host, port):
        gameserver.start(host, port, self.graph)

    
    def getgames(self):
        HOST, PORT = '98.26.17.47', 8000
        data = " ".join(sys.argv[1:])        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        sock.connect((HOST, PORT))
        sock.send(bytes("GET,Name,127.0.0.0,9999", "utf-8"))
        received = str(sock.recv(1024), "utf-8")
        sock.close()
        opengames = received.split(',')
        self.clear()
        for i in range(0, len(opengames)):
            print("[%d] %s" % (i+1, opengames[i]))
        sel = input("Select a game you would like to play or press Q to return ")
        if sel.upper() == 'Q' or int(sel) < 1 or int(sel) > len(opengames):
            return
        req = "REQUEST," + str(int(sel) - 1)
        print(req)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))        
        sock.send(bytes(req, "utf-8"))
        received = str(sock.recv(1024), "utf-8").split(',')
        print(received)
        sock.close()
        self.connect(received[1], received[2])
    def connect(self, ip, port):
        name = input("What is your username? ")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, int(port)))
        sock.send(bytes("INIT," + name, "utf-8"))        
        while True:
            recv = str(sock.recv(1024), "utf-8")
            print(recv)
            recv = str(sock.recv(1024), "utf-8")
            if recv == "MOVE":
                move = input("Please make your move: ")
                sock.send(bytes("MOVE," + move, "utf-8"))
            recv = str(sock.recv(1024), "utf-8")
            print(recv)
    def start(self):
        self.setup()

def main():
    game = Game(5)
    game.start()

if __name__ == "__main__" : main()
