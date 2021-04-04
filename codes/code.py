# from main import *
import main
import re
import random

output_english = open("output_english.txt","w")

file_e = open("input_english.txt","rt")
input_english = file_e.read()
input_english = input_english.lower()
input_english = re.sub(' +', ' ', input_english)
input_english = re.sub('[^a-zA-Z \n]+', '', input_english)
input_english = re.sub('-+', ' ', input_english)
input_english_list = []
input_english_list = input_english.split("\n")
file_h = open("input_hindi.txt","rt")
input_hindi = file_h.read()
input_hindi_list = []
input_hindi_list = input_hindi.split("\n")

output_postags_english = []
output_dependency_english = []
output_dependency_hindi = []
output_postags_hindi = []

for i in range(len(input_english_list)-1):
# for i in range(40):
    doc = main.nlp_en(input_english_list[i])
    output_dependency_english.append(main.get_dependencies(doc,1))
    output_postags_english.append(main.get_pos_tags(doc,1))
    
    doc_hi = main.nlp_hi(input_hindi_list[i])
    output_dependency_hindi.append(main.get_dependencies(doc_hi,1))
    output_postags_hindi.append(main.get_pos_tags(doc_hi,1))



sov_eng = 0
svo_eng = 0
vos_eng = 0
vso_eng = 0
osv_eng = 0
ovs_eng = 0
sov_hin = 0
svo_hin = 0
vos_hin = 0
vso_hin = 0
osv_hin = 0
ovs_hin = 0

for i in range(len(output_dependency_english)):
    for j in range(len(output_dependency_english[i])) :
        ind_obj = -1
        ind_s = -1
        ind_v = -1
        for k in range(len(output_dependency_english[i][j])) :
            if output_dependency_english[i][j][k][1] == "obl" or output_dependency_english[i][j][k][1] == "obj":
                if ind_obj == -1:
                    ind_obj = k
            if output_dependency_english[i][j][k][1] == "nsubj" or output_dependency_english[i][j][k][1] == "nsubj:pass":
                if ind_s == -1:
                    ind_s = k
            if output_dependency_english[i][j][k][1] == "root":
                if ind_v == -1:
                    ind_v = k
        if ind_s < ind_obj < ind_v:
            sov_eng +=1
        elif ind_s <ind_v < ind_obj:
            svo_eng+=1
        elif ind_v<ind_obj<ind_s:
            vos_eng+=1
        elif ind_v<ind_s<ind_obj:
            vso_eng+=1
        elif ind_obj<ind_s<ind_v:
            osv_eng+=1
        elif ind_obj<ind_v<ind_s:
            ovs_eng+=1

        #     print( output_dependency_english[i][j][k][1],end=" ")
        # print()

print("word order numbers in english data","sov:",sov_eng," svo:",svo_eng," vos:",vos_eng," vso:",vso_eng," osv:",osv_eng," ovs", ovs_eng)

for i in range(len(output_dependency_hindi)):
    for j in range(len(output_dependency_hindi[i])) :
        ind_obj = -1
        ind_s = -1
        ind_v = -1
        for k in range(len(output_dependency_hindi[i][j])) :
            if output_dependency_hindi[i][j][k][1] == "obl" or output_dependency_hindi[i][j][k][1] == "obj":
                if ind_obj == -1:
                    ind_obj = k
            if output_dependency_hindi[i][j][k][1] == "nsubj" or output_dependency_hindi[i][j][k][1] == "nsubj:pass":
                if ind_s == -1:
                    ind_s = k
            if output_dependency_hindi[i][j][k][1] == "root":
                if ind_v == -1:
                    ind_v = k
        if ind_s < ind_obj < ind_v:
            sov_hin +=1
        elif ind_s <ind_v < ind_obj:
            svo_hin+=1
        elif ind_v<ind_obj<ind_s:
            vos_hin+=1
        elif ind_v<ind_s<ind_obj:
            vso_hin+=1
        elif ind_obj<ind_s<ind_v:
            osv_hin+=1
        elif ind_obj<ind_v<ind_s:
            ovs_hin+=1

        #     print( output_dependency_english[i][j][k][1],end=" ")
        # print()

print("word order numbers in hindi data","sov:",sov_hin," svo:",svo_hin," vos:",vos_hin," vso:",vso_hin," osv:",osv_hin," ovs", ovs_hin)

noun_adp_eng = 0
adj_noun_eng = 0
verb_noun_eng = 0
conj_noun_eng = 0
verb_adj_eng = 0
adv_verb_eng = 0
verb_adv_eng = 0


