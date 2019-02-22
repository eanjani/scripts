# Program 1 description #

Program fetches content of http page specified by user and saves data to local .html file
Program allows to save content to txt file, with removal of html tags and punctuation marks.

# Program 2 description #
Program is using program 1 to fetch needed data.
Scripts is finding k most common words in file and print it in sorted order together with number of occurencies.

It is using naive alghoritm:
1. sort all the words in document
2. mark duplicated words as a pair (word, amount of occurencies)
3. sort once again by amount of occurencies
4. return maximum N top results

# Program 3 description #
Program is using program 1 to fetch needed data.
Program is helping to define similarity between text documents, calculated as a cosinus of angle between vectors generated for each document. To generate vectors, program is using so called term count model, where weight of each word is presented as:

word_weight = word occurencies / sum of all words in document

example:

Doc#1: This is a dog
Doc#2: She has a black dog
Doc#3: Cat doesn't like this dog

Dictionary: a, black, cat, doesn't, dog, has, is, like, she, this

vector for doc#1: [1/4, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 1/4]
vector for doc#2: [1/5, 1/5, 0, 0, 1/5, 1/5, 0, 0, 1/5, 0]
vector for doc#3: [0, 0, 1/5, 1/5, 1/5, 0, 0, 1/5, 0, 1/5]


# Program 4 description #
Program is parsing hyperlinks from dowloaded html file.
Hyperlinks are saved in 2 files, depending if they comes from the same server or they are external.


