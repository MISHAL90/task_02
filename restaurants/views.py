from django.shortcuts import render
from restaurants import templates 

# Create your views here.
def task_02 (request):
	context= {
	 	  'msg' : "Hello World!" ,



	}
	return render(request, 'index.html', context)
