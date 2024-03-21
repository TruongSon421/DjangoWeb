from django.shortcuts import render, redirect
from .models import PatientRecord,MedicalReport
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, MedReport
def home(request):
	records = PatientRecord.objects.all()
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again")
			return redirect('home')
	else:
		return render(request, 'home.html')
def login_user(request):
    pass
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password = password)
			login(request,user)
			messages.success(request, "You have sucessfully registered")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html',{'form': form})
	return render(request, 'register.html',{'form': form})
def record_all(request):
	if request.user.is_authenticated:
		records = PatientRecord.objects.all()
		return render(request, 'record_all.html',{'records':records})
def customer_record(request,pk):
	if request.user.is_authenticated:
		customer_record = PatientRecord.objects.get(id = pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You must be logged in to use that page!")
		return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_customer = PatientRecord.objects.get(id = pk)
		delete_customer.delete()
		messages.success(request, "Record Deleted Successfully!")
		return redirect('home')
	else:
		messages.success(request, "You must be logged in to use that page!")
		return redirect('home')
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				form.save()
				messages.success(request, "Record Added!")
				return redirect('record_all')
		return render(request, 'add_record.html',{'form':form})
	else:
		messages.success(request, "You must be logged in to use that page!")
		return redirect('home')
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = PatientRecord.objects.get(id = pk)
		form = AddRecordForm(request.POST or None, instance = current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record has been updated!")
			return redirect('record_all')
		return render(request, 'update_record.html',{'form':form, 'current_record': current_record})
	else:
		messages.success(request, "You must be logged in to use that page!")
		return redirect('home')
def medical_report(request):
	if request.user.is_authenticated:
		records = MedicalReport.objects.all()
		return render(request, 'medical_report.html',{'records':records})
def add_med_report(request):
	form = MedReport(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				form.save()
				messages.success(request, "Report Added!")
				return redirect('medical_report')
		return render(request, 'add_med_report.html',{'form':form})
	else:
		messages.success(request, "You must be logged in to use that page!")
		return redirect('home')