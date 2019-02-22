from os import listdir
from os.path import isfile, join
from collections import OrderedDict
import math
from itertools import combinations

def cosine_similarity(v1,v2):
        
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return round(sumxy/math.sqrt(sumxx*sumyy),4)


path = 'C:/Users/Ania/Desktop/EDwI/LAB3/'
files = [f for f in listdir(path) if isfile(join(path,f))]
vectors = {}
stats = {}

global_words = {} #all words from all files -> word:amount of global occurences
files_words = {} #words in particular files -> file:[list of words in file]

def get_all_words(f):
    full_path = join(path,f)
    txtFile = open(full_path, 'r')
    words = txtFile.read().split()

    for word in words:
        if word not in global_words.keys():
            global_words[word] = 1
        else:
            global_words[word] = global_words[word]+1

    files_words[f]=words
    txtFile.close();
    
for plik in files:
    get_all_words(plik)

for plik in files:
    vec = []
    #svec = [] # lista robocza
    total = len(files_words[plik])
    for key in sorted(global_words.keys()):
        value = float(files_words[plik].count(key))
        #svec.append(" "+str(value)+"/"+str(total))
        vec.append(round((value/total),4))
    #print svec
    vectors[plik] = vec
#print vectors[vectors.keys()[0]]
#print vectors[vectors.keys()[1]]

results = {}
for para in list(combinations(vectors.keys(),2)):
    results[para] = cosine_similarity(vectors[para[0]],vectors[para[1]])
    #print results
    
#print sorted_results

print "10 najlepszych wyników: "
newA = OrderedDict(sorted(results.iteritems(), key=lambda x: x[1], reverse=True)[:10]) # sortowanie malejace
for k, v in newA.items():
    print k[0]+" " +k[1]+" = "+str(v)

print "\n 10 najgorszych wynikow: "
newB = OrderedDict(sorted(results.iteritems(), key=lambda x: x[1], reverse=False)[:10]) #sortowanie rosnace
for k, v in newB.items():
    print k[0]+" "+k[1] +" = "+str(v)


#print files_words['widlogonki.txt']
#print files_words['fuga.txt']

#print set(files_words['widlogonki.txt']) & set(files_words['fuga.txt'])


