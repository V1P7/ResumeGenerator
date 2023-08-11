from django.urls import path
from . import views

urlpatterns = [
    path('to_pdf/', views.to_pdf, name= 'to_pdf'),
	path('to_docx/', views.to_docx, name= 'to_docx'),
]