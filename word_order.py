#!/usr/bin/env python3

### INPUT
while True:
    x=int(input()) # Number of INPUTs
    if x>1 and x<=100000:
        break
    else:
        quit()
words={} # Collection of INPUTs, has do be dict because list research is too slow
for i in range(x):
    word=input()
    if word not in words:
        new_word={word:1}
        words.update(new_word)
    else:
        words[word]+=1
### OUTPUT
print(str(len(words)))
string=''
for i in words.values():
    string=string+str(i)+' '
print(string)
