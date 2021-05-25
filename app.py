from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv_1_c1')
def cv_1_c1():
    return render_template('cv_1_c1.html')

@app.route('/cv_1_c2')
def cv_1_c2():
    return render_template('cv_1_c2.html')

@app.route('/cv_1_c3')
def cv_1_c3():
    return render_template('cv_1_c3.html')

@app.route('/intro_ia')
def intro_ia():
    return render_template('intro_ia.html')


@app.route('/ia_c1')
def ia_c1():
    return render_template('ia_c1.html')

@app.route('/ia_c2')
def ia_c2():
    return render_template('ia_c2.html')

@app.route('/ia_c3')
def ia_c3():
    return render_template('ia_c3.html')


if __name__ == "__main__":

    app.run(debug=True)