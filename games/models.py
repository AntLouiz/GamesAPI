from django.db import models

# Create your models here.
class Game(models.Model):
	"""docstring for Game"""
	def __init__(self, arg):
		super(Game, self).__init__()
		self.arg = arg
		