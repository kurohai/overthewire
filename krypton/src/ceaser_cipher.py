#!/usr/bin/env python


from pprint import pprint as pp
import sys
from logutil import get_logger

log = get_logger(__name__)


def encrypt(text, s):
    result = str()
    for i in range(len(text)):
        char = text[i]
        print("working on char: {0}".format(char))
        if char == " ":
            result += str(char)
        elif char in [str(n) for n in range(0, 12)]:
            result += str(char)
        elif char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
            print("current result: {0}".format(result))
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
            print("current result: {0}".format(result))
    return result


def normal_cesear(text, s):
    result = str()
    for i in range(len(text)):
        char = text[i]
        # print("working on char: {0}".format(char))
        if char == " ":
            result += str(char)
        else:
            result += chr((ord(char) + s - 65) % 26 + 65)
    return result


def main(args):
    if args:
        pp(args)

    # check the above function
    # text = "CEASER CIPHER DEMO"
    # text = "YRIRY GJB CNFFJBEQ EBGGRA"
    # text = "MNOPQRSTUVWXYZABCQEFGHIJKL"
    text = "KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS"
    s = 13
    n = 14

    # print("Plain Text : " + text)
    # print("Shift pattern : " + str(s))
    print("Cipher: " + encrypt(text, 13))

    # pp(encrypt("Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh", 13))
    # for n in range(128):
    log.debug("{0}\t {1}".format(n, normal_cesear(text, n)))


if __name__ == "__main__":
    args = [sys.argv]
    main(args)
