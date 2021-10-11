from django.shortcuts import render,redirect
from .models import *
from django.views.generic import ListView
# Create your views here.

def homepage(request):
	return render(request,'index.html')

def contactus(request):
	return render(request,'contactus.html')

def LogIn(request):
	return render(request,'login.html')

def CheckLogin(request):
	emailhere = request.GET['getEmail']
	passwordhere = request.GET['getPassword']

	data = UserDetailsModel.objects.all()
	for d in data:
		if d.Email==emailhere and d.Password==passwordhere:
			return render(request,'index.html')
	return render(request,'register.html')


def Register(request):
	return render(request,'register.html')

def RegNewUser(request):
	data = UserDetailsModel(First_Name = request.GET['UserFname'], Last_Name = request.GET['UserLname'], Email = request.GET['UserEmail'], Password = request.GET['UserPassword'], Contact_Number = request.GET['UserContact'], Address = request.GET['UserAddress'], Landmark = request.GET['UserLandmark'], City = request.GET['UserCity'], State = request.GET['UserState'], Zip = request.GET['UserZip'])
	data.save()
	data=UserDetailsModel.objects.all()
	return render(request,'login.html')

def home(request):
	return render(request,'index.html')

def CBSE(request):
	return render(request,'cbse.html')

def GSEB(request):
	return render(request,'gseb.html')

class CBSES1(ListView):
	model = BookDetailsModel
	template_name = 'cbses1.html'

def CBSES2(request):
	return render(request,'cbses2.html')

def CBSES3(request):
	return render(request,'cbses3.html')

def CBSES4(request):
	return render(request,'cbses4.html')

def CBSES5(request):
	return render(request,'cbses5.html')

def CBSES6(request):
	return render(request,'cbses6.html')

def CBSES7(request):
	return render(request,'cbses7.html')

def CBSES8(request):
	return render(request,'cbses8.html')

def CBSES9(request):
	return render(request,'cbses9.html')

def CBSES10(request):
	return render(request,'cbses10.html')

def Brush(request):
	return render(request,'brush.html')

def Color(request):
	return render(request,'color.html')

def Sketchbook(request):
	return render(request,'sketchbook.html')

def Singleline(request):
	return render(request,'singleline.html')