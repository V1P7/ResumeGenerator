from django.http import HttpResponse, FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render, redirect
from .forms import ResumeForm
import io

def index(request):
	title = "Main Page"
	
	context = {
		'title': title,
	}
	return render(request, 'accounts/index.html', context)


def create_resume(request):
	if request.method == 'POST':
		form = ResumeForm(request.POST, request.FILES)
		if form.is_valid():
			resume = form.save(commit = False)
			# Разделение полей, разделенных запятыми, на списки
			education_list = [edu.strip() for edu in resume.education.split(',')]
			languages_list = [lang.strip() for lang in resume.languages.split(',')]
			work_experience_list = [exp.strip() for exp in resume.work_experience.split(',')]
			hard_skills_list = [skill.strip() for skill in resume.hard_skills.split(',')]
			soft_skills_list = [skill.strip() for skill in resume.soft_skills.split(',')]
			# Присваивание списков обратно полям модели
			resume.education = education_list
			resume.languages = languages_list
			resume.work_experience = work_experience_list
			resume.hard_skills = hard_skills_list
			resume.soft_skills = soft_skills_list
			
			resume.save()
			return redirect('index')
	else:
		form = ResumeForm()
	
	context = {'form': form}
	return render(request, 'builder/create_resume.html', context)


def generate_pdf(request):
	if request.method == 'POST':
		form = ResumeForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			
			buffer = io.BytesIO()
			p = canvas.Canvas(buffer)
			
			y_coordinate = 750  # Начальная координата Y для текста
			
			p.drawString(100, y_coordinate, f"Name: {data['first_name']} {data['last_name']}")
			y_coordinate -= 20
			
			p.drawString(100, y_coordinate, f"Number: {data['phone_number']}")
			y_coordinate -= 20
			
			p.drawString(100, y_coordinate, f"Email: {data['email']}")
			y_coordinate -= 20
			
			p.drawString(100, y_coordinate, f"City: {data['city']}")
			y_coordinate -= 20
			
			p.drawString(100, y_coordinate, f"Date of birth: {data['date_of_birth']}")
			y_coordinate -= 20
			
			p.showPage()
			p.save()
			
			buffer.seek(0)
			response = FileResponse(buffer, content_type = 'application/pdf')
			response['Content-Disposition'] = f'attachment; filename="{data["first_name"]}_{data["last_name"]}_resume.pdf"'
			
			return response
	else:
		form = ResumeForm()
		
		context = {'form': form}
		return render(request, 'builder/resume_form.html', context)
			
		
