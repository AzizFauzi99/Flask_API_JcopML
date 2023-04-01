from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # print(request.args['nama'])
    print(request.args.get('nama'))
    return "Terima Kasih"

if __name__ == '__main__':
    app.run(debug=True)