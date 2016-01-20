import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

input1 = raw_input("Input the first phrase: ")
input2 = raw_input("Input the second phrase: ")
phrase1=word_tokenize(input1)
phrase2=word_tokenize(input2)

#declare two arrays to hold the words from phrases
arr1=[]
arr2=[]

#split phrases into words
result1 = nltk.pos_tag(phrase1)
result2 = nltk.pos_tag(phrase2)

#put only verbs,adjectives or nouns in arrays
for i in result1:
    if(i[1].startswith('NN')  or i[1].startswith('JJ') or i[1].startswith('VB')):
        arr1.append(i[0])
for i in result2:
    if(i[1].startswith('NN')  or i[1].startswith('JJ') or i[1].startswith('VB')):
        arr2.append(i[0])

#we iterate threw the arrays to find synonyms between the two sentences
synonyms = []
for m in range(len(arr1)):
    for l in range(len(arr2)):
        for syn1 in wordnet.synsets(arr1[l]):
            for lemma in syn1.lemmas():
                #if we have synonyms,we print them and add them to synonyms array
                if(lemma.name() == arr2[l]):
                    synonyms.append(lemma.name())
                    print lemma.synset(),",",arr2[l]

#print the synonyms array
print set(synonyms)