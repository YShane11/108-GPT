from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/game')
def game():
    return render_template("game.html")

if __name__ == "__main__":
    app.run()
