# Chatbot-Application
Project for Chatbot Application in Python using concepts of NLP.

A computer program is designed to have a conversation using chatbot which is a conversational agent. The user can give input in the form of text.The project is created using the python language. In this project we used python libraries such as numpy, tkinter, pickle,etc. Numpy is used for numerical calculation, tkinter for GUI, pickle for storing the pre computed data.

The basic concepts of NLP are used for normalizing the text, converting the text to feature, text matching for comparing two messages.
The input given by the user is compared with all the available messages using cosine similarity. If the maximum similarity is greater than equal to 70% then then the output response is chosen randomly from all the messages with similarity having error less than equal to 1% from the maximum similarity.

The messages are first converted into tf-idf vectors and then the input given by user is also converted into tf-idf vector and then cosine similarity between them is calculated for comparison purpose. Cosine similarity is cosine of the angle between this two vectors.
The model is having 89% accuracy on the given data set.
