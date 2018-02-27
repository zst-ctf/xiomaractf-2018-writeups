# Bin
Practice - 0 points

## Challenge 
> Try to Decipher this

> [cipher.txt](cipher.txt)

## Solution
	
	$ cat cipher.txt | tr -d ' ' | perl -lpe '$_=pack"B*",$_'
	xiomara{youfoundme}

## Flag
`xiomara{youfoundme}`