import time
from collections import deque
from sympy import randprime


def mod_squarings_per_sec(prime_bit_size):
    min_prime = (2**prime_bit_size) // 2
    max_prime = (2**prime_bit_size) - 1
    p = randprime(min_prime, max_prime)
    q = randprime(min_prime, max_prime)
    n = p*q

    start = time.time()
    print((2**2047) % n)
    end = time.time()

    return end - start


def create_puzzle(key, t, p, q, base=2):
    n = p*q
    totient = (p-1) * (q-1)
    e = 2**t % totient
    return (key + base ** e) % n


def solve(puzzle, t, n, base=2):
    return (puzzle - base**(2**t)) % n


def caeser_encrypt(key, message):
    char_list = deque(list(message))
    char_list.rotate(key)
    return ''.join(char_list)


def caeser_decrypt(key, ciphertext):
    char_list = deque(list(ciphertext))
    char_list.rotate(-key)
    return ''.join(char_list)


if __name__ == '__main__':
    num_bits = int(1024 / 2)
    min_prime = (2**num_bits) // 2
    max_prime = (2**num_bits) - 1
    p = randprime(min_prime, max_prime)
    q = randprime(min_prime, max_prime)
    t = 27

    key = 2
    message = 'timelock'
    ciphertext = caeser_encrypt(key, message)

    puzzle = create_puzzle(key, t, p, q)
    print('Creating puzzle with these parameters: ')
    print('  key = ', key)
    print('  message = ', message)
    print('  ciphertext = ', ciphertext)
    print('  p = ', p)
    print('  q = ', q)
    print('  t = ', t)

    start_time = time.time()
    found_key = solve(puzzle, t, p*q)
    found_message = caeser_decrypt(found_key, ciphertext)
    print('Found Key: ', found_key)
    print('Found Message: ', found_message)
    print('Time to solve puzzle: ', time.time() - start_time, 'seconds')
