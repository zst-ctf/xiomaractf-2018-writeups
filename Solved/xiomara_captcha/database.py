#!/usr/bin/env python3
import socket
import base64
import os
import hashlib


def getresponse(b64img):

    md5sum = hashlib.md5(b64img.encode()).hexdigest()
    if os.path.isfile("./human/" + md5sum):
        print("Human (1)")
        return '1'

    if os.path.isfile("./nonhuman/" + md5sum):
        print("Non-human (0)")
        return '0'

    display_image(b64img)

    os.system("cp ./image " + md5sum)
    return input("Human? [0/1]: ").strip()

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

    count = 0
    while True:
        try:
            data = s.recv(64).decode().strip()
        except ConnectionResetError:
            print(cumulated_data)

        cumulated_data += data.replace('\n', '')

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
            count += 1
            print(f">> Parsing Image {count} <<")

            response = getresponse(cumulated_data)

            if len(response) > 0:
                s.send(response.encode() + b'\n')
            # print(cumulated_data)
            cumulated_data = ''

        if 'Sorry' in cumulated_data:
            print(cumulated_data)
            break

        if count == 64:
            print(cumulated_data)
            print(f">> Done <<")
            while True:
                s.send(b'\n\n')
                data = s.recv(1).decode().strip()
                print(data, end='')
        


if __name__ == '__main__':
    while True:
        main()

        if input("Continue [Y/N]").strip().lower() == 'n':
            break
