# https://www.youtube.com/watch?v=4uHTSknGJaY

import socket
import warnings

HOST, PORT = "127.0.0.1", 25001


class ClientServer:
    def __init__(self):
        self.data = "1.0|1.0"

        try:
            # connect to the socket
            # SOCK_STREAM means TCP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))
        except:
            self.__raiseExcNotConnected()

    def __del__(self):
        self.sock.close()

    def isConnected(self) -> bool:
        try:
            # Try to get the peer name, this will raise an exception if not connected
            self.sock.getpeername()
            return True
        except socket.error:
            self.__raiseExcNotConnected()
            return False

    def __raiseExcNotConnected(self):
        warnings.warn("The client is not connected")

    def sendData(self, _data):
        self.data = _data
                #if self.isConnected() is not True:
        #    return
        self.sock.sendall(self.data.encode("utf-8"))

        response = self.sock.recv(1024).decode("utf-8")
        print(response)


if __name__ == "__main__":
    client = ClientServer()
    client.data = "1,2"
    print("a")
    client.sendData()
