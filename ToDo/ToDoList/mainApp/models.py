from django.db import models

# Create your models here.

class ToDo(models.Model):
	Title = models.CharField(max_length = 100, blank = False)
	Description = models.TextField()
	Image = models.ImageField(null = True, blank =	True)

	def __str__ (self):
		return self.Title