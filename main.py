from flask import Flask, render_template, request
from prompt_function import Chatbot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    if request.method == 'POST':
        question = request.form['question']
        answer = get_answer(question)
    return render_template('index.html', answer=answer)

def get_answer(question):
    chatbot = Chatbot()
    answer = chatbot.run_qa(question)
    return answer

if __name__ == '__main__':
    app.run()
