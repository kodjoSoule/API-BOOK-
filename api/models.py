from django.db import models

class Menu(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	description = models.TextField(blank=True)

	class Meta:
		app_label = 'api'

	def __str__(self):
		return self.name
