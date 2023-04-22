from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   data = {
      'title':'Home Page',
      "welcome": 'Welcome to home page',
      'clist':["django", 'CPP', 'PHP'],
      'friends_details':[
      {'name':"Ashfaq", 'profession':"Student", 'residence':"Finland", 'phone':+152255885448},
      {'name':"Mutafaf", 'profession':"IT Company", 'residence':"Pakistan", 'phone':+923125474458}
      ]
   }
   return render(request, "index.html",data)


def aboutUs(request):
   return HttpResponse("this is view in mysite app")

def portfolio(request):
   return HttpResponse("this is portfolio in mysite app")

def contactUs(request):
   return HttpResponse("this is contact us page")

def courseDetails(request, courseid):
   return HttpResponse("Hello, you are on page "+courseid)