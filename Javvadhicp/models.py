from django.db import models

# Create your models here.
# class Menu(models.Model):
# 	Nonveg = models.CharField(max_length=30)
# 	Veg = models.CharField(max_length=30)
# 	pickles = models.CharField(max_length=35)
# 	price = models.CharField(max_length=5, default="")
class NonVeg(models.Model):
	item = models.CharField(max_length=20)
	quantity = models.CharField(max_length=5)
	price = models.CharField(max_length=5)

	def __str__(self):
		return self.item +'-'+ self.price


class Veg(models.Model):
	item = models.CharField(max_length=20)
	quantity = models.CharField(max_length=5)
	price = models.CharField(max_length=5)



