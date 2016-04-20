from django.shortcuts import render

# Create your views here.
def adminsite(request):
	return HttpResponse("This is admin")