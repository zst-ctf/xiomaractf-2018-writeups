#!/usr/bin/env python3
import socket
import base64
import hashlib


def download(b64img):
    md5sum = hashlib.md5(b64img.encode()).hexdigest()
    with open('./download/' + md5sum, 'wb') as file:
        file.write(base64.decodebytes(b64img.encode()))


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

    print('>> Download <<')

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
            download(cumulated_data)
            break

if __name__ == '__main__':
    while True:
        main()
