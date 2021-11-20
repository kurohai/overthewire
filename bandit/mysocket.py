#!/usr/bin/env python


from pprint import pprint as pp
import socket
import os
import pdb
import nmap
import bs4


target_host = "www.google.com"
target_port = 80  # create a socket object
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
bytes_to_rec = 4096 * 4


class MySocket:
    """demonstration class only
    - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


def main():
    s = MySocket()
    s.connect(target_host, target_port)
    s.mysend(msg=request)
    r = s.myreceive()
    pp(r)
    return r


if __name__ == '__main__':
    main()
