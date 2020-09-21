from flask import Flask, render_template, request, redirect, Markup

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bohken_plot import get_plot

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')
  
@app.route('/graph')
def graph():
	symbol = request.args['ticker']
	plot = get_plot(symbol)
	return Markup(file_html(plot, CDN, "my plot"))

if __name__ == '__main__':
  app.run(port=33507, debug=True)