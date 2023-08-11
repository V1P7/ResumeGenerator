from django.shortcuts import render


def to_pdf(request):
	title = "To PDF"
	
	context = {
		'title': title,
	}
	return render(request, 'converter/to_pdf.html', context)


def to_docx(request):
	title = "To Docx"
	
	context = {
		'title': title,
	}
	return render(request, 'converter/to_docx.html', context)