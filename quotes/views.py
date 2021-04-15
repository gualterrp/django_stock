from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

# pk_87aefe071fea4dea86ad14a2dbc4ee1a 

# 'https://br.financas.yahoo.com/quote/GGBR4.SA' endpoint do google finance com a Gerdau

def home(request):
	import requests
	import json

	# confere se o formulário foi submetido
	if request.method == "POST":
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_87aefe071fea4dea86ad14a2dbc4ee1a")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error ..."
		return render(request, 'home.html', {'api': api})

	else:
		# se o formulário não tiver sido submetido, envia a mensagem na variável 'msgblank para a página 'home.html'
		return render(request, 'home.html', {'msgblank': 'Enter a Ticker Symbol on Form.'})

	
	

def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	import requests
	import json
	# confere se o formulário foi submetido
	if request.method == "POST":
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been Added to database!"))
			return redirect('add_stock')
	else:

		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_87aefe071fea4dea86ad14a2dbc4ee1a")
		
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error ..."

		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock has been Deleted from database!"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker': ticker})

