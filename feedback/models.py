from django.db import models

class Feedback(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	email = models.CharField(max_length=30, blank=False, null=False)
	phone = models.CharField(max_length=15, blank=True, null=True)
	message = models.TextField(max_length=1000, blank=True, null=True)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.email

	def __unicode__(self):
		return self.email
