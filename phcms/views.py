
from django import shortcuts
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from phcms.models import Department, Clinician, Patient




def laptop(reqest):
    return render(reqest, "laptops.html")

#request -> user request
#HttpResponse - is a module used to display some content on the UI.

def mobile(request):
    return render(request, "mobiles.html")

def home(request):
    return render(request, "home.html")

@csrf_exempt
def addDepartment(request):
    department = Department()
    if request.method == "POST":
        department.addDepartment(request.POST["deptname"], request.POST["deptcontact"], request.POST["deptdetails"])
    return render(request, "department.html")

@csrf_exempt
def getdepartment(request):
    #create a department object
    department = Department()
    #call getdepartment from the object and store in department variables
    departments = department.getdepartment(0)
    #render havind 3 params request,url,data (data is dictionary)
    return render(request, "departmentlist.html", {"departments": departments})


@csrf_exempt
def saveClinician(request):
    clinician = Clinician()
    if request.method == "POST":
        clinician.saveClinician(request.POST["clinicianname"], request.POST["deptid"], request.POST["cliniciancontact"], request.POST["cliniciandetails"])

    return render(request, "addclinician.html")

@csrf_exempt
def getClinician(request):
    clinician = Clinician()
    clinicians = clinician.getClinician(0)
    return render(request, "clinician.html", {"clinicians": clinicians})


@csrf_exempt
def savePatient(request):
    patient = Patient()
    if request.method == "POST":
        patient.savePatient(request.POST["patname"], request.POST["patcontact"], request.POST["pataddress"], request.POST["patdetails"])

    return render(request, "addpatient.html")

@csrf_exempt
def getPatient(request):
    patient = Patient()
    patients = patient.getPatient(0)
    return render(request, "patient.html", {"patients": patients})


@csrf_exempt
def patientRegform(request):
    return render(request, "patientreg.html")