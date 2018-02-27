#!/usr/bin/env python3
import socket
import base64
import os

'''
# edit `./facedetect`
# /usr/local/lib/python3.6/site-packages/cv2/data
    DATA_DIR = '/usr/local/lib/python3.6/site-packages/cv2/data/'
    CASCADES = {}

    PROFILES = {
        'HAAR_FRONTALFACE_ALT2': 'haarcascade_frontalface_alt2.xml',
    }
'''


def getresponse(b64img):
    output = os.popen('./facedetect/facedetect ./image').read()

    display_image(b64img)
    if len(output.splitlines()) > 1:
        # face detected
        print("Human")
        return '1'
    else:
        print("Non-human")
        return '0'


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
            print(cumulated_data)
            break


if __name__ == '__main__':
    while True:
        main()

        if input("Continue [Y/N]").strip().lower() == 'n':
            break
