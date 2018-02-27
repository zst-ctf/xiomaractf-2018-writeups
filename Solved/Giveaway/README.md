# Giveaway
Cryptography - 150 points

## Challenge 
> Hey! We at Xiomara would love to giveaway the flag to you. But, we can't now, because someone just stole it from us and tried sending it to our rival, Jack. Our super strong web guy here came to the rescue and intercepted it on the way, but found that it was RSA encrypted! You are our crypto guy now. So, decrypt the message and as we promised, the flag is yours!

> [Jacks_public_key](Jacks_public_key)

> [Ciphertext](Ciphertext)

## Solution

`e` is very small, `n` is very large.

[If there's no padding we can try to crack it](https://crypto.stackexchange.com/questions/6770/cracking-an-rsa-with-no-padding-and-very-small-e)

	If there is no padding, then you can try the following:
	...
	If e = 3 and m is short, then m^3 could be an integer which is smaller than n, in which case the modulo operation is a no-operation. In that case, you can just compute the cube root of the value you have (cube root for plain integers, not modular cube root).

Using python3 and gmpy

	$ python3
	>>> import gmpy2
	>>> c = int(open('Ciphertext').read())
	>>> e = 3
	>>> m = gmpy2.iroot(c, e)[0]
	>>> flag = bytes.fromhex('%x' % m)
	>>> print(flag.decode())
	xiomara{4y3_4y3_cryp70_6uy!}

## Flag
`xiomara{4y3_4y3_cryp70_6uy!}`