for i in range(len(output_postags_english)):
    for j in range(len(output_postags_english[i])):
        ind_noun = -1
        ind_adp = -1
        ind_verb = -1
        ind_adj = -1
        ind_conj = -1
        for k in range(len(output_postags_english[i][j])-1):
            if (output_postags_english[i][j][k][1] == "NOUN" or output_postags_english[i][j][k][1] == "PRON") and output_postags_english[i][j][k+1][1] == "ADP":
                noun_adp_eng+=1
            if output_postags_english[i][j][k][1] == "ADJ" and (output_postags_english[i][j][k+1][1] == "NOUN" or output_postags_english[i][j][k+1][1] == "PRON"):
                adj_noun_eng+=1
            if (output_postags_english[i][j][k][1] == "VERB" or output_postags_english[i][j][k][1] == "AUX") and (output_postags_english[i][j][k+1][1] == "NOUN" or output_postags_english[i][j][k+1][1] == "PRON"):
                verb_noun_eng+=1
            if output_postags_english[i][j][k][1] == "CCONJ" and (output_postags_english[i][j][k+1][1] == "NOUN" or output_postags_english[i][j][k+1][1] == "PRON"):
                conj_noun_eng+=1
            if (output_postags_english[i][j][k][1] == "VERB" or output_postags_english[i][j][k][1] == "AUX") and output_postags_english[i][j][k+1][1] == "ADJ":
                verb_adj_eng+=1
            if (output_postags_english[i][j][k][1] == "ADV") and (output_postags_english[i][j][k+1][1] == "VERB" or output_postags_english[i][j][k+1][1] == "AUX"):
                adv_verb_eng+=1
            if (output_postags_english[i][j][k+1][1] == "ADV") and (output_postags_english[i][j][k][1] == "VERB" or output_postags_english[i][j][k][1] == "AUX"):
                verb_adv_eng +=1
            
print()
print("for english: ")
print("noun preceeds adp:" ,noun_adp_eng)
print("adj preceeds noun: ",adj_noun_eng)
print("verb preceeds noun: ", verb_noun_eng)
print("conjuction preceeds noun: ",conj_noun_eng)
print("verb preceeds adjective: ",verb_adj_eng)
print("adverb preceeds verb: ",adv_verb_eng)
print("verb precedes adverb:",verb_adv_eng)
print()

noun_adp_hin = 0
adj_noun_hin = 0
verb_noun_hin = 0
conj_noun_hin = 0
verb_adj_hin = 0
adv_verb_hin = 0
verb_adv_hin = 0

for i in range(len(output_postags_hindi)):
    for j in range(len(output_postags_hindi[i])):
        ind_noun = -1
        ind_adp = -1
        ind_verb = -1
        ind_adj = -1
        ind_conj = -1
        for k in range(len(output_postags_hindi[i][j])-1):
            if (output_postags_hindi[i][j][k][1] == "NOUN" or output_postags_hindi[i][j][k][1] == "PRON") and output_postags_hindi[i][j][k+1][1] == "ADP":
                noun_adp_hin+=1
            if output_postags_hindi[i][j][k][1] == "ADJ" and (output_postags_hindi[i][j][k+1][1] == "NOUN" or output_postags_hindi[i][j][k+1][1] == "PRON"):
                adj_noun_hin+=1
            if (output_postags_hindi[i][j][k][1] == "VERB" or output_postags_hindi[i][j][k][1] == "AUX") and (output_postags_hindi[i][j][k+1][1] == "NOUN" or output_postags_hindi[i][j][k+1][1] == "PRON"):
                verb_noun_hin+=1
            if output_postags_hindi[i][j][k][1] == "CCONJ" and (output_postags_hindi[i][j][k+1][1] == "NOUN" or output_postags_hindi[i][j][k+1][1] == "PRON"):
                conj_noun_hin+=1
            if (output_postags_hindi[i][j][k][1] == "VERB" or output_postags_hindi[i][j][k][1] == "AUX") and output_postags_hindi[i][j][k+1][1] == "ADJ":
                verb_adj_hin+=1
            if (output_postags_hindi[i][j][k][1] == "ADV") and (output_postags_hindi[i][j][k+1][1] == "VERB" or output_postags_hindi[i][j][k+1][1] == "AUX"):
                adv_verb_hin+=1
            if (output_postags_hindi[i][j][k+1][1] == "ADV") and (output_postags_hindi[i][j][k][1] == "VERB" or output_postags_hindi[i][j][k][1] == "AUX"):
                verb_adv_hin +=1

print()
print("for hindi: ")
print("noun preceeds adp:" ,noun_adp_hin)
print("adj preceeds noun: ",adj_noun_hin)
print("verb preceeds noun: ", verb_noun_hin)
print("conjuction preceeds noun: ",conj_noun_hin)
print("verb preceeds adjective: ",verb_adj_hin)
print("adverb preceeds verb: ",adv_verb_hin)
print("verb precedes adverb:",verb_adv_hin)
print()

