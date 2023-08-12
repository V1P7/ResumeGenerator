from django.db import models


class Resume(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length = 20)
	email = models.EmailField()
	city = models.CharField(max_length = 200)
	social = models.CharField(max_length = 200, blank = True)
	date_of_birth = models.DateField()
	photo = models.ImageField(upload_to = 'photos/', blank = True)
	education = models.CharField(max_length=300)
	languages = models.CharField(max_length =200)
	work_experience = models.TextField()
	hard_skills = models.TextField()
	soft_skills = models.TextField()
	motivation_letter = models.TextField()