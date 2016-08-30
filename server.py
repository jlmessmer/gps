import socketserver
import socket

class Connection:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
    def __str__(self):
        return self.name + "\r\n\t" + self.ip + "\r\n\t" + self.port

class GPSHandler(socketserver.BaseRequestHandler):

    opengames = []
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        conninfo = self.data.decode("utf-8").split(',')
        print(conninfo[0])
        if conninfo[0] == "START":
            newconn = Connection(conninfo[1], conninfo[2], conninfo[3])
            self.opengames.append(newconn)
            self.opengames.sort(key=lambda connection: connection.name)
            print("==========")
            for conn in self.opengames:
                print(conn.name)
            print("==========")
            self.request.sendall(bytes("Received", "utf-8"))
        elif conninfo[0] == "GET":
            retstr = ""
            for conn in self.opengames:
                retstr += conn.name + ','
            self.request.sendall(bytes(retstr[:-1], "utf-8"))
        else:
            selgame = self.opengames[int(conninfo[1])]
            self.opengames.remove(selgame)
            retstr = selgame.name + "," + selgame.ip + "," + selgame.port
            print("Game to get: " + conninfo[1])
            self.request.sendall(bytes(retstr, "utf-8"))



if __name__ == "__main__":
    #print("hi")
    HOST, PORT = '', 80
    print(HOST)
    server = socketserver.TCPServer((HOST, PORT), GPSHandler)
    server.serve_forever()
