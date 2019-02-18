from django.shortcuts import render
from coins.models import coins
import urllib.request, urllib.parse, urllib.error
import json

def post_list(request):
    return render(request, 'coins/coins_list.html', {})
def bitcoin(request):
	data =fetchDetails('bitcoin')
	if flag == 1:
		return render(request, 'coinsDetails/error.html',{})
	return render(request, 'coinsDetails/details.html',{'data':data,'flag':flag})

def ethereum(request):
	data =fetchDetails('ethereum')
	if flag == 1:
		return render(request, 'coinsDetails/error.html',{})
	return render(request, 'coinsDetails/details.html', {'data':data,'flag':flag})

def litecoin(request):
	data =fetchDetails('litecoin')
	if flag == 1:
		return render(request, 'coinsDetails/error.html',{})
	return render(request, 'coinsDetails/details.html', {'data':data,'flag':flag})

def fetchDetails(n):
	serviceurl = "https://api.coingecko.com/api/v3/coins/markets?"
	curr = "inr"
	address = n
	global flag
	params = dict()
	params["vs_currency"]= curr
	params["ids"] = address
	url = serviceurl + urllib.parse.urlencode(params)
	uh = None
	data = None
	try:
		uh = urllib.request.urlopen(url)
		data = uh.read().decode()
		js = json.loads(data)
	except:
		js = None
	data = dict()
	if js is None:
		if coins.objects.filter(id=n).exists():
			coin = coins.objects.get(id=n)
			flag = 0
			return coin
		else:
			flag = 1		
	else:	
		data = js[0]
		flag = 2
		if coins.objects.filter(id=data['id']).exists():
			coins.objects.filter(id=data['id']).delete()
		coin = coins.objects.create(
			id = data['id'],
			name = data['name'],
			symbol = data['symbol'],
			image = data['image'],
			current_price = data['current_price'],
			market_cap =  data['market_cap'],
			market_cap_rank = data['market_cap_rank'],
			total_volume = data['total_volume'],
			high_24h = data['high_24h'],
			low_24h = data['low_24h'],
			price_change_24h = data['price_change_24h'],
			price_change_percentage_24h = data['price_change_percentage_24h'],
			market_cap_change_24h = data['market_cap_change_24h'],
			market_cap_change_percentage_24h = data['market_cap_change_percentage_24h'],
			circulating_supply = data['circulating_supply'],
			total_supply = data['total_supply'],
			ath = data['ath'],
			ath_change_percentage = data['ath_change_percentage'],
			ath_date = data['ath_date'])
		coin.save()
		coin = coins.objects.get(id=n)
		return coin