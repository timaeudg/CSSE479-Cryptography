__author__ = 'timaeudg'
import math
from operator import itemgetter

ALPHA_MAPPING = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061,
                 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019,
                 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001,
                 0.020, 0.001]


def main():
    message = input("Enter a message to decode: ")
    message_list = decipher_affine(message.lower())
    for message in message_list:
        print(message)


def decipher_vigenere(message):
    key_lengths = find_probable_key_lengths(message)
    for k_length in key_lengths:
        print(k_length)
    key_length = int(input("What key length would you like to try?: "))

    key = find_decryption_key(message, key_length)
    return [key]


def find_decryption_key(message, key_length):
    resultant_key = []

    for x in range(0, key_length):
        resultant_key.append(find_letter(message, x, key_length, resultant_key))

    return resultant_key


def find_letter(message, pos, length, key_thusfar):
    partial_deciphers = []

    message_thusfar = list(message)
    for x in range(0, len(key_thusfar)):
        message_thusfar = partially_decipher(message_thusfar, x, length, ord(key_thusfar[x])-97)
    print(message_thusfar)

    for letter in range(0, 26):
        converted_letter = chr(letter+97)
        partial_message = partially_decipher(message_thusfar, pos, length, letter)
        frequency = normalize(count_letters(partial_message))
        partial_deciphers.append((converted_letter, pearson_def(frequency, ALPHA_MAPPING)))
    sorted_list = sorted(partial_deciphers, key=itemgetter(1), reverse=True)

    return sorted_list[0][0]


def partially_decipher(message, pos, length, letter):
    converted_int_message = []

    for character in message:
        converted_int_message.append(ord(character) - 97)

    for x in range(pos, len(message), length):
        converted_int_message[x] -= letter
        converted_int_message[x] %= 26

    string_message = []
    for val in converted_int_message:
        string_message.append(chr(val+97))

    return string_message


def find_probable_key_lengths(message):
    to_return = []
    for x in range(1, len(message)):
        displaced_message = displace_message(message, x)
        number_of_coincidences = count_coincidences(message, displaced_message)
        to_return.append((x, number_of_coincidences))
    to_return = sorted(to_return, key=itemgetter(1), reverse=True)
    return to_return


def displace_message(message, dist):
    padded = ' '*dist + message
    return padded[:-dist]


def count_coincidences(message, displaced):
    coincidences = 0
    for index in range(0, len(message)):
        if message[index] == displaced[index]:
            coincidences += 1
    return coincidences


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
            possible_conversions.append(conversion)

    correlated_conversions = []
    for conversion in possible_conversions:
        frequency = normalize(count_letters(conversion))
        correlated_conversions.append((conversion, pearson_def(frequency, ALPHA_MAPPING)))
    sorted_correlated_conversions = sorted(correlated_conversions, key=itemgetter(1), reverse=True)

    to_return = []
    for conversion in sorted_correlated_conversions:
        to_return.append((''.join(conversion[0]), conversion[1]))
    return to_return


def count_letters(list_of_characters):
    count_list = [0 for x in range(0, 26)]
    for letter in list_of_characters:
        count_list[ord(letter) - 97] += 1
    return count_list

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


def normalize(v):
    total_occurrences = sum(v)
    return [ (v[i])/total_occurrences for i in range(len(v)) ]


if __name__ == '__main__':
    main()