import os
import re
from flask import Flask, request , json ,render_template, send_from_directory
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return render_template("index.html")


''''
Ask @umang dubey to implement this page.
Basically a hotstocks.html page needs to be designed that will be put inside templages folder.
'''
@app.route('/hotstocks')
def hotStocks():
    return render_template("hotstocks.html")

# The flows below is a static web page and can be easily picked up.
@app.route('/optimizers')
def optimizers():
    return render_template("optimizers.html")

@app.route('/report')
def report():
    return render_template("report.html",report="oldreport.pdf")

@app.route('/signUp')
def signUp():
    return "Not a part of current project.To be done."


@app.route('/optimize', methods=['POST'])
def process_json():
    
    content_type = request.headers.get('Content-Type')
    print(content_type)

    data  = request.form
    # print(data["tickers"])
    # print(data["amount"])

    amt = int(data["amount"])
    tic = list(data["tickers"].split(','))

    print(amt)
    print(tic)

    # get these after rendering and storing in assets
    _chart_markowitz = "piechart.png"
    _chart_rpp = "piechart.png"
    _chart_hrp = "piechart.png"

    _barchart_expectedreturns = "barchart.png"
    _barchart_changedvariance = "barchart.png"
    _barchart_sharpratio = "barchart.png"

    # https://stackoverflow.com/questions/53202636/render-dynamically-changing-images-with-same-filenames-in-flask
    return render_template(
    "optimized_portfolio.html",
    chart_markowitz=_chart_markowitz,
    chart_rpp=_chart_rpp,
    chart_hrp=_chart_hrp,
    barchart_expectedreturns=_barchart_expectedreturns,
    barchart_changedvariance=_barchart_changedvariance,
    barchart_sharpratio=_barchart_sharpratio
    )

    

if __name__ == "__main__":
    app.run()