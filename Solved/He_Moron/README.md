# He Moron
Crypto - 200 points

## Challenge 
> An overconfident boastful moron has claimed that he has written his own version of a MAC and has challenged the people here at Xiomara to break it! We are very certain that he might have made a mistake in the implementation. So, help us find one, crack his scheme and get the flag!

>Challenge is running at 103.5.112.91 8912

>Here's the source of his python implementation...

> [source.py](source.py)

## Solution

nc to the challenge and submit a test 

	$ nc 103.5.112.91 8912

	You wanna challenge me? You trying to break my signing scheme? LOLLLLLL ><
	Anyways, try hard for that boy!
	Press 0 to get your message signed and 1 to submit a forgery...Pffff! Seriously?
	0


	Gimme your hex encoded message

	61616161616161616161616161616161

	There you go! Here's my hex encoded tag!
	da030c17f299c08f5f63527b29ed520f


From the source we see this

	strxor(mb[i], t)

This means `output = enc( enc(block0) XOR block1 )`

Hence, we just need to append the ciphertext of the previous block.

#### Execute now

	xiomaractf-2018 $ nc 103.5.112.91 8912

	You wanna challenge me? You trying to break my signing scheme? LOLLLLLL ><
	Anyways, try hard for that boy!
	Press 0 to get your message signed and 1 to submit a forgery...Pffff! Seriously?
	0


	Gimme your hex encoded message

	61616161616161616161616161616161

	There you go! Here's my hex encoded tag!
	da030c17f299c08f5f63527b29ed520f
	0


	Gimme your hex encoded message

	61616161616161616161616161616161da030c17f299c08f5f63527b29ed520f

	There you go! Here's my hex encoded tag!
	76d1cb4bafa246e2e3af035d6c13c372
	0


	Gimme your hex encoded message

	61616161616161616161616161616161da030c17f299c08f5f63527b29ed520f76d1cb4bafa246e2e3af035d6c13c372

	There you go! Here's my hex encoded tag!
	76d1cb4bafa246e2e3af035d6c13c372

Success!

Now we got the 2 texts, submit them both.

	Oh! So, you are up for it?

	Alright! Gimme just two different hex encoded messages that could sign to the same tag!

	Message #1: 

	61616161616161616161616161616161da030c17f299c08f5f63527b29ed520f

	Message #2: 

	61616161616161616161616161616161da030c17f299c08f5f63527b29ed520f76d1cb4bafa246e2e3af035d6c13c372

	What? Nooooooooo!!! xiomara{1_b0w_d0wn_70_y0u!}

## Flag
`xiomara{1_b0w_d0wn_70_y0u!}`