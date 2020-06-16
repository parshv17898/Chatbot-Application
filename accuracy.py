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
with open(file_path,'r') as message:
		reader = json.load(message)
		for row in reader:
			m = re.sub('\W+',' ', row["message"])
			m1 = lem.lemmatize(m,'v')
			m2 = lem.lemmatize(m,'n')
			if len(m1)>len(m2):
				m = m2
			else:
				m = m1
			query = m
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
			if j == index_max:
				accuracy+=1
			j+=1
			if j%50 == 0:
				print(j)
print(float(accuracy)/j)
