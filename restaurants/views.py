from django.shortcuts import render



# Create your views here.
def myviews(request):

	context = {

		'msg': 'Hello World!',
	}
	return render(request, "first.html", context)