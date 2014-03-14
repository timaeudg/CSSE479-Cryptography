__author__ = 'timaeudg'
import math

ALPHA_MAPPING = {'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.127, 'f': 0.022, 'g': 0.020, 'h': 0.061,
                 'i': 0.070, 'j': 0.002, 'k': 0.008, 'l': 0.040, 'm': 0.024, 'n': 0.067, 'o': 0.075, 'p': 0.019,
                 'q': 0.001, 'r': 0.060, 's': 0.063, 't': 0.091, 'u': 0.028, 'v': 0.010, 'w': 0.023, 'x': 0.001,
                 'y': 0.020, 'z': 0.001}


def main():
    message = input("Enter a message to decode: ")
    message_list = decipher_affine(message)
    print(message_list)


def decipher_affine(message):
    valid_beta = [x for x in range(0, 26)]
    valid_alpha = [x for x in range(1, 26, 2)]
    valid_alpha.remove(13)

    possible_conversions = []
    converted_int_message = []

    for letter in message:
        converted_int_message.append(ord(letter) - 97)

    for alpha in valid_alpha:
        for beta in valid_beta:
            conversion = []
            for val in converted_int_message:
                conversion.append(chr(((alpha*val + beta) % 26) + 97))
            possible_conversions.append(''.join(conversion))
    return possible_conversions


def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)


def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)


def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))


def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag  for i in range(len(v)) ]

if __name__ == '__main__':
    main()