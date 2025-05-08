from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session to work

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 20)
        session['tries'] = 0

    message = ""
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['tries'] += 1
            number = session['number']

            if guess < number:
                message = "Too low! Try again."
            elif guess > number:
                message = "Too high! Try again."
            else:
                message = f"🎉 Correct! You guessed it in {session['tries']} tries."
                session.pop('number')  # Reset game
                session.pop('tries')
        except ValueError:
            message = "Please enter a valid number."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
