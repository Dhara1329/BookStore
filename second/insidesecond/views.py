from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

context =[{'name':'Dhara','places':['Coorg','Ooty'],'city':'Ahmedabad','contact' : 1234567890},
		  {'name':'Prapti','places':['Ahmedabad','GOA'],'city':'Ahmedabad','contact' : 3216549870},
		  {'name':'Preshita','places':['Banglore','Pune'],'city':'Ahmedabad','contact' : 4561237890}
		  ]


def homepage(Request):
	return render(Request,"home.html",context[2])
	
def MyMusic(Request):
	return render(Request,'music.html')

def MyMovie(Request):
	return render(Request,"movie.html")

def MyPlace(Request):
	return render(Request,"place.html",context[1])

def MyBooks(Request):
	return render(Request,"book.html")
	
def MyHobbies(Request):
	return render(Request,"hobby.html")

def MyFriends(Request):
	return render(Request,"friends.html")