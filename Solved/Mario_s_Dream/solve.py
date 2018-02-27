#!/usr/bin/env python3
import socket

# Given x , we need to find the numbers less than x such that (p xor x) > x where 1<=p<x

'''
def count_p(x):
    bits = len(bin(x)[2:].lstrip('1'))
    starting = (1 << bits)
    p = starting
    count = 0
    while 1 <= p:
        p -= 1
        if p ^ x > x:
            count += 1
    return count
'''

'''
def count_optimised(x):
    weight = 1
    count = 0
    while x > 0:
        if (x & 1) == 0:
            # if last bit is zero,
            # then xor last bit will be larger
            count += weight

        x >>= 1 # move on to next LSB
        weight <<= 1 # the next LSB has a higher weightage
    return count
'''

def count_static(x):
    return (1 << x.bit_length()) - 1 - x

def main():
    s = socket.socket()
    s.connect(('139.59.28.4', 1352))

    success = 0

    # do first one here so don't add up overhead of splitlines
    data = s.recv(512).decode().strip()
    number = int(data.splitlines()[-1])
    counts = count_static(number)
    s.send(str(counts).encode() + b'\n')

    while True:
        data = s.recv(2048).decode().strip()
        # print('\rReceived:', data, success, end='')

        number = int(data)
        counts = count_static(number)

        s.send(str(counts).encode() + b'\n')
        success += 1


if __name__ == '__main__':
    main()
