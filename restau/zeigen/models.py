# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Essen(models.Model):
	"""docstring for Essen"""
	name = models.CharField(max_length=30)
	preis = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return self.name

class Reservation(models.Model):
	vorname = models.CharField(max_length=10)
	nachname= models.CharField(max_length=10)
	telnu   = models.CharField(max_length=11)
	gastnu  = models.CharField(max_length=3)
	email   = models.EmailField(max_length=254)
	re_date = models.DateTimeField()

	def __str__(self):
		return self.vorname