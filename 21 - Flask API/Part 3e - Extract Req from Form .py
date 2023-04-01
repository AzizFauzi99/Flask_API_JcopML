from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("form.html")
    elif request.method == 'POST':
        # bisa pake .get atau langsung []
        print(request.form.get('name'))
        print(request.form['gender'])
        return 'Terima Kasih telah mengirimkan data'
    
if __name__ == '__main__':
    app.run(debug=True)