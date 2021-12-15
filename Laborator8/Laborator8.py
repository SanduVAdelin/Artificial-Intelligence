import lightrdf
import sys
import nltk
from nltk import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

f = open('computer-science.txt', encoding="mbcs")

text = f.read()
lower_case = text.lower()
f_out = open("output.txt", "a", encoding="mbcs")
f_out_2 = open("output_concepts.txt", "a", encoding="mbcs")
f_out.truncate(0)
f_out_2.truncate(0)

owl_path = "./CSO.3.3.owl"

data = []
doc = lightrdf.RDFDocument(owl_path)
list_of_concepts = []

word = sys.argv[1]
print('Cuvantul pe care trebuie sa il cautam este : ' + word)

for triple in doc.search_triples(None, None, None):
    line = []
    for v in triple:
        line.append(v)
    data.append(line)

for n1, m, n2 in data:
    s1 = n1
    s2 = n2
    index1 = s1.rfind('/')
    index2 = s2.rfind('/')
    if 'superTopicOf' in m:
        if s1[index1 + 1:] == word or s2[index2 + 1:] == word:
            print(n1, 'superTopicOf', n2)
    list_of_concepts.append(s1[index1 + 1:])
    list_of_concepts.append(s2[index2 + 1:])

# print(list_of_concepts)
unique_list_of_concepts = list(set(list_of_concepts))
sentences = nltk.sent_tokenize(lower_case)
number_of_sentences = len(sentences)
index = 0

for index in range(0, number_of_sentences):
    sentence_token = nltk.pos_tag(nltk.word_tokenize(sentences[index]))

    noun1_found = 0
    noun2_found = 0
    verb_found = 0
    index_word = 0
    for index_word in range(0, len(sentence_token)):
        if 'NN' in sentence_token[index_word][1] and noun1_found == 0:
            noun1_found = 1
        if 'VB' in sentence_token[index_word][1] and noun1_found == 1:
            verb_found = 1
        if 'NN' in sentence_token[index_word][1] and verb_found == 1:
            noun2_found = 1

    if noun1_found == 1 and noun2_found == 1 and verb_found == 1:
        f_out.write(sentences[index])
        f_out.write('\n')
        word_list = sentences[index].split()
        for word in word_list:
            if word in unique_list_of_concepts:
                f_out_2.write(sentences[index])
                f_out_2.write('....')






