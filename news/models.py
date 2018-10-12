from django.db import models

class News(models.Model):
	headline = models.CharField(max_length=500, blank=True, null=True)
	news_image = models.ImageField(upload_to="news/news_image", blank=True, null=True)
	news_para = models.TextField(max_length=3000, blank=True, null=True)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.headline

	def __unicode__(self):
		return self.headline