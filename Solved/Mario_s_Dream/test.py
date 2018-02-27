
def count_p(x, starting=None):
    p = starting
    count = 0
    while 1 <= p:
        p -= 1
        if p ^ x > x:
            print(f"{p} - {bin(p)} XOR {bin(x)} = {bin(p ^ x)} YES")
            count += 1
        else:
            print(f"{p} - {bin(p)} XOR {bin(x)} = {bin(p ^ x)}")
            continue
    return count

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
    print(count)
    return count

def count_static(x):
    # all ones
    all_ones = (1 << x.bit_length()) - 1
    print(all_ones - x)
    return all_ones - x

def test_optimisation(x):
    a = count_p(x, x)

    bits = len(bin(x)[2:].lstrip('1'))
    starting = (1 << bits)
    b = count_p(x, starting)
    print(a, b)
    assert a == b

    return b

#assert test_optimisation(43343) == count_optimised(43343)

count_optimised(43343)
count_static(43343)



