from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    education = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1Education degree, 2Education degree..'}))
    languages = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1Language level, 2Language level..'}))
    work_experience = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '1Job experience, 2Job experience..'}))
    hard_skills = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '1Skill, 2Skill..'}))
    soft_skills = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '1Skill, 2Skill..'}))

    class Meta:
        model = Resume
        fields = '__all__'

        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+380-123-456-789'}),
            'motivation_letter': forms.Textarea(attrs={'class': 'form-control'}),
        }