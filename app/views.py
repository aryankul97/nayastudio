from django.shortcuts import render
from app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def index(request):
	return render(request,'index.html',{})
def detail(request):
	return render(request,'detailform.html',{})
@csrf_exempt
def getdetail(request):
	if request.method=="POST":
		n=request.POST.get('name')
		e=request.POST.get('email')
		obj=detailformdata(
			Name=n,
			Email=e
			)
		obj.save()
		return HttpResponse("<h1>SAVED</h1>")