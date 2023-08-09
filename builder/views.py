from django.shortcuts import render


def index(request):
	title = "Main Page"
	
	context = {
		'title': title,
	}
	return render(request, 'accounts/index.html', context)
