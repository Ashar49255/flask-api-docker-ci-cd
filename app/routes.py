from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')  # Renders home.html file from templates folder


if __name__ == '__main__':
    app.run(debug=True)
