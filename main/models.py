from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Company(models.Model):
	company_name = models.CharField(max_length=50)
	ticker = models.CharField(max_length=10)

	def __str__(self):
		return str(self.company_name)

class Investments(models.Model):
	investor = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.FloatField()
	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.company)+" - "+str(self.amount)
	