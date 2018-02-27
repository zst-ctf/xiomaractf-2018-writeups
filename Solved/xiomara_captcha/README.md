# xiomara captcha
Misc - 100 points

## Challenge 
> Young mario was fascinated with computers being able to recognise human beings. Well now he wants to do the same. Help him out!!

> Challenge running :103.5.112.91 1340

## Solution

	$ nc 103.5.112.91 1340
	  Human or Not??
	We are giving you 64 base64 encodings of jpg images.
	You just need to tell me if it is a human or not.
	print 1 if there is a human and 0 if there is no human!

From this, we need a script to parse the base64 JPG encodings and display it to us, after which determine if human or not human.

I had many failed attempts such as:

- an interface where I can type `0` and `1` as fast as I can (server had timelimit)
- another using facedetect (failed because it detected an monkey/ape like a human's face...)

---

Since the images are recycled, I decided to do a database...

A database where I downloaded images beforehand (`downloads.py`) and manually sorted it into folders (`human` and `nonhuman`).

Next, I ran my script (`database.py`) which retrieved from the database and sent the correct reply.


Finally after 64 images, it was successful... 


	...
	>> Parsing Image 63 <<
	Non-human (0)
	>> Parsing Image 64 <<
	Human (1)

	>> Done <<
	^CCongratsflagis:xiomara{you_just_processed_an_image}Traceback (most recent call last):
	  File "database.py", line 94, in <module>
	    main()
	  File "database.py", line 86, in main
	    s.send(b'\n\n')
	KeyboardInterrupt


## Flag
`xiomara{you_just_processed_an_image}`