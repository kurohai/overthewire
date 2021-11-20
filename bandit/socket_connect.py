#!/usr/bin/env python


from pprint import pprint as pp
import socket
import os
import pdb
import nmap
import bs4
import codecs


target_host = "www.google.com"
target_port = 80  # create a socket object
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
bytes_to_rec = 4096 * 4


def client_connect(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(10)
    # connect the client
    client.connect((host, port))
    return client


def send_data(client, data):
    # send some data
    client.send(request.encode())
    return client


def receive_data(client, bytes_to_rec):
    # receive some data
    # response = client.recv(int(bytes_to_rec))
    rbytes = 4096
    r = bytes()
    cont_resp = True
    try:
        while cont_resp:
            resp = client.recv(int(rbytes))
            # pp(resp)
            # pp(codecs.decode(resp, 'utf8'))
            # pp(resp.decode('utf8'))
            # pp(len(resp))
            # print(type(str(resp)))

            if resp:
                r += resp
            else:
                cont_resp = False
    except Exception as err:
        pp(err)
        pass
    return client, r


def write_file(data, filepath):
    with open(filepath, 'w') as f:
        f.write(data)


def main():
    client = client_connect(target_host, target_port)
    client = send_data(client, request)
    client, response = receive_data(client, bytes_to_rec)
    # data = format_response(response)
    filepath = './datafile'
    write_file(response, filepath)
    print(data)
    print('data written to: {0}'.format(filepath))


if __name__ == '__main__':
    main()
