import PyPDF2
from django.http import HttpResponse
from django.shortcuts import render
from io import BytesIO


def add_password(request):
	title = "Add password"
	if request.method == 'POST':
	
		pdf_file = request.FILES['pdf_file']
		password = request.POST['password']
		
		pdf_in = PyPDF2.PdfReader(pdf_file)
		pdf_file = PyPDF2.PdfWriter()
		
		for page in pdf_in.pages:
			pdf_file.add_page(page)
		
		pdf_file.encrypt(password)
		
		pdf_output = BytesIO()
		pdf_file.write(pdf_output)
		# with open('encrypted.pdf', 'wb') as f:
		# 	pdf_file.write(f)
		response = HttpResponse(pdf_output.getvalue(), content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename='"encrypted.pdf"
		return response
	
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

