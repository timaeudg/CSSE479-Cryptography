__author__ = 'Icarus'


def main():

    print(problem3())
    print(problem4())
    print(problem7())
    print(problem9())


def problem3():
    big_number = 3 ** 1234567
    answer = big_number % 100000
    return answer


def problem4():
    return (modular_inverse(314, 11111)*271) % 11111


def modular_inverse(value, mod):
    gcd, x, y = extended_euclidean(value, mod)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % mod


def extended_euclidean(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def problem7():
    n = 17*23
    bool_exp = 1 == 2**(n-1) % n
    print(bool_exp)
    for x in range(1, 100000):
        if ((2**x) % 391) == 1:
            return x
    return False


def problem9():
    roots_found = {}
    for x in range(1, 65537):
        val = (3**x) % 65537
        if val in roots_found:
            return False
        else:
            roots_found[val] = True
    return True

if __name__ == '__main__':
    main()
