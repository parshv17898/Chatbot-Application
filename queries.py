from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np
import json
import re
lem = WordNetLemmatizer()
with open("idf.txt",'rb') as fp:
	idf = pickle.load(fp)
with open("words.txt",'rb') as fp:
	words = pickle.load(fp)
with open("datasetx.txt",'rb') as fp:
	X = pickle.load(fp)
	X = np.array(X)
file_path = "/home/apurv/Downloads/chatbot/previous_chats.json"
j = 0	
accuracy = 0
while 1:
	query = raw_input('You: ')
	query = re.sub('\W+',' ', query)
	m1 = lem.lemmatize(query,'v')
	m2 = lem.lemmatize(query,'n')
	if len(m1)>len(m2):
		query = m2
	else:
		query = m1
	query = query.lower()		
	a = []
	map1 = {}
	for s in query.split(' '):
		if s in map1.keys():
			map1[s] += 1
		else:
			map1[s] = 1
	for s in words:
		if s in map1.keys():
			a = a+[map1[s]]
		else:
			a = a+[0]
	test = np.multiply(a,idf).reshape(1,len(a))
	cosine = cosine_similarity(test,X)
	index_max = np.argmax(cosine)
	rw = 0
	with open(file_path,'r') as fp1:
		reader1 = json.load(fp1)
		for row1 in reader1:
			if rw == index_max:
				print('Ishika: '),
				print(row1["response"])
				break
			rw+=1
