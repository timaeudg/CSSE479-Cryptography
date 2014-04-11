__author__ = 'Kenny'
import math
import PrimeFactorizer
import ModularSqrt

def main():
    print mod_sqrt(71, 77)

    return


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


def modular_inverse(value, mod):
    gcd, x, y = extended_euclidean(value, mod)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % mod


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


def solve_series_of_linear_congruences(a, m, b, n):
    k = solve_linear_congruence(n, (a-b), m)
    return (b + n*k) % (m*n)


def smart_power(base, exp, mod):
    if exp < 10:
        return (base**exp) % mod
    accum = 1
    power_accum = base
    while accum < exp/2:
        power_accum *= power_accum
        power_accum %= mod
        accum *= 2
    diff = exp - accum
    power_accum = (power_accum * smart_power(base, diff, mod)) % mod

    return power_accum


# This is pretty useless but fuck you devon
def modular_evaluation(base, exponent, mod):
    while exponent > mod:
        exponent -= (mod - 1)
    return base**exponent % mod


def phi(n):
    ret = 0
    for i in range(0,n):
        if rel_prime(i, n):
            ret += 1
    return ret


def rel_prime(a, b):
    gcd, x, y = extended_euclidean(a, b)
    return gcd == 1


def factor_number(n):
    factors = []
    for x in range(1, int(math.ceil(math.sqrt(n)))):
        if n % x == 0:
            factors.append(x)
            factors.append(n/x)
    factors.sort()
    return factors


def get_rel_primes_less_than(n):
    ret = []
    for i in range(1,n):
        if rel_prime(i,n):
            ret.append(i)
    return ret


def find_primitive_roots(mod):
    primroots = []
    candidates = factor_number(mod-1)
    primes = PrimeFactorizer.factorization(mod-1).keys()
    for x in candidates:
        flag = 1
        for y in primes:
            calc = x**((mod-1)/y)
            if calc % mod == 1:
                flag = 0
                break
        if flag == 1:
            primroots.append(x)
        else:
            flag = 1
    relprimeexps = get_rel_primes_less_than(mod-1)
    for prime in primroots:
        for relprimeexp in relprimeexps:
            k = prime**relprimeexp % mod
            if k not in primroots:
                primroots.append(k)
    primroots.sort()
    for q in range(0,len(primroots)):
        primroots[q] = int(primroots[q])
    return primroots


def mod_sqrt(a, p):
    if PrimeFactorizer.isprime(p):
        return ModularSqrt.modular_sqrt(a, p)
    else:
        return brute_force_square_solver(a, p)

def brute_force_square_solver(a, mod):
    solutions = []
    for i in range(1, mod):
        if i**2 % mod == a:
            solutions.append(i)
    return solutions



if __name__ == '__main__':
    main()