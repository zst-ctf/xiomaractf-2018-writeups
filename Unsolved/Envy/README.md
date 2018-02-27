# Envy
Reverse Engineering - 100 points

## Challenge 
> The environment is everything that isn't me.

> [envy](envy)

## Solution

Running normally, we get this
    
    $ ./envy 0 0      
    Unauthorized access !!!!
    : Success

Decompile in Hopper

    int EntryPoint_2() {
        rax = 0x0;
        if (ptrace(0x0, 0x0, 0x0, 0x0) < 0x0) {
                rax = puts("********** Stack smashing Detected ********");
                rax = exit(0x0);
        }
        else {
                rax = getenv("ctor_");
                *0x201120 = rax;
                var_8 = 0x0;
                for (var_4 = 0x0; var_4 <= 0x36; var_4 = var_4 + 0x2) {
                        rax = 0x201140;
                        *(int8_t *)(sign_extend_64(var_8) + rax) = *(int32_t *)(sign_extend_32(var_4) * 0x4 + 0x201020);
                        var_8 = var_8 + 0x1;
                }
        }
        return rax;
    }

    int sub_968(int arg0, int arg1) {
        if (*0x201120 == 0x0) {
                perror("Unauthorized access !!!!\n");
                rax = 0x0;
        } else {
                if (strcmp(*0x201120, 0x201140) == 0x0) {
                        puts("Well done by now u should have ur flag");
                }
                strcpy(&var_50, *0x201120);
                if (0x0 == 0xd0a0d0a) {
                        puts("Oh no ther is a buffer overflow here :(");
                }
                else {
                        printf("Try again, you got 0x%08x\n", 0x0);
                }
                rax = 0x0;
        }
        rcx = *0x28 ^ *0x28;
        if (rcx != 0x0) {
                rax = __stack_chk_fail();
        }
        return rax;
    }

---
Add an environment variable `ctor_`

    $ export ctor_="derp"
    $ ./envy                                                 
    Try again, you got 0x00000000


We can do until a length of 72, at length 73, it detects stack smashing

    $ export ctor_=$(pwn cyclic 72)
    $ ./envy
    Try again, you got 0x00000000

    $ export ctor_=$(pwn cyclic 73)
    $ ./envy
    Try again, you got 0x00000000
    *** stack smashing detected ***: ./envy terminated

---

We need to make `eax == 0xd0a0d0a` (as seen in the source), we will get a message...

    00000000000009eb         cmpl       $0xd0a0d0a, %eax
    00000000000009f0         jne        loc_a00
    00000000000009f2         leaq       aOhNoTherIsABuf, %rdi
    ; argument "s" for method j_puts, "Oh no ther is a buffer overflow here :("
    00000000000009f9         call       j_puts                                      ; puts
    00000000000009fe         jmp        loc_a16

???

    $ export ctor_=$(python -c 'print "A"*72 + "\x0a\x0d\x0a\x0d"')
    $ ./envy

???

http://www.aboureada.com/buffer_overflow/2017/12/18/exploiting_protostar_stack2.html


## Flag
`?`