from flask import Flask
from flask import render_template, request, redirect

app=Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def magic_ball():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True) 