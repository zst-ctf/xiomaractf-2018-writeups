# Mario's Dream
Misc - 100 points

## Challenge 
> Welcome again challenger!!

> Our Young Mario was dreaming about Xors when he was struck with a question.Help him solve his question.

> Challenge is running at 139.59.28.4:1352

## Solution

The program:

    $ nc 139.59.28.4 1352
        
     Question:  
        Given x , we need to find the numbers less than x such that (p xor x) > x where 1<=p<x
        Constrict time as much as possible as the solution given here takes (t * log n) time , where t is the number of test cases.
     
     Input Format:
        Line 1 : No of test cases (t)
        Next t lines are the values of x

    Output Format:
        Single line stating the count of numbers where than p xor x > x

    71567
    98477

---

#### O(t * n!)

We can bruteforce from `0 to x` and check the XOR result. 

    def count_p(x):
        p = x
        count = 0
        while 1 <= p:
            p -= 1
            if p ^ x > x:
                count += 1
        return count

However, if we do normal bruteforce, the time complexity will be O(t * n!) and we will receive `Time's up!!`

#### O(t * n!/2)

How to shorten the time:
- To make it less than x, we just need to zero out the 1-MSBs, hence all those numbers touching the 1-MSBs will make the number smaller.
- We can speed up the time by starting from the number which touches the first 0-MSB.

So now change starting value of `p = x` to...
    
    bits = len(bin(x)[2:].lstrip('1'))
    starting = (1 << bits)
    p = starting

Unfortunately, the time is still too long

#### O(t * log n)

Now, I coded some test outputs (`out.txt`) and from what info I understand, building up from the previous...

If we zero out the 1 bits, then the number becomes smaller...

So we can check for each bit, if it is equal to 1, then add its weight to the count

This is indeed `log n` style and hence it will be much faster...

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

> python3 solve.py

Good gravy, it is still not fast enough due to network overhead. Let's optimise one step further.

#### O(t * 1)?

If we look at `count_optimised()`, 
isn't it just adding up all the zero bits?

Hence, we can just do a bit flip and that's out number already!

    def count_static(x):
        # all ones
        all_ones = (1 << x.bit_length()) - 1
        return all_ones - x

#### Success

Last thing to note... Remove the overhead of the print function `-.-`

    $ python3 solve.py 
    Traceback (most recent call last):
      File "solve.py", line 61, in <module>
        main()
      File "solve.py", line 53, in main
        number = int(data)
    ValueError: invalid literal for int() with base 10: 'Success, the flag is xiomara{link_lists_are_cool_btw}'

## Flag
`xiomara{link_lists_are_cool_btw}`