import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("upload.html")
    elif request.method == 'POST':
        csv_file = request.files.get('file')
        X_test = pd.read_csv(csv_file, index_col='PassengerId')
        return X_test.to_html()
    
if __name__ == '__main__':
    app.run(debug=True)