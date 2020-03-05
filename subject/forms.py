from django import forms
from .models import *


class subjectForm(forms.ModelForm):
	class Meta:
		model = subject
		fields = ('id','course_name')