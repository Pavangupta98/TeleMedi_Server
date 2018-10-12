from django.shortcuts import render
from .models import Feedback
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def feedback_save(request):
	response_json = {}
	try:
		if request.method == "POST":
			
			name = request.POST.get("name")
			email = request.POST.get("email")
			phone = request.POST.get("phone")
			message = request.POST.get("message")

			obj = Feedback.objects.create(name=str(name), phone=str(phone), email=str(email), message=str(message))
			obj.save()

			response_json["success"] = True
			response_json["message"] = "Thank You for your Feedback. It was saved successfully."

		else:
			response_json["success"] = False
			response_json["message"] = "Some Error occured while saving."	    
	except Exception as e:

		print(e)
		msg = "Exception- " + str(e)

		response_json["success"]= False
		response_json["message"] = msg
	return JsonResponse(response_json)

