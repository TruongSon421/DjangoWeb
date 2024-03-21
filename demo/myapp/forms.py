from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import PatientRecord,MedicalReport
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    name = forms.CharField(label="",max_length=100,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'Username'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

class AddRecordForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="")
    gender = forms.ChoiceField(required=True, choices=[('M', 'Male'), ('F', 'Female')], widget=forms.Select(attrs={"class":"form-control"}), label="")
    year = forms.IntegerField(required=True, widget=forms.TextInput(attrs={"placeholder":"Year Of Birth", "class":"form-control"}), label="")
    addr = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    date= forms.DateField(required=True, widget=forms.DateInput(attrs={"type":"date", "class":"form-control"}), label="")

    class Meta:
        model = PatientRecord
        exclude = ("user",)

class MedReport(forms.ModelForm):
    PRED_CHOICES = [
        ('1', 'Type 1'),
        ('2', 'Type 2'),
        ('3', 'Type 3'),
        ('4', 'Type 4'),
        ('5', 'Type 5'),
    ]
    MEDICINE_CHOICES = [
        ('medicine1', 'Medicine 1'),
        ('medicine2', 'Medicine 2'),
        ('medicine3', 'Medicine 3'),
        ('medicine4', 'Medicine 4'),
        ('medicine5', 'Medicine 5'),
        ('medicine6', 'Medicine 6'),
        ('medicine7', 'Medicine 7'),
        ('medicine8', 'Medicine 8'),
        ('medicine9', 'Medicine 9'),
        ('medicine10', 'Medicine 10'),
        ('medicine11', 'Medicine 11'),
        ('medicine12', 'Medicine 12'),
        ('medicine13', 'Medicine 13'),
        ('medicine14', 'Medicine 14'),
        ('medicine15', 'Medicine 15'),
        ('medicine16', 'Medicine 16'),
        ('medicine17', 'Medicine 17'),
        ('medicine18', 'Medicine 18'),
        ('medicine19', 'Medicine 19'),
        ('medicine20', 'Medicine 20'),
        ('medicine21', 'Medicine 21'),
        ('medicine22', 'Medicine 22'),
        ('medicine23', 'Medicine 23'),
        ('medicine24', 'Medicine 24'),
        ('medicine25', 'Medicine 25'),
        ('medicine26', 'Medicine 26'),
        ('medicine27', 'Medicine 27'),
        ('medicine28', 'Medicine 28'),
        ('medicine29', 'Medicine 29'),
        ('medicine30', 'Medicine 30'),
    ]

    UNIT_CHOICES = [
        ('pill', 'Pill'),
        ('bottle', 'Bottle'),
    ]

    WAY_CHOICES = [
        ('1', 'Way 1'),
        ('2', 'Way 2'),
        ('3', 'Way 3'),
        ('4', 'Way 4'),
    ]
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="")
    date= forms.DateField(required=True, widget=forms.DateInput(attrs={"type":"date", "class":"form-control"}), label="")
    symptoms = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Symptoms", "class":"form-control"}), label="Symptoms")
    pred = forms.ChoiceField(required=True, choices=PRED_CHOICES, widget=forms.Select(attrs={"class":"form-control"}), label="Prediction")
    medicine = forms.ChoiceField(required=True, choices=MEDICINE_CHOICES, widget=forms.Select(attrs={"class":"form-control"}), label="Medicine")
    unit = forms.ChoiceField(required=True, choices=UNIT_CHOICES, widget=forms.Select(attrs={"class":"form-control"}), label="Unit")
    amount = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Amount", "class":"form-control"}), label="Amount")
    way = forms.ChoiceField(required=True, choices=WAY_CHOICES, widget=forms.Select(attrs={"class":"form-control"}), label="Way")

    class Meta:
        model = MedicalReport
        exclude = ("user",)