import string
import itertools
import time
import jax
import jax.numpy as jnp
start=time.time()
letters=list(string.ascii_lowercase)
print(letters)


def l(letter1, letter2):
    return abs(letters.index(letter2)-letters.index(letter1))

def paths(sample):
    smallest_path_word=0
    for i in range(0,len(sample)-1):
        smallest_path_word += l(sample[i],sample[i+1])
#    print(smallest_path_word)
#    print(largest_path_word)
    return smallest_path_word
def permutations(word: str,smallest: int, largest: int):
    for i in itertools.permutations(word):
        contender = paths(''.join(i))
        if int(contender)<smallest:
            smallest=contender
            small_word=''.join(i)
        if contender>largest:
            largest=contender
            large_word=''.join(i)
    return smallest, small_word, largest, large_word


word = "ritangle"
permutation= itertools.permutations(word)
combos = []
for val in permutation:
    combos.append(str(''.join(val)))
#print(combos)
#print(len(combos))
#paths("ritangle")
smallest=paths("ritangle")
small_word=""
largest=paths("ritangle")
large_word=""
smallest, small_word, largest, large_word = permutations("ritangle",smallest,largest)
#for i in combos:
#    contender=paths(i)
#    if int(contender)<smallest:
#        smallest=contender
#        small_word=i
#    if contender>largest:
#        largest=contender
#        large_word=i
#        print(i)
end=time.time()
print("Time taken: "+str(end-start)+" seconds")
print("smallest: "+small_word+",  "+str(smallest))
print("largest: "+large_word+",  "+str(largest))
print("result:  "+str(smallest*largest))