from flask import Flask,render_template,request
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')
conv = open('chats.txt','r').readlines()
bot.set_trainer(ListTrainer)
bot.train(conv)
app = Flask(__name__)
@app.route('/handle_data', methods=['POST'])
def handle_data():
    query = request.form['user']
    response = bot.get_response(query)
    return str(response)
@app.route("/")
def main():
    return render_template('page.html')
if __name__ == "__main__":
    app.run()
