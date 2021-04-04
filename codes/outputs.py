# from main import *
import main
import re
import random

# output_english = open("output_english.txt","w")

# file_e = open("input_english.txt","rt")
# input_english = file_e.read()
# input_english = input_english.lower()
# input_english = re.sub(' +', ' ', input_english)
# input_english = re.sub('[^a-zA-Z \n]+', '', input_english)
# input_english = re.sub('-+', ' ', input_english)
# input_english_list = []
# input_english_list = input_english.split("\n")
file_h = open("./../Hin_50_sent.txt","rt")
input_hindi = file_h.read()
input_hindi_list = []
input_hindi_list = input_hindi.split("\n")

output_postags_english = []
output_dependency_english = []
output_dependency_hindi = []
output_postags_hindi = []

for i in range(len(input_hindi_list)-1):
# for i in range(40):
    # doc = main.nlp_en(input_english_list[i])
    # output_dependency_english.append(main.get_dependencies(doc,1))
    # output_postags_english.append(main.get_pos_tags(doc,1))
    
    doc_hi = main.nlp_hi(input_hindi_list[i])
    output_dependency_hindi.append(main.get_dependencies(doc_hi,1))
    output_postags_hindi.append(main.get_pos_tags(doc_hi,1))

# print("pos tags english:")
# for i in output_postags_english:
#     print(i)
# print("dependency english")
# for i in output_dependency_english:
#     print(i)
print("pos tags hindi")
for i in output_postags_hindi:
    print(i)
print("dependency hindi")
for i in output_dependency_hindi:
    print(i)

