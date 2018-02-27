# Flag Checker V2.0
Web - 150 points

## Challenge 
> We made a portal to check your flag. Make sure you got the right flag!

> http://103.5.112.91

## Solution

In `main.js`, it looks like base64 obfuscation.

If we search for `alert`, we see this...

	if(_0x52b070==_0x5125('0x11',']!tO')){alert('You\x20got\x20the\x20right\x20flag');}

Let's add a `console.log(_0x52b070); console.log(_0x5125('0x11',']!tO'));` just in front of it...

> See [solve.js](solve.js)

Run it and enter anything in the textbox... Now in the console window we see the flag!

	xiomara{0bfu5c@ti0n_@r3_@lw@y5_h@rd}

## Flag
`xiomara{0bfu5c@ti0n_@r3_@lw@y5_h@rd}`