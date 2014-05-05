__author__ = 'Icarus'


# Solves in the form ax = b (mod mod)
def solve_linear_congruence(a, b, mod):
    gcd, x, y = extended_euclidean(a, mod)
    if gcd == 1:
        return x*b % mod
    elif b % gcd == 0:
        newa = a / gcd
        newb = b / gcd
        newmod = mod / gcd
        ans = solve_linear_congruence(newa, newb, newmod)
        ret = []
        while ans < mod:
            ret.append(ans)
            ans = ans + newmod
        return ret
    else:
        return None


# ax + by = gcd(a, b)1
# This takes in a and b and returns the gcd, x, and y.
def extended_euclidean(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def split_message(message):
    result_list = []
    for i in range(0, len(message), 3):
        string_value = message[i] + message[i+1] + message[i+2]
        result_list.append(int(string_value))
    return result_list


def encode_to_ascii(char_list):
    result = []
    for char in char_list:
        result.append(chr(char))
    return result


def smart_power(base, exp):
    if exp < 10:
        return base**exp
    accum = 1
    power_accum = base
    while accum < exp/2:
        power_accum *= power_accum
        accum *= 2
    diff = exp - accum
    power_accum = (power_accum * smart_power(base, diff))

    return power_accum


def smart_mod_power(base, exp, mod):
    if exp < 10:
        return (base**exp) % mod
    accum = 1
    power_accum = base
    while accum < exp/2:
        power_accum *= power_accum
        power_accum %= mod
        accum *= 2
    diff = exp - accum
    power_accum = (power_accum * smart_mod_power(base, diff, mod)) % mod

    return power_accum


def main():
    message_text = input('Encrypted Message: ')
    n_text = input('n value: ')
    n_int = int(n_text)
    p = smart_power(10, 110) + 7
    q = smart_power(10, 111) + 139
    p_minus = p - 1
    q_minus = q - 1
    d = solve_linear_congruence(5, 1, q_minus * p_minus)
    message_int = int(message_text)
    decrypted = smart_mod_power(message_int, d, n_int)
    string_decrypted = repr(decrypted)
    if len(string_decrypted) % 3 == 0:
        split = split_message(repr(decrypted))
    elif len(string_decrypted) % 3 == 1:
        split = split_message('00'+repr(decrypted))
    else:
        split = split_message('0'+repr(decrypted))
    char_message = encode_to_ascii(split)
    print(''.join(char_message))
    return


if __name__ == "__main__":
    main()