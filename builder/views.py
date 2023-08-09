from django.shortcuts import render, redirect
from .forms import ResumeForm


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
		
