from django.db import models

# Create your models here.

class ToDo(models.Model):
	Title = models.CharField(max_length = 100, blank = False)
	Description = models.TextField()

	def __str__ (self):
		return self.Title