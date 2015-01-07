import time
import sys

def increase_length(text, multiple_of):
    current_size = len(text)
    if current_size % multiple_of == 0:
        return text
    wanted_size = multiple_of*(len(text)/multiple_of + 1)
    return text + ' ' * (wanted_size - current_size)

def encrypt(plaintext, size):
    size = int(size)
    plaintext = increase_length(plaintext, size)
    ciphertext = []
    column_count = len(plaintext) / size
    for column in xrange(column_count):
        ciphertext += plaintext[column::column_count]
    print ''.join(ciphertext)

def decrypt(ciphertext, size):
    size = int(size)
    plaintext = []
    for row in xrange(size):
        plaintext += ciphertext[row::size]
    print ''.join(plaintext).rstrip()

def hack(ciphertext):
    tick = time.time()
    guesses = 0
    length = len(ciphertext)
    for guess in xrange(1, length):
        if length % guess == 0:
            guesses += 1
            decrypt(ciphertext, guess)
    tock = time.time()
    print 'It took %.5f seconds to try %d guesses' % (tock - tick, guesses)

def main():
    method = sys.argv[1]
    {'encrypt': encrypt,
     'decrypt': decrypt,
     'hack': hack}[method](*sys.argv[2:])

if __name__ == '__main__':
    main()