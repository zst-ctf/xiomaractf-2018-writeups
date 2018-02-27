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
cache = dict()


def getresponse(b64img):
    md5sum = hashlib.md5(b64img.encode()).hexdigest()
    if md5sum in cache:
        response = cache[md5sum]
        print("Cached value:", response)
    else:
        display_image(b64img)
        response = input("Human? [0/1]: ").strip()
        cache[md5sum] = response
    return response


def display_image(b64img):
    with open('image', 'wb') as file:
        file.write(base64.decodebytes(b64img.encode()))
    os.system("open ./image")
    os.system("open -a Terminal")    


def main():
    s = socket.socket()
    s.connect(('103.5.112.91', 1340))

    cumulated_data = ''

    while True:
        data = s.recv(1).decode().strip()
        # remove initial message
        cumulated_data += data
        if cumulated_data.endswith('human!'):
            cumulated_data = ''
            break

    print('>> START <<')

    while True:
        try:
            data = s.recv(1).decode().strip()
        except ConnectionResetError:
            print(cumulated_data)

        cumulated_data += data

        try:
            decoded = base64.decodebytes(cumulated_data.encode())
        except:
            decoded = b''

        # https://stackoverflow.com/a/4585611
        # bytes 0xFF, 0xD8 indicate start of image
        # bytes 0xFF, 0xD9 indicate end of image
        end_of_image = decoded.endswith(b'\xFF\xD9')

        # Complete image has been downloaded, parse it
        if end_of_image:
            print(">> Parsing Image <<")

            response = getresponse(cumulated_data)

            if len(response) > 0:
                s.send(response.encode() + b'\n')
            cumulated_data = ''

        if 'Sorry' in cumulated_data:
            break
        '''
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
        '''


if __name__ == '__main__':
    while True:
        main()

        if input("Continue [Y/N]").strip().lower() == 'n':
            break
