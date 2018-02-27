# For-1
Practice - 0 points

## Challenge 
> Someone has crashed our server , but luckily we have captured all traffic , help us in finding the culprit

> [forensics_50c170cdb118f47d764cc07998490262_100.pcap](forensics_50c170cdb118f47d764cc07998490262_100.pcap)

## Solution

Open in wireshark.

After a quick glance, we see that a user of ip `192.168.192.136` is entering some username / password on a website.

Hence, apply the filter:

	ip.src == 192.168.192.136 && tcp

Now we realise that there's a lot of zero length packets.

Add the filter:

	ip.src == 192.168.192.136 && tcp && data.len != 0

Finally, we have found a packet of length `509`. Extract it 

	$ cat data.txt | xxd -r -p
	from pwn import *

	shellcode = "\xeb\x1e\xb8\x04\x00\x00\x00\xbb\x01\x00\x00\x00\x59\xba\x21\x00\x00\x00\xcd\x80\xb8\x01\x00\x00\x00\xbb\x00\x00\x00\x00\xcd\x80\xe8\xdd\xff\xff\xff\x78\x69\x6f\x6d\x61\x72\x61\x7b\x53\x68\x65\x6c\x6c\x63\x6f\x64\x65\x5f\x69\x73\x5f\x61\x6c\x77\x61\x79\x73\x5f\x66\x75\x6e\x21\x7d\x0d\x0a"

	p = gdb.debug('./easyshell')

	print p.recvline()

	p.sendline(shellcode)

	flag =  p.recvline()
	print flag 

There's something fishy about the shellcode. Print it.

	$ python3
	>>> shellcode = "\xeb\x1e\xb8\x04\x00\x00\x00\xbb\x01\x00\x00\x00\x59\xba\x21\x00\x00\x00\xcd\x80\xb8\x01\x00\x00\x00\xbb\x00\x00\x00\x00\xcd\x80\xe8\xdd\xff\xff\xff\x78\x69\x6f\x6d\x61\x72\x61\x7b\x53\x68\x65\x6c\x6c\x63\x6f\x64\x65\x5f\x69\x73\x5f\x61\x6c\x77\x61\x79\x73\x5f\x66\x75\x6e\x21\x7d\x0d\x0a"
	
	>>> print(shellcode)
	ë¸»Yº!Í¸»ÍèÝÿÿÿxiomara{Shellcode_is_always_fun!}

## Flag
`xiomara{Shellcode_is_always_fun!}`