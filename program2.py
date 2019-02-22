from collections import OrderedDict
import time

txt = open('source.txt','r').read().split()
words  = {}

thresh = 2
itemNumber = 3

start_time = time.clock()  #start time

for word in txt:
    if word not in words.keys():
        words[word] = 1
    else:
        words[word] = words[word]+1

sorted_words  = OrderedDict(sorted(words.items(), key = lambda x: x[1], reverse=True))

#for k,v in sorted_words.items():
#   print"%s:%s" % (k.decode('utf-8'),v)


#zwracanie maksymalnie itemNumber par z czolowki wystepujacych conajmniej thresh razy
i = 0

for key,val in sorted_words.items():
    if val >= thresh and i < itemNumber:
            print "\nThe winner is word:  %s => %s" % (key.decode('utf-8'),val)
            i=i+1
print "\n --- %s sekund ---" %(time.clock() - start_time)

