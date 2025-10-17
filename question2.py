import string
import itertools
letters=list(string.ascii_lowercase)
print(letters)
def l(letter1, letter2):
    int1=letters.index(letter1)
    int2=letters.index(letter2)
#    print("int1:"+str(int1))
#    print("int2:"+str(int2))
    if int2>int1:
        diff1=int2-int1
        diff2=len(letters)-int2+int1
    else:
        diff1=int1-int2
        diff2=len(letters)+int2-int1
    if diff1>diff2:
        smallest_path=diff2
        largest_path=diff1
    else:
        smallest_path=diff1
        largest_path=diff2
    return [smallest_path,largest_path]
def paths(sample):
    smallest_path_word=0
    largest_path_word=0
    for i in range(0,len(sample)-1):
        smallest_path_word += l(sample[i],sample[i+1])[0]
        largest_path_word += l(sample[i],sample[i+1])[1]
#    print(smallest_path_word)
#    print(largest_path_word)
    return smallest_path_word

word = "ritangle"
permutation= itertools.permutations(word)
combos = []
for val in permutation:
    combos.append(str(''.join(val)))
#print(combos)
#print(len(combos))
paths("ritangle")
smallest=paths("ritangle")
small_word=""
largest=paths("ritangle")
large_word=""
for i in combos:
    contender=paths(i)
    if int(contender)<smallest:
        smallest=contender
        small_word=i
    if contender>largest:
        largest=contender
        large_word=i
        print(i)
print("smallest: "+small_word+",  "+str(smallest))
print("largest: "+large_word+",  "+str(largest))
print("result:  "+str(smallest*largest))