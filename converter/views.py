from django.shortcuts import render
from django.http import HttpResponse
import os
import tempfile
from PyPDF2 import PdfReader
from docx import Document


def to_pdf(request):
	title = "To PDF"
	
	context = {
		'title': title,
		
	}
	return render(request, 'converter/to_pdf.html', context)


def pdf_to_docx(pdf_path):
	pdf = PdfReader(pdf_path)
	doc = Document()
	
	for page in pdf.pages:
		text = page.extract_text()
		doc.add_paragraph(text)
	
	return doc


def to_docx(request):
	title = "To Docx"
	if request.method == 'POST' and request.FILES.get('pdf_file'):
		pdf_file = request.FILES['pdf_file']
		pdf_path = os.path.join(tempfile.gettempdir(), pdf_file.name)
		
		with open(pdf_path, 'wb') as f:
			for chunk in pdf_file.chunks():
				f.write(chunk)
		
		doc = pdf_to_docx(pdf_path)
		docx_path = os.path.splitext(pdf_path)[0] + '.docx'
		doc.save(docx_path)
		
		with open(docx_path, 'rb') as f:
			response = HttpResponse(f.read(), content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
			response['Content-Disposition'] = f'attachment; filename={os.path.basename(docx_path)}'
			return response
	
	context = {
		'title': title,
	}
	return render(request, 'converter/to_docx.html', context)