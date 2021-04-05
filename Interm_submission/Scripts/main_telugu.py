import stanza


def get_dependencies(doc, n):
    """Get dependencies in the format of a list of
    (token, deprel, dependent_token) pairs- 
    for all 'n' sentences in doc"""

    def getdeps(i):
        deps = []
        for head, rel, dep in doc.sentences[i].dependencies:
            deps.append((head.text, rel, dep.text))
        return deps

    return [getdeps(i) for i in range(n)]


def get_pos_tags(doc, n):
    """Get POS-tagged tokens in the format of a list of 
    (token, POStag) pairs for all sentences in doc.
    Returns upos (Universal part-of-speech) tag only, not 
    xpos (treebank-specific part of speech)"""

    def getpos(i):
        tokens = []
        for token in doc.sentences[i].words:
            tokens.append((token.text, token.upos))
        return tokens

    return [getpos(i) for i in range(n)]

# ==== MAIN: English ====
stanza.download('te')
nlp_en = stanza.Pipeline('te') # This sets up a default neural pipeline in English
f = open('data/Tel_50_sent.txt', 'r')
data_en = f.readlines()
f.close()
#data = data.replace('.', '')
#data = data.replace("\n", '. ').replace("\r", ". ")
#doc = nlp_en("Barack Obama was born in Hawaii.  He was elected president in 2008.")
f = open('telugu_depdency_50.txt', 'w', encoding = 'utf-8')
for sent in data_en:
	doc_en = nlp_en(sent)
	# this prints the dependencies in a human-readable format	
	#print(get_dependencies(doc, 1))
	for output in get_dependencies(doc_en, 1):
		for triplet in output:
			#print(triplet)
			f.write(', '.join(triplet) )
			f.write('\n')	
		f.write('============\n')
f.close()
print("Completed Telugu dependency")

# this prints the POS-tagged sentence in a human-readable format

f = open('telugu_pos_50.txt', 'w', encoding = 'utf-8')
for sent in data_en:
	doc_en = nlp_en(sent)
	# this prints the dependencies in a human-readable format	
	#print(get_pos_tags(doc, 1))
	for output in get_pos_tags(doc_en, 1):
		for pair in output:
			#print(triplet)
			f.write(', '.join(pair) )
			f.write('\n')	
		f.write('============\n')
f.close()
print("Completed Telugu POS")
#print(get_pos_tags(doc, 2))
#f = open('english_pos.txt', 'w', encoding = 'utf-8')
#print(get_pos_tags(doc, 4))
#for output in get_pos_tags(doc, 4):
#	for triplet in output:
#		#print(triplet)
#		f.write(', '.join(triplet) )
#		f.write('\n')	
#	f.write('============\n')
#f.close()

# ==== MAIN: Hindi ====

# this sets up a default neural pipeline for Hindi
#stanza.download('hi')
#nlp_hi = stanza.Pipeline('hi')
#f = open('data/hindi.txt', 'r')
#data_hi = f.readlines()
#f.close()

#f = open('hindi_depdency.txt', 'w', encoding = 'utf-8')
#for sent in data_hi:
#	doc_hi = nlp_hi(sent)
#	# this prints the dependencies in a human-readable format	
	#print(get_dependencies(doc, 1))
#	for output in get_dependencies(doc_hi, 1):
#		for triplet in output:
#			#print(triplet)
#			f.write(', '.join(triplet) )
#			f.write('\n')	
#		f.write('============\n')
#f.close()

#print("Completed Hindi dependency")
# this prints the POS-tagged sentence in a human-readable format

#f = open('hindi_pos.txt', 'w', encoding = 'utf-8')
#for sent in data_hi:
#	doc_hi = nlp_hi(sent)
	# this prints the dependencies in a human-readable format	
	#print(get_pos_tags(doc, 1))
#	for output in get_pos_tags(doc_hi, 1):
#		for pair in output:
			#print(triplet)
#			f.write(', '.join(pair) )
#			f.write('\n')	
#		f.write('============\n')
#f.close()
#print("Completed Hindi POS")


#doc_hi = nlp_hi("नमस्ते तुम कैसे हो")
#doc_hi = nlp_hi(data)
# this accesses the list of Token objects in the sentence
# for more on the data structures in a Document, see here:
# https://stanfordnlp.github.io/stanza/data_objects.html
#print(doc_hi.sentences[0].tokens)

# this prints the dependency tree in a human-readable format
#doc_hi.sentences[0].print_dependencies()

# same set of functions as above- but for Hindi
#print(get_dependencies(doc_hi, 1))
#print(get_pos_tags(doc_hi, 1))

