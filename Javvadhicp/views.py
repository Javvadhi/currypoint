from django.shortcuts import render
from .models import *

# Create your views here.
# def items(request):
# 	o=Menu.objects.all()
# 	return render(request,'items.html',{'o':o})


def Nv(request):
	q = NonVeg.objects.all()
	return render(request,'NonVeg.html',{'q':q})

def V(request):
	w = Veg.objects.all()
	q = NonVeg.objects.all()
	return render(request,'Veg.html',{'w':w,'q':q})	
