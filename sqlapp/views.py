from django.shortcuts import render
from .models import *
# Create your views here.
def insertpageview(request):
    return render(request, "sqlapp/insert.html")

def InsertData(request): #Data comes from html to view
    fname=request.POST["fname"]
    lname = request.POST["lname"]
    email= request.POST["email"]
    contact= request.POST["contact"]

    # creating object of Model class -- Inserting data into table
    newuser= Student.objects.create(firstname=fname, lastname=lname, email=email, contact=contact)

    #after inserting data show on show.html
    return render(request,"sqlapp/show.html")

def FetchData(request):
    data = Student.objects.all()
    return render (request, "sqlapp/show.html", {'students': data })
