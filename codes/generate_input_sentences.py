import re
import random
f = open("./parallel/IITB.en-hi.en","rt")
g = open("./parallel/IITB.en-hi.hi","rt")
h = open("input_english.txt","w")
j = open("input_hindi.txt","w")

data_english = f.read()
data_hindi = g.read()
sentences_english = []
data_english_list = []
sentences_hindi = []
data_hindi_list = []

data_english_list = data_english.split("\n")
data_hindi_list = data_hindi.split("\n")

for i in range(500):
    temp = random.randint(0,1561840)
    sentences_english.append(data_english_list[temp])
    sentences_hindi.append(data_hindi_list[temp])

for i in range(len(sentences_english)):
    if len(sentences_english[i].strip())<100 and len(sentences_english[i].strip())>30:
        h.write(sentences_english[i]+"\n")
        j.write(sentences_hindi[i]+"\n")
