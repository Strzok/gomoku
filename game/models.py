from __future__ import unicode_literals

from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Coord_o(models.Model):
    """It keeps coordinates of computer move"""
    ip = models.GenericIPAddressField(primary_key=True)
    coord_ox = models.CharField(max_length=200, default=list)
    coord_oy = models.CharField(max_length=200, default=list)
class Coord_x(models.Model):
    """It keeps coordinates of player's move"""
    ip = models.GenericIPAddressField(primary_key=True)
    coord_xx = models.CharField(max_length=200, default=list)
    coord_xy = models.CharField(max_length=200, default=list)
class Difficulty_level(models.Model):
    """It keeps diffuculty level"""
    ip = models.GenericIPAddressField(primary_key=True)
    level_in_model = models.CharField(max_length=200, default=list)
class Size(models.Model):
    """It keeps size"""
    ip = models.GenericIPAddressField(primary_key=True)
    size_in_model = models.CharField(max_length=3, default=list)
