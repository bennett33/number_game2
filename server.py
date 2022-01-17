from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    guess = ""
    if "rand" not in session:
        session["rand"] = random.randint(1,100)
    if "guess" in session:
        guess = int(session["guess"])
    return render_template("index.html", guess=guess)

@app.route("/guess", methods=["POST"])
def guess():
    session["guess"] = request.form["guess"]
    print(request.form) 
    return redirect("/")

@app.route('/reset', methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

