from django.http import HttpResponse

def index(request):
	return HttpResponse("Main page. We'll get Search, My Assets, and Uploads done here.")