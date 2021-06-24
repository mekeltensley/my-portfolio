from django.db import models

# Create your models here.


class Project(models.Model):
	# Contains project title
	project_title = models.CharField(max_length=50)

	# Contains an image
	image = models.ImageField(upload_to='images/')

	# Contains a brief project description
	description = models.CharField(max_length=200)

	# In-depth summary for projects in portfolio
	summary = models.TextField(max_length=500)


	def __str__(self):
		portfolio = '{0.summary} {0.project_title}'
		return portfolio.format(self)
	# this allows returns the summary for a particular object
