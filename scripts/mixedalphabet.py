# -*- coding:utf8
import itertools
import time
import sys

alphabet = u' !"#$%&\'()*+,-./:;<=>?@[\]^_`{£}~0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzϕϴΩβε'
alphabet_length = len(alphabet)

example_key = {alphabet[i]: alphabet[(i + 32) % alphabet_length] for i in xrange(alphabet_length)}

def encrypt(plaintext, key=None):
    plaintext = unicode(plaintext)
    if key is None:
        key = example_key
    print ''.join([key[c] for c in plaintext])

def decrypt(ciphertext, key=None):
    ciphertext = unicode(ciphertext)
    if key is None:
        key = example_key
    reversed_key = {v: k for k, v in key.iteritems()}
    print ''.join([reversed_key[c] for c in ciphertext])

def hack(ciphertext):
    tick = time.time()
    guesses = 0
    try:
        for order in itertools.permutations(alphabet):
            guess = {alphabet[i]: order[i] for i in xrange(alphabet_length)}
            decrypt(ciphertext, guess)
            guesses += 1
    except:
        pass
    tock = time.time()
    print 'It took %.5f seconds to try %d guesses' % (tock - tick, guesses)
    print 'There are 9.3x10^157 possible keys'
    print 'It would take %d years to try every key' % (9.3*pow(10, 157) / (guesses / (tock - tick)) / (60*60*24*364), )
    print 'Folding@home has close to 200,000 active computers and could try every guess in %d years' % (9.3*pow(10, 157) / (20.7*pow(10, 15)) / (60*60*24*364), )

def main():
    method = sys.argv[1]
    {'encrypt': encrypt,
     'decrypt': decrypt,
     'hack': hack}[method](*sys.argv[2:])

if __name__ == '__main__':
    main()