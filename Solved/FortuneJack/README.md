# FortuneJack
Reverse Engineering - 50 points

## Challenge 
> If your smartphone gets connected to a VPN, you feel like you won a lucky draw.

> [Lucky_Drawer.exe](Lucky_Drawer.exe)

## Solution

Decompile with Jetbrains dotPeek

From decompiled source:

- It generates a number between 0-1500, and
- decrypts a string using the number as a key.
- If the number is correct (matching a certain MD5), it shows the flag

Hence we can bruteforce 0-1500. 

> solve.cs

	Flag is:
	xiomara{wow_great_you_did_it_:)}
	Press any key to continue . . .

## Flag
`xiomara{wow_great_you_did_it_:)}`