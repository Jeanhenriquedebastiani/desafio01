from flask import Flask, render_template

app = Flask(__name__)

@app.route("/curriculo")
def ola():
    return render_template('curriculo.html')


app.run(debug=True)