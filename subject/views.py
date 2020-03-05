from django.shortcuts import render
from .models import subject

# Create your views here.
def home(request):
	x = subject.objects.all()
	print(x)

	return render(request,'home.html',{'x':'x'})
