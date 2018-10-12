from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ["name", "email", "phone", "created", "modified"]
	search_fields = ["name", "email", "phone", "created", "modified"]

admin.site.register(Feedback, FeedbackAdmin)