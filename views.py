from ast import If
from email import message
from django.shortcuts import render

from CRUD_operation.models import main_clientsModel
from django.contrib import messages
from CRUD_operation.forms import client_form

def showClients(request):
    showall= main_clientsModel.objects.all()
    return render(request, 'index.html', {"data":showall})

def insertData(request):
    if request.method=="POST":
     if request.POST.get('client_id') and request.POST.get('client_name') and request.POST.get('client_county') and request.POST.get('client_age'):
        saverecord = main_clientsModel()
     saverecord.client_id = request.POST.get('client_id')
     saverecord.client_name = request.POST.get('client_name')
     saverecord.client_county = request.POST.get('client_county')
     saverecord.client_age = request.POST.get('client_age')

     saverecord.save()
     messages.success(request, 'Client' +" "+saverecord.client_name+ " "+ 'successfully saved')
     return render(request, 'insert.html')


    else:

     return render(request, 'insert.html')


def editData(request, client_id):
    editObj=main_clientsModel.objects.get(client_id=client_id)
    return render(request, 'Edit.html', {"main_clientsModel":editObj})

def updateClt(request, client_id):
    updateEach=main_clientsModel.objects.get(client_id=client_id)
    form=client_form(request.POST, instance=updateEach)
    if form.is_valid():
        form.save() 
    messages.success(request, "records saved successfuly")
    return render(request, 'Edit.html', {"main_clientsModel":updateEach})
     #return render(request, 'Edit.html', {"main_clientsModel":updateEach}) 

def delClt(request, client_id):
    delObj=main_clientsModel.objects.get(client_id=client_id)
    delObj.delete()

    show_all =main_clientsModel.objects.all()
    return render(request, 'Edit.html', {"main_clientsModel":delObj} )