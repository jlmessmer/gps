import rgraph
import os
import sys
import random

class Game:
    # Choose a size for the rps game
    def __init__(self, size):
        self.size = size
        
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
        self.menu()
    def menu(self):
        print("Main Menu")
        print("[1] New Game")
        print("[2] About This")
        print("[3] Quit Game")
        sel = input("Please enter a selection ")
        sel = int(sel)
        if sel == 1:
            self.newgame()
        elif sel == 2:
            self.about()
        elif sel == 3:
            sys.exit()

    def gameloop(self):
        print("This game of Graph-Paper-Scissors has %d possible moves (moves 0 - %d)" % (self.size, self.size - 1))
        pmove = input("Please make your move, or enter Q to quit ")
        while pmove.upper() != "Q":
            pmove = int(pmove)
            if pmove < 0 or pmove >= self.size:
                print("Invalid move")
                continue
            cmove = random.randint(0, self.size - 1)
            print(str(cmove))
            result = self.graph.resolve(pmove, cmove)
            if result == 0:
                print("Tie: %d ties %d" % (pmove, cmove))
            elif result == 1:
                print("Win: %d beats %d" % (pmove, cmove))
            else:
                print("Loss: %d loses to %d" % (cmove, pmove))
            self.clear()
            pmove = input("Please make your move, or enter Q to quit ")
    
    def newgame(self):
        self.clear()
        print("New Game")
        self.gameloop()
    def about(self):
        self.clear()
        print("About")
    def start(self):
        self.setup()

def main():
    game = Game(5)
    game.start()

if __name__ == "__main__" : main()
