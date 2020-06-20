#pip install pandas_datareader
#pip install jupyterlab
#pip install notebook

from flask import Flask, render_template

app=Flaske(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)