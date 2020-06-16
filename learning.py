from nltk.stem.wordnet import WordNetLemmatizer 
import numpy as np
import json
import pickle
import re
lem = WordNetLemmatizer()
def create_dataset(file_path):
	rows = 0
	columns = 0
	words = set([])
	with open(file_path,'r') as message:
		reader = json.load(message)
		for row in reader:
			rows+=1
			m = re.sub('\W+',' ', row["message"])
			m1 = lem.lemmatize(m,'v')
			m2 = lem.lemmatize(m,'n')
			if len(m1)>len(m2):
				m = m2
			else:
				m = m1
			m = m.lower()
			for s in m.split(' '):
				words.add(s)
        words = list(words)
	columns = len(words)	
	tf = []
	idf = []
	count = {}
	num = 0
	with open(file_path,'r') as message:
		reader = json.load(message)
		for row in reader:
			num+=1
			a = []
			map1 = {}
			m = re.sub('\W+',' ', row["message"])
			m1 = lem.lemmatize(m,'v')
			m2 = lem.lemmatize(m,'n')
			if len(m1)>len(m2):
				m = m2
			else:
				m = m1
			m = m.lower()
			for s in m.split(' '):
				if s in map1.keys():
					map1[s] += 1
				else:
					map1[s] = 1
				if s in count.keys():
					count[s] += 1
				else:
					count[s] = 1
			for s in words:
				if s in map1.keys():
					a = a+[map1[s]]
				else:
					a = a+[0]
			tf = tf+[a]
			if num%50 == 0:
				print(num)
	with open("words.txt",'wb') as fp:
		pickle.dump(words,fp)
	for s in words:
		idf = idf+[count[s]]
	idf = np.array(idf)
	idf = 1./idf
	idf = rows*idf
	idf = np.log10(idf)
	idf = np.array(idf.tolist())
	with open("idf.txt",'wb') as fp:
		pickle.dump(idf,fp)
	j = 0
	y = []
	while j<rows:
		tf[j] = np.multiply(tf[j],idf).tolist()
		j+=1
		y = y+[[j]]
	w = tf
	with open("datasetx.txt",'wb') as fp:
		pickle.dump(w,fp)
	with open("datasety.txt",'wb') as fp:
		pickle.dump(y,fp)
file_path = "/home/apurv/Downloads/chatbot/previous_chats.json"
create_dataset(file_path)
