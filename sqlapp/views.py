from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def insertpageview(request):
    return render(request, "sqlapp/insert.html")

def InsertData(request): #Data comes from insert.html to view
    fname=request.POST["fname"]
    lname = request.POST["lname"]
    email= request.POST["email"]
    contact= request.POST["contact"]

    # creating object of Model class -- Inserting data into table
    newuser= Student.objects.create(firstname=fname, lastname=lname, email=email, contact=contact)

    #after inserting data, show on show.html
    #return render(request,"sqlapp/show.html")
    return redirect ('show_data')

def FetchData(request):
    data = Student.objects.all()
    return render (request, "sqlapp/show.html", {'students': data })

def EditData(request,pk): #Fetching the data on ID
    get_data = Student.objects.get(id=pk)
    print('PK :', pk)
    return render (request, "sqlapp/edit.html", {'key1': get_data  })

def UpdateData(request,pk):
    udata= Student.objects.get(id=pk)
    udata.firstname = request.POST['fname']
    udata.lastname = request.POST['lname']
    udata.email=request.POST['email']
    udata.contact = request.POST['contact']
    udata.save()
    return redirect ('show_data')

def DeleteData(request, pk):
    ddata=Student.objects.get(id=pk)
    ddata.delete()
    return redirect('show_data')
