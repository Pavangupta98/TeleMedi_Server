from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
	list_display = ["headline", "news_image", "news_para", "created", "modified"]
	search_fields = ["headline", "news_image", "created", "modified"]

admin.site.register(News, NewsAdmin)

