from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse("My first DJango homepage")
	
def about(request):
	return HttpResponse("About Us page")
	
def contact(request):
	return HttpResponse("Contact Us page")