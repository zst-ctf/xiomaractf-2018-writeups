#!/usr/bin/env python3
import socket
import string
import base64
import os
import hashlib
from time import sleep

def parse(b64img):
    if 'if there is no human!' in b64img:
        b64img = b64img.split('if there is no human!')[1]

    b64img = b64img.replace('\n', '').strip()

    with open('image', 'wb') as file:
        file.write(base64.decodebytes(b64img.encode()))

    returnvalue = os.system("imgcat ./image --width=80")

    if (returnvalue == 0):
        os.system("open ./image")
        os.system("open -a Terminal")
        return input("Response: ").strip()
    else:
        return ''

def savehash(b64img, response):
    md5sum = hashlib.md5(b64img.encode()).hexdigest()
    with open("./output/" + md5sum, 'w') as file:
        file.write(response)

def readhash(b64img):
    md5sum = hashlib.md5(b64img.encode()).hexdigest()
    if os.path.isfile("./output/" + md5sum):
        with open("./output/" + md5sum, 'r') as file:
            return file.read().strip()
    return None

def fuzz():
    s = socket.socket()
    s.connect(('103.5.112.91', 1340))

    base64img = ''
    while True:
        data = s.recv(1024).decode().strip()
        if not data:
            break

        base64img += data

        try:
            if readhash(base64img) is not None:
                print('Done before')
                sleep(1)
                break

            response = parse(base64img)
            if len(response) > 0:
                s.send(response.encode() + b'\n')
                savehash(base64img, response)
                base64img = ''
                break
        except:
            pass

def perform_fuzz():
    while True:
        os.system("clear")
        fuzz()

def main():
    s = socket.socket()
    s.connect(('103.5.112.91', 1340))

    base64img = ''
    prev_data = 'x'
    while True:
        data = s.recv(4).decode().strip()

        if len(prev_data) == 0:
            base64img = base64img.strip()
            # fully downloaded data
            donebefore = readhash(base64img)
            if donebefore is not None:
                print("Done before:", donebefore)
                s.send(donebefore.encode() + b'\n')
                base64img = ''
            else:
                print("Received:", data)

                try:
                    response = parse(base64img)

                    if len(response) > 0:
                        s.send(response.encode() + b'\n')
                        savehash(base64img, response)
                        base64img = ''
                except:
                    pass
        else:
            print("Received:", data)
            base64img += data
            prev_data = data.strip()

        

if __name__ == '__main__':
    #perform_fuzz()
    main()
