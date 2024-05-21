from django.shortcuts import render, redirect
from .models import PatientList, MedicalExamination,Patient,DetailedPatientList,MedicationUsageReport, MedicationStockList
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, MedReport, MedicalExaminationForm, MedicationStockListForm
def home(request):
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
			messages.success(request, "You have successfully registered")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html',{'form': form})
	return render(request, 'register.html',{'form': form})
def record_all(request):
	if request.user.is_authenticated:
		records = PatientList.objects.all()
		return render(request, 'record_all.html',{'records':records})
def customer_record(request, pk):
    if request.user.is_authenticated:
        patient_list = PatientList.objects.filter(patient_id=pk)
        if patient_list.exists():
            patient_list = patient_list.first()
            med_examinations = MedicalExamination.objects.filter(patientlist=patient_list)
            return render(request, 'record.html', {'med_examinations': med_examinations, 'pk': pk})
        else:
            messages.error(request, "No patient record found.")
            return redirect('home')
    else:
        messages.success(request, "You must be logged in to use that page!")
        return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_customer = MedicalExamination.objects.get(id = pk)
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
                patient = Patient.objects.create(
                    name=form.cleaned_data['name'],
                    gender=form.cleaned_data['gender'],
                    birth_year=form.cleaned_data['year'],
                    address=form.cleaned_data['addr']
                )
                record = form.save(commit=False)
                record.patient = patient
                record.save()
                messages.success(request, "Record Added!")
                return redirect('record_all')
            else:
                messages.error(request, "Record not added! Please correct errors.")
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to use that page!")
        return redirect('home')
def update_record(request, pk):
    if request.user.is_authenticated:
        patient_list = PatientList.objects.get(pk=pk)
        if request.method == 'POST':
            form = MedicalExaminationForm(request.POST)
            if form.is_valid():
                examination = form.save(commit=False)
                examination.patientlist = patient_list
                examination.save()
                messages.success(request, "Examination record added successfully!")
                return redirect('record', pk=pk)
        else:
            form = MedicalExaminationForm()
        return render(request, 'update_record.html', {'form': form, 'pk': pk})
    else:
        messages.success(request, "You must be logged in to use that page!")
        return redirect('home')

def medical_report(request):
	if request.user.is_authenticated:
		records = MedicalExamination.objects.all()
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

def list_patient(request):
	if request.user.is_authenticated:
		patients = PatientList.objects.all()
		reports = MedicalExamination.objects.all()
		return render(request, 'list_patient.html',{'patients':patients,'reports':reports})

def all_patients(request):
	if request.user.is_authenticated:
		detailed_patients = DetailedPatientList.objects.select_related('patientlist__patient', 'examination').all()
		return render(request, 'all_patients.html', {'detailed_patients': detailed_patients})
	else:
		messages.success(request, "You must be logged in to use that page!")
		return redirect('home')
def medication_usage_report(request):
    if request.user.is_authenticated:
        reports = MedicationUsageReport.objects.all()
        return render(request, 'medication_usage_report.html', {'reports': reports})
    else:
        messages.success(request, "You must be logged in to use that page!")
        return redirect('home')

def new_medication_entry(request):
    if request.method == 'POST':
        form = MedicationStockListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medication_stock_list')
    else:
        form = MedicationStockListForm()
    return render(request, 'new_medication_entry.html', {'form': form})

def medication_stock_list(request):
    stock_list = MedicationStockList.objects.all()
    return render(request, 'medication_stock_list.html', {'stock_list': stock_list})