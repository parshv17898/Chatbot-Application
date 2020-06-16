from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from Tkinter import *
import pickle
import numpy as np
import json
import re
import random

lem = WordNetLemmatizer()
file_path = "/home/apurv/Downloads/chatbot/previous_chats.json"
with open("idf.txt",'rb') as fp:
	idf = pickle.load(fp)
with open("words.txt",'rb') as fp:
	words = pickle.load(fp)
with open("datasetx.txt",'rb') as fp:
	X = pickle.load(fp)
	X = np.array(X)

def query(query):
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
	max = np.max(cosine)
        if max<0.7:
		return "Sorry, I did not understand what you said"
	max = max-0.01
	list = np.where(cosine > max)
        index_max = random.choice(list[1])
	#index_max = np.argmax(cosine)
	rw = 0
	with open(file_path,'r') as fp1:
		reader1 = json.load(fp1)
		for row1 in reader1:
			if rw == index_max:
				return row1["response"]
				break
			rw+=1
	return ""
def ClickAction():
    message = EntryBox.get("0.0",END)
    response = query(message)
    LoadMyEntry(message,"You")
    LoadMyEntry(response,"Ishika")
    ChatLog.yview(END)
    EntryBox.delete("0.0",END)

def PressAction(event):
	EntryBox.config(state=NORMAL)
	ClickAction()

def DisableEntry(event):
	EntryBox.config(state=DISABLED)

def LoadMyEntry(message,tag):
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            LineNumber = float(ChatLog.index('end'))-1.0
            ChatLog.insert(END, tag+": " + message)
	    ChatLog.tag_add(tag, LineNumber, LineNumber+float(len(tag)+1)/10)
	    if tag == "Ishika":
		ChatLog.insert(END,"\n")
	    	ChatLog.tag_config(tag, foreground="green", font=("Arial", 12, "bold"))
	    else:
	    	ChatLog.tag_config(tag, foreground="orange", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
	    ChatLog.yview(END)

base = Tk()
base.title("Chatbot")
base.geometry("500x550")
base.resizable(width=FALSE, height=FALSE)

ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.insert(END, "Hey! Welcome to the chatbot\n")
ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

SendButton = Button(base, font=30, text="Send", width="12", height=5,
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",
                    command=ClickAction)

EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox.bind("<Return>", DisableEntry)
EntryBox.bind("<KeyRelease-Return>", PressAction)
scrollbar.place(x=490,y=6, height=486)
ChatLog.place(x=6,y=6, height=486, width=480)
EntryBox.place(x=6, y=501, height=45, width=387)
SendButton.place(x=390, y=501, height=45,width=80)
base.mainloop()
