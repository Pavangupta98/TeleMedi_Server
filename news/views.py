from django.shortcuts import render
from .models import News
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def news_feed(request):
	response_json={}
	try:
		
		if request.method=="GET":
			news_query = News.objects.all()
			news_list = []
			for news in news_query:
				news_json = {
					"headline": news.headline,
					"image": request.scheme + "://" + request.get_host() + '/media/' + str(news.news_image),
					"news_para": news.news_para
				}
				news_list.append(news_json)
			response_json["news_list"] = news_list
			response_json["success"] = True
			response_json["message"] = "News List Fetched"
		else:
			response_json["success"] = False
			response_json["message"] = "Some error occurred while fetching"

	except Exception as e:
		print(e)
		msg = "Exception- " + str(e)
		response_json["success"] = False
		response_json["message"] = msg

	return JsonResponse(response_json)

