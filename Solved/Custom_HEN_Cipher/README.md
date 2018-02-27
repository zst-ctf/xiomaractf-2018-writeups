# Custom HEN Cipher
Crypto - 50 points

## Challenge 
> Ragnar &Lagertha are two secret agents of Valhalla wants to share a secret message but could not place the trust on basic ciphers so they decided to come up with their own cipher.

>We have managed to get the ciphertext :082_336_88_167755403.
So help us and we will reward you with 50 points
Flag is not wrapped in xiomara{}

> [finalhen.txt](finalhen.txt)

## Solution

#### Solve alphametic puzzle

	the stardard alphametic puzzle used is {ZCUKZ+NPYFG=GFUKPH}

Use this website: http://www.tkcs-collins.com/cgi/alpha_solve.cgi

And we get the solution

	C=0 F=2 G=1 H=9 K=3 N=4 P=5 U=6 Y=7 Z=8 

Now convert the cipher text into the encrypted hen:

	082_336_88_167755403 
	... becomes ...
	CZF_KKU_ZZ_GUYYPPNCK

#### Decrypt hen


	$ python3
	
	>>> import hen_cipher
	
	>>> hen_cipher.hen_decrypt('CZF_KKU_ZZ_GUYYPPNCK')
	'THE_ARS_OF_DIDUCTION'

## Flag
`xiomara{THE_ARS_OF_DIDUCTION}`
