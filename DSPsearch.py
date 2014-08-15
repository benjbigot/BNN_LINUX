import nltk
from nltk import *
def DSPsearch(transcript):
		tokenforsearch=[[] for _ in range(len(transcript))]
		tokenized=[]
		for i in range(len(transcript)):
			tokenized=nltk.word_tokenize(transcript[i][2])
			tagged=nltk.pos_tag(tokenized)
			tokenforsearch[i].append(transcript[i][0])
			tokenforsearch[i].append(transcript[i][1])     
			for z in range(len(tagged)):
					 lowercase=tagged[z][0].lower()
					 if(tagged[z][1]=="NNP" or tagged[z][1]=="NN"):  
						 tokenforsearch[i].append(tagged[z][0])		
		return tokenforsearch