import simplejson as json
import pandas as pd
import requests

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

# creates the plots based off ticker symbol and dictionary for various checks
def get_plot(symbol):
	# outputs plot from input of symbol and check_list of various
	# gets data
	parameters = {"symbol": symbol, "function": 'TIME_SERIES_DAILY', "apikey": 'PFXXZOUQ3XAXKMVT', "datatype": 'json'}
	response = requests.get("https://www.alphavantage.co/query?", params=parameters)
	text = json.dumps(response.json()['Time Series (Daily)'], sort_keys=True, indent=4)
	df = pd.read_json(text,orient='index')
	df = df.loc['2020-07-01':'2020-08-01']
	# creates graph
	p1 = figure(x_axis_type="datetime", title="Daily Stock Prices for "+symbol)
	p1.grid.grid_line_alpha=0.3
	p1.xaxis.axis_label = 'Date'
	p1.yaxis.axis_label = 'Price'
	p1.line(df.index, df['1. open'], color='#A6CEE3', legend_label='Opening Price')
	p1.line(df.index, df['4. close'], color='#FB9A99', legend_label='Closing Price')
	p1.legend.location = "top_left"
	return p1
	
	
	