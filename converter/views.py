import io
from django.shortcuts import render
from django.http import HttpResponse
import os
import tempfile
from PyPDF2 import PdfReader
import docx
from docx import Document
from docx.shared import Inches
import pypdf
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas


def docx_to_pdf(docx_path):
	pdf_path = os.path.splitext(docx_path)[0] + '.pdf'
	
	c = canvas.Canvas(pdf_path, pagesize = landscape(letter))
	c.drawString(100, 750, "Converted from DOCX to PDF")
	c.showPage()
	c.save()
	
	return pdf_path


def to_pdf(request):
	title = "To PDF"
	if request.method == 'POST' and request.FILES.get('docx_file'):
		docx_file = request.FILES['docx_file']
		docx_path = os.path.join(tempfile.gettempdir(), docx_file.name)
		with open(docx_path, 'wb') as f:
			for chunk in docx_file.chunks():
				f.write(chunk)
		
		pdf_path = docx_to_pdf(docx_path)
		
		with open(pdf_path, 'rb') as pdf_file:
			response = HttpResponse(pdf_file, content_type = 'application/pdf')
			response['Content-Disposition'] = f'attachment; filename={os.path.basename(pdf_path)}'
			f.close()
			return response
	
	context = {
		'title': title
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