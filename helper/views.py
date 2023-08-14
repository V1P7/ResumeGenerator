from django.shortcuts import render


def add_password(request):
	title = "Add password"
	
	context = {
		'title': title,
	}
	return render(request, 'helper/add_password.html', context)


def delete_metadata(request):
	title = "Delete Metadata"
	
	context = {
		'title': title,
	}
	return render(request, 'helper/delete_metadata.html', context)


def add_signature(request):
	title = "Add Signature"
	
	context = {
		'title': title,
	}
	return render(request, 'helper/add_signature.html', context)


def optimize_file(request):
	title = "Optimize File"
	
	context = {
		'title': title,
	}
	return render(request, 'helper/optimize_file.html', context)

