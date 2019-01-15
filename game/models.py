from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Coord_o(models.Model):
	ip = models.GenericIPAddressField(primary_key=True)
	coord_ox = models.CharField(max_length=200)
	coord_oy = models.CharField(max_length=200)
class Coord_x(models.Model):
	ip = models.GenericIPAddressField(primary_key=True)
	coord_xx = models.CharField(max_length=200)
	coord_xy = models.CharField(max_length=200)
class Difficulty_level(models.Model):
	ip = models.GenericIPAddressField(primary_key=True)
	level_in_model = models.CharField(max_length=200)	
