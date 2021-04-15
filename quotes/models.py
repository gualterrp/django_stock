from django.db import models

# Create your models here.
class Stock(models.Model):
	"""docstring for Stock"""
	ticker = models.CharField(max_length=12)

	def __str__(self):
		return self.ticker