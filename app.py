from flask import Flask, render_template, request, redirect, url_for, flash, jsonify,session


app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json(force=True)
        print(data)
        return jsonify({'result': 'success'})
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)