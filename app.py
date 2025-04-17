from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'guess_secret_key'

@app.route('/')
def index():
    session['number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['guess'])
    number = session.get('number', random.randint(1, 100))

    if user_guess < number:
        return jsonify({'message': 'Too low! Try again.'})
    elif user_guess > number:
        return jsonify({'message': 'Too high! Try again.'})
    else:
        return jsonify({'message': f'Correct! The number was {number}. Starting a new game...', 'correct': True})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
