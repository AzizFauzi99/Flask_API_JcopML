from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    return 'Hai ini percobaan untuk POST request'

if __name__ == '__main__':
    app.run(debug=True)