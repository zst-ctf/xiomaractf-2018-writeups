# Rev2
Practice - 0 points

## Challenge 
> Find the key!

> [Oh_No_Find_The_Key.exe](Oh_No_Find_The_Key.exe)

## Solution

It is a .NET application

	$ file Oh_No_Find_The_Key.exe 
	Oh_No_Find_The_Key.exe: PE32 executable (GUI) Intel 80386 Mono/.Net assembly, for MS Windows

Decompile with JetBrains dotPeek

We see these relevant lines

	this.reverse(this.label2.Text + this.label3.Text + this.label4.Text + this.label5.Text);
	
	this.label2.Text = "==QfyV2aj";
	this.label3.Text = "FGSfVWTf";
	this.label4.Text = "Rmb19mRfV3b";
	this.label5.Text = "ZtXYyFWbvlGe";

And now decode it

	$ python

	>>> ("==QfyV2aj" + "FGSfVWTf" + "Rmb19mRfV3b" + "ZtXYyFWbvlGe")[::-1].decode('base64')
	'xiomara{You_Found_Me_Hacker}'

## Flag
`xiomara{You_Found_Me_Hacker}`