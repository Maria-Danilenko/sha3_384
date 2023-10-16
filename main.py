# import hashlib
#
# #https://docs.python.org/uk/3/library/hashlib.html
# #https://emn178.github.io/online-tools/sha3_384.html
#
# file = open('matrix.txt', mode='r')
# matrix = file.read()
# file.close()
#
# gfg = hashlib.sha3_384()
# gfg.update(matrix.encode())
#
# print(gfg.hexdigest())

import hashlib
import itertools
import time

# Decrypt by hash
def brute_force(hash, symbols):
    repeat = 0
    while True:
        for sequence in itertools.product(symbols, repeat=repeat):
            word_try = ''.join(sequence)
            if hashlib.sha3_384(word_try.encode()).hexdigest() == hash:
                return word_try
        repeat = repeat + 1


if __name__ == '__main__':
    # Data
    symbols = ['1', '0', '#']

    # Open file
    file = open('matrix.txt', mode='r')
    message = file.read()
    file.close()

    # Hash
    hash = hashlib.sha3_384(message.encode()).hexdigest()
    print("Hash: %s" % hash)

    # Brute forcing
    print("Brute-forcing...")
    start = time.time()
    result = brute_force(hash, symbols)
    end = time.time()
    runtime = end - start
    print("Runtime: %s seconds" % runtime)
    print("Brute-force result: %s" % result)