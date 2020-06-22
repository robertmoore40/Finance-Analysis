#pip install pandas_datareader
#pip install jupyterlab
#pip install notebook

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('plot')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start=datetime.datetime(2020,1,1)
    end=datetime.datetime(2020,5,1)

    df=data.DataReader(name="GOOG", data_source='google', start=start,end=end)

    def inc_dec(c,o):
        if c > o:
            value="Increase"
        elif c < o:
            value="Decrease"
        else:
            value="Equal"
        return value



if __name__=="__main__":
    app.run(debug=True)