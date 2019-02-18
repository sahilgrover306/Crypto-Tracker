from django.db import models


class coins(models.Model):
	id = models.CharField(primary_key=True,max_length=50)
	name = models.CharField(max_length=50)
	symbol = models.CharField(max_length=50)
	image = models.CharField(max_length=500)
	current_price = models.FloatField()
	market_cap =  models.FloatField()
	market_cap_rank = models.IntegerField()
	total_volume = models.FloatField()
	high_24h = models.FloatField()
	low_24h = models.FloatField()
	price_change_24h = models.FloatField()
	price_change_percentage_24h = models.FloatField()
	market_cap_change_24h = models.FloatField()
	market_cap_change_percentage_24h = models.FloatField()
	circulating_supply = models.FloatField()
	total_supply = models.BigIntegerField()
	ath = models.FloatField()
	ath_change_percentage = models.FloatField()
	ath_date = models.DateTimeField()
	last_updated = models.DateTimeField(auto_now_add=True)

