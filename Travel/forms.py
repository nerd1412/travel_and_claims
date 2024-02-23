from dataclasses import fields 
from datetime import datetime
from multiprocessing import AuthenticationError
from tkinter import Widget
from turtle import width
from unittest.util import _MAX_LENGTH
# from .models import Travelrequestheader,Travelflightdetails,Travelhoteldetails,Non_Emp_Details,Travelvisadetails,Travelforexdetails,Travelcarbookingdetails,Expenseclaimhead,Workbreakdownstructure,Pettycashdetails,Pettycashheader,Expenseclaimdetails,AdvanceRequestdetails,Divassignmentuser
# from .models import  GradeModel,WorkcenterModel,DepartmentModel,Expenseheadmaster,Expensesubheadmaster,Basecostcenter,Projectmaster,Internalorder,Advancerequesthead,Advancerequestsubheadmaster,DivmasterModel,UserroleModel,TitledetailsModel,MulticityDetails       
from .models import *
from django import forms
# from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory
from Travel.models import MyUser
from django.forms import modelformset_factory
from django.forms import inlineformset_factory
from django.forms import BaseFormSet
from django.core.validators import MinValueValidator
from datetime import date
from django.utils import timezone
from django.forms import DateInput
import itertools
from django.forms import widgets
from django.forms.utils import flatatt
from django.utils.html import format_html,format_html_join
import random,string
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from base64 import urlsafe_b64encode
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from datetime import datetime



# class MyUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['user_name'].widget.attrs.update({
#             'class': 'form-input',
#             'required': '',
#             'name': 'user_name',
#             'id': 'user_name',
#             'type': 'text',
#             'placeholder': 'John',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['first_name'].widget.attrs.update({
#             'class': 'form-input',
#             'required': '',
#             'name': 'first_name',
#             'id': 'first_name',
#             'type': 'text',
#             'placeholder': 'John',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['last_name'].widget.attrs.update({
#             'class': 'form-input',
#             'required': '',
#             'name': 'last_name',
#             'id': 'last_name',
#             'type': 'text',
#             'placeholder': 'Doe',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['email'].widget.attrs.update({
#             'class': 'form-input',
#             'required': '',
#             'name': 'email',
#             'id': 'email',
#             'type': 'email',
#             'placeholder': 'Enter Email',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['efforts'].widget.attrs.update({
#             'class': 'form-input',
#             'required': '',
#             'name': 'efforts',
#             'id': 'efforts',
#             'type': 'text',
#             'placeholder': 'Efforts',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['emp_id'].widget.attrs.update({
#             'class': 'form-input',
#             'required': '',
#             'name': 'emp_id',
#             'id': 'emp_id',
#             'type': 'text',
#             'placeholder': 'Employee Id',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['role'].widget.attrs.update({
#             'class': 'form-select',
#             'required': '',
#             'name': 'role',
#             'id': 'role',
#             'type': 'select',
#             'placeholder': 'Role',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['grade'].widget.attrs.update({
#             'class': 'form-select',
#             'required': '',
#             'name': 'grade',
#             'id': 'grade',
#             'type': 'select',
#             'placeholder': 'Grade',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['department'].widget.attrs.update({
#             'class': 'form-select',
#             'required': '',
#             'name': 'department',
#             'id': 'department',
#             'type': 'select',
#             'placeholder': 'Department',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['workcenter'].widget.attrs.update({
#             'class': 'form-select',
#             'required': '',
#             'name': 'workcenter',
#             'id': 'workcenter',
#             'type': 'select',
#             'placeholder': 'Workcenter',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['emp_type'].widget.attrs.update({
#             'class': 'form-select',
#             'required': '',
#             'name': 'emp_type',
#             'id': 'emp_type',
#             'type': 'select',
#             'placeholder': 'Employee Type',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['cost_center'].widget.attrs.update({
#             'class': 'form-select',
#             'required': '',
#             'name': 'cost_center',
#             'id': 'cost_center',
#             'type': 'select',
#             'placeholder': 'Costcenter',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['profile'].widget.attrs.update({
#             'class': 'form-select',
#             'required': '',
#             'name': 'profile',
#             'id': 'profile',
#             'type': 'select',
#             'placeholder': 'Profile',
#             'maxlength': '16',
#             'minlength': '6',
#         })
#         self.fields['profile'].widget.attrs.update({
#             'class': 'form-select',
#             'required': '',
#             'name': 'profile',
#             'id': 'profile',
#             'type': 'select',
#             'placeholder': 'Profile',
#             'maxlength': '16',
#             'minlength': '6',
#         })
        # self.fields['emp_status'].widget.attrs.update({
        #     'class': 'form-select',
        #     'required': '',
        #     'name': 'emp_status',
        #     'id': 'emp_status',
        #     'type': 'radio',
        #     'placeholder': 'Employee Status',
        #     'maxlength': '16',
        #     'minlength': '6',
        # })
        # self.fields['auth'].widget.attrs.update({
        #     'class': 'form-control',
        #     'required': '',
        #     'name': 'auth',
        #     'id': 'auth',
        #     'type': 'radio',
        #     'placeholder': 'Authorization',
        # })
        # self.fields['joining_date'].widget.attrs.update({
        #     'class': 'form-control',
        #     'required': '',
        #     'name': 'joining_date',
        #     'id': 'joining_date',
        #     'type': 'date',
        #     'placeholder': 'Joining Date',
        # })
        # self.fields['dob'].widget.attrs.update({
        #     'class': 'form-control',
        #     'required': '',
        #     'name': 'dob',
        #     'id': 'dob',
        #     'type': 'date',
        #     'placeholder': 'DOB',
        # })

#     class Meta:
#         model = MyUser
#         fields = ('user_name','email','emp_id','first_name','last_name','emp_type','cost_center','emp_status','auth','joining_date','efforts','profile','mobileno','password1','password2','address','role','grade','department','workcenter','dob')


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('user_name','email','emp_id','first_name','last_name','emp_type','cost_center','emp_status','auth','joining_date','efforts','mobileno','address','role','grade','department','workcenter','dob')

        widgets = {
                        "first_name":forms.TextInput(attrs={'class': 'form-control'}),
                        "last_name":forms.TextInput(attrs={'class': 'form-control'}),
                        "email":forms.EmailInput(attrs={'class': 'form-control'}),
                        "efforts":forms.TextInput(attrs={'class': 'form-control'}),
                        "mobileno":forms.TextInput(attrs={'class': 'form-control'}),
                        "address":forms.TextInput(attrs={'class': 'form-control'}),
                        "emp_id":forms.TextInput(attrs={'class': 'form-control'}),
                        "user_name":forms.TextInput(attrs={'class': 'form-control'}),
                        "role":forms.Select(attrs={"class":"form-select"}),
                        "grade":forms.Select(attrs={"class":"form-select"}),
                        "department":forms.Select(attrs={"class":"form-select"}),
                        "workcenter":forms.Select(attrs={"class":"form-select"}),
                        "emp_type":forms.Select(attrs={"class":"form-select"}),
                        "cost_center":forms.Select(attrs={"class":"form-select"}),
                        # "profile":forms.Select(attrs={"class":"form-select"}),
                        "emp_status":forms.RadioSelect(),
                        "auth":forms.RadioSelect(),
                        "joining_date":forms.DateInput(attrs={'class': 'form-control','type':'date'}),
                        "dob":forms.DateInput(attrs={'class': 'form-control','type':'date'})

                }
        
    def __init__(self, *args, **kwargs):
        self.user_name = kwargs.pop('user_name', None)
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.HiddenInput()
        self.fields['password2'].widget = forms.HiddenInput()
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob:
            if dob > datetime.now().date():
                raise forms.ValidationError('Date of birth cannot be in the future.')
            if dob < datetime(1900, 1, 1).date():
                raise forms.ValidationError('Enter a valid date.')
        return dob
    
    def clean_joining_date(self):
        joining_date = self.cleaned_data.get('joining_date')
        if joining_date:
            if joining_date > datetime.now().date():
                raise forms.ValidationError('Joining Date cannot be in the future.')
        return joining_date

    def clean(self):
        cleaned_data = super().clean()
        password1 = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        cleaned_data['password1'] = password1
        cleaned_data['password2'] = password1
        return cleaned_data
        
    def save(self, commit=True):
        user = super().save(commit=False)
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        user.set_password(password)
        emp_created_by_id = self.cleaned_data.get('emp_created_by')
        emp_mod_by_id = self.cleaned_data.get('emp_mod_by')
        user_name = self.cleaned_data.get('user_name') 
        if emp_created_by_id:
            user.emp_created_by_id = emp_created_by_id
        if emp_mod_by_id:
            user.emp_mod_by_id = emp_mod_by_id
        if commit:
            user.save()
            self.send_welcome_email(user, password,user_name)
        return user

    def send_welcome_email(self, user, password, user_name):
        subject = 'Welcome to Aakit Technologies'
        reset_url = reverse('password_reset_confirm', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)), 'token': default_token_generator.make_token(user)})
        reset_url = f"http://127.0.0.1:8000{reset_url}"
        context = {
            'user': user,
            'password': password,
            'reset_url': reset_url,
            'user_name': user_name,
        }
        html_message = render_to_string('email_template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'malikrao14@gmail.com'
        to_email = user.email 
        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)


    # def send_password_change_email(self, user):
    #     last_password_change_date = user.pass_date_changed  # Make sure this field exists in your model
    #     if last_password_change_date is None:
    #         return
        
    #     expiration_date = last_password_change_date + timedelta(days=-1)
    #     current_date = datetime.now().date()

    #     if current_date > expiration_date:
    #         subject = 'Change Your Password'
    #         reset_url = reverse('password_reset_confirm', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)), 'token': default_token_generator.make_token(user)})
    #         reset_url = f"http://127.0.0.1:8000{reset_url}"
    #         context = {
    #             'user': user,
    #             'reset_url': reset_url,
    #         }
    #         html_message = render_to_string('email_template.html', context)
    #         plain_message = strip_tags(html_message)
    #         from_email = 'malikrao14@gmail.com'
    #         to_email = user.email 
    #         send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

    # def send_password_change_email(user):
        # last_password_change_date = user.pass_date_changed  # Make sure this field exists in your model
        # if last_password_change_date is None:
        #     return  # No previous password change date, no need to send an email

    #     # Calculate the expiration date (90 days from the last change)
        # expiration_date = last_password_change_date + timedelta(days=1)

        # # Get the current date
        # current_date = datetime.now().date()

    #     if current_date > expiration_date:
    #         subject = 'Change Your Password'
    #         message = 'Your password has expired. Please change it immediately.'
    #         from_email = 'malikrao14@gmail.com'  # Set your email
    #         recipient_list = [user.email]

    #         # Generate a password reset token and URL
    #         uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    #         token = default_token_generator.make_token(user)
    #         reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
    #         reset_url = f"http://127.0.0.1:8000{reset_url}"

            # context = {
            #     'user': user,
            #     'reset_url': reset_url,
            # }

    #         html_message = render_to_string('email_template.html', context)
    #         plain_message = strip_tags(html_message)

    #         send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

        
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['profile'].choices = self.get_profile_choices()

    # def get_profile_choices(self):
    #     profiles = ProfileModel.objects.order_by('TPFCNAME')
    #     choices = []
    #     added_profiles = set()
    #     for profile in profiles:
    #         if profile.TPFCNAME not in added_profiles:
    #             employees = MyUser.objects.filter(id=profile.TPFCMANID_id)
    #             employee_names = [f"{employee.first_name} {employee.last_name}" for employee in employees]
    #             employee_names_str = '/'.join(employee_names)
    #             choice_label = f"{profile.TPFCNAME} - {employee_names_str}"
    #             choices.append((profile.TPFCINTID, choice_label))
    #             added_profiles.add(profile.TPFCNAME)
    #         else:
    #             existing_choice = next((choice for choice in choices if choice[1].startswith(profile.TPFCNAME)), None)
    #             if existing_choice:
    #                 existing_employee_names = existing_choice[1].split(' - ')[1].split('/')
    #                 employees = MyUser.objects.filter(id=profile.TPFCMANID_id)
    #                 new_employee_names = [f"{employee.first_name} {employee.last_name}" for employee in employees]
    #                 combined_employee_names = existing_employee_names + new_employee_names
    #                 employee_names_str = '/'.join(combined_employee_names)
    #                 existing_choice_label = f"{profile.TPFCNAME} - {employee_names_str}"
    #                 choices.remove(existing_choice)
    #                 choices.append((profile.TPFCINTID, existing_choice_label))
    #     return choices

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['profile'].choices = self.get_profile_choices()

    # def get_profile_choices(self):
    #     profiles = AssignProfileModel.objects.filter(TPFAPRNAME__isnull=False).order_by('TPFAPRNAME__TPFCNAME')
    #     choices = []
    #     added_profiles = set()
    #     for profile in profiles:
    #         employees = MyUser.objects.filter(id=profile.TPFAEMPID_id)
    #         employee_names = [f"{employee.first_name}/{employee.last_name}" for employee in employees]
    #         employee_names_str = ', '.join(employee_names)
    #         choice_label = f"{profile.TPFAPRNAME.TPFCNAME}/{employee_names_str}"
    #         choice = (profile.TPFAPRNAME_id, choice_label)
    #         if choice not in added_profiles:
    #             choices.append(choice)
    #             added_profiles.add(choice)
    #     return choices




class Loginform():
    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    
class BookingStatusForm(forms.ModelForm):
    status = forms.CharField(label="Booking Status",required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'eg: Applied'}))
    
    class Meta:
        model = BookingStatus
        fields = [
            "status",
        ]

class ProgressStatusForm(forms.ModelForm):
    status = forms.CharField(label="Progress Status",required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'eg: Applied'}))
    
    class Meta:
        model = ProgressStatus
        fields = [
            "status",
        ]


class Travelrequestheaderform(forms.ModelForm):
    THTRPNAME = forms.CharField(label="Trip Name", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: Trip to Nashik'}))
    THPURPOSE = forms.CharField(label="Purpose Of Visit", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: Presentation Meeting'}))
    THTRVTYP = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: Enter Travel type'}))

    THBOOKSTA = forms.ModelChoiceField(
        required=False,
        queryset=BookingStatus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    THPROJ = forms.ModelChoiceField(
        required=False,
        queryset=Projectmaster.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    THTRVTYP = forms.CharField(label="Travel Type", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Travel Type'}))
    THTASTATUS = forms.ModelChoiceField(
        required=False,
        queryset=TravelStatus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Travelrequestheader
        fields = [
            "THTRPNAME",
            "THPURPOSE",
            "THTRVTYP",
            "THSTUSTYP",
            "THPROJ",
            "THBOOKSTA",
            "THTASTATUS",
        ]

        widgets = {
            "THTRVTYP": forms.Select(attrs={"class": "form-select"}),
            "THSTUSTYP": forms.Select(attrs={"class": "form-select"}),
            "THPROJ": forms.Select(attrs={"class": "form-select"}),
            "THTASTATUS": forms.Select(attrs={"class": "form-select"}),
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.fields['THBOOKSTA'].queryset.exists():
    #         self.fields['THBOOKSTA'].initial = self.fields['THBOOKSTA'].queryset.first().id

class Travelflightdetailsform(forms.ModelForm):  
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    TFLDTRPNAME = forms.ModelChoiceField(queryset=Travelrequestheader.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    TFLDDTEOFTRV = forms.DateField(label='Date Of Travel',required=True,widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))   
    TFLDPREF = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'eg: Business Class'}))
    TFLDRETURN = forms.DateField(label='To Place',required=False,widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))
    TFLDPREFAIR = forms.CharField(label="Pref Time",required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'eg: Air India'}))    
    TFLDFRMPLC = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter City'})) 
    TFLDTOPLC = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter City'})) 
    is_optional = forms.BooleanField(required=False, initial=False)
    TFLDPROGSTA = forms.ModelChoiceField(
        required=False,
        queryset=ProgressStatus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )



    class Meta:
        model = Travelflightdetails 
        fields = [ 
                 "TFLDTRPNAME",
                  "TFLDDTEOFTRV",
                  "TFLDRETURN",
                  "TFLDPREF",
                  "TFLDPREFAIR",
                  "TFLDFRMPLC",
                  "TFLDTOPLC",
                  "TFLDTRPTYP",
                  "is_optional",
                  "TFLDPROGSTA",
                  ]

        widgets = {
                        # "TFLDTRPNAME":forms.Select(attrs={"class":"form-select"}),
                        # "TFLDPRJTRF":forms.Select(attrs={"class":"form-select"}),
                        "TFLDTRPTYP":forms.RadioSelect(),

                }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.fields['TFLDPROGSTA'].queryset.exists():
    #         self.fields['TFLDPROGSTA'].initial = self.fields['TFLDPROGSTA'].queryset.first().id



class MulticityForm(forms.ModelForm):
    TFLDFRMPLC = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter City'})) 
    TFLDTOPLC = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter City'})) 
    TFLDDTEOFTRV = forms.DateField(label='Date Of Travel',required=True,widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))
    TFLDPROGSTA = forms.ModelChoiceField(
        required=False,
        queryset=ProgressStatus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Travelflightdetails 
        fields = [ 
                  "TFLDFRMPLC",
                  "TFLDTOPLC",
                  "TFLDDTEOFTRV",
                  "TFLDPROGSTA",
                  ]
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     date_of_travel = cleaned_data.get("TFLDDTEOFTRV")

    #     if date_of_travel and date_of_travel < date.today():
    #         raise forms.ValidationError("The date of travel cannot be in the past")

    #     return cleaned_data

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     today = date.today().strftime('%Y-%m-%d')
    #     self.fields['TFLDDTEOFTRV'].widget.attrs['min'] = today

# MulticityFormSet = modelformset_factory(MulticityDetails, form=Multicityform, extra=1)

# FlightFormSet = inlineformset_factory(Travelrequestheader, Travelflightdetails, form=Multicityform, extra=1)

class TravelVisaForm(forms.ModelForm):
    TVDTRAVEL = forms.ModelChoiceField(queryset=Travelrequestheader.objects.all(),required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    TVDTRAVDTE = forms.DateField(label='Travel Date',required=True,widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))
    TVDVISTGCOUN = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Enter Country'}))
    TVDVSAFES = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Enter Amount'}))
    TVDREMK = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Remarks'}))
    TVDPROGSTA = forms.ModelChoiceField(
        required=False,
        queryset=ProgressStatus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Travelvisadetails
        fields = [
                "TVDTRAVEL",
                "TVDTRAVDTE",
                "TVDVISTGCOUN",
                "TVDVSAFES",
                "TVDREMK",
                "TVDVISTYPE",
                "TVDPROGSTA",
        ]

        widgets = {
                        "TVDVISTYPE":forms.Select(attrs={"class":"form-select"}),

                }

class TravelForexForm(forms.ModelForm):
    TFDTRVTID = forms.ModelChoiceField(queryset=Travelrequestheader.objects.all(),required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    TFDTRAVDTE = forms.DateField(label='Travel Date',required=True,widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))
    TFDAMNT = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Enter Amount'}))
    TFDREMARK = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Remarks'}))
    TFDPROGSTA = forms.ModelChoiceField(
        required=False,
        queryset=ProgressStatus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    # TFDCURR = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Travelforexdetails
        fields = [
                "TFDTRVTID",
                "TFDTRAVDTE",
                "TFDAMNT",
                "TFDREMARK",
                "TFDCURR",
                "TFDCSHTYPE",
                "TFDPROGSTA",
        ]

        widgets = {
                        "TFDCURR":forms.Select(attrs={"class":"form-select"}),
                        "TFDCSHTYPE":forms.Select(attrs={"class":"form-select"}),
                }



class Travelhoteldetailsform(forms.ModelForm):    
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    THDTRHINTRID = forms.ModelChoiceField(queryset=Travelrequestheader.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    THDPREFHOTL = forms.CharField(label="Preferred Hotel",required=False, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'eg: Taj'}))   
    THDCHKINDTE = forms.DateField(label='Check In Date',required=True,widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))   
    THDCHKOTDTE = forms.DateField(label="Check Out Date",required=True, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))    
    THDCITY = forms.CharField(label="City",required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'eg: Mumbai'}))
    THDPROGSTA = forms.ModelChoiceField(
        required=False,
        queryset=ProgressStatus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )


    class Meta:
        model = Travelhoteldetails 
        # fields = "__all__"
        fields = [ 
                  "THDTRHINTRID",
                  "THDPREFHOTL",
                  "THDCHKINDTE",
                  "THDCHKOTDTE",
                  "THDCITY",
                  "THDHTYPE",
                  "THDPROGSTA",
                  ]
        
        widgets = {
                "THDHTYPE":forms.Select(attrs={"class":"form-select"})
        }
    
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     if self.fields['THDPROGSTA'].queryset.exists():
        #         self.fields['THDPROGSTA'].initial = self.fields['THDPROGSTA'].queryset.first().id


    
class Non_Emp_Detailsform(forms.ModelForm):       
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    TNEDNONEMPNAM = forms.CharField(label="Non Employee Nane",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    TNEDPPRSOFVIS = forms.CharField(label="Purpose of Visit",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    TNEDMOBLNO = forms.CharField(label="Mobile No",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    TNEDEML = forms.EmailField(label="Email",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    
    
    class Meta:
        model = Non_Emp_Details 
        fields = [ 
                  "TNEDNONEMPNAM",
                  "TNEDPPRSOFVIS",
                  "TNEDMOBLNO",
                  "TNEDEML",
                  ]

        
        
class Travelforexdetailsform(forms.ModelForm):    
    TFDTRVTID = forms.ModelChoiceField(queryset=Travelrequestheader.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    TFODTRAVDTE = forms.DateField(label="Travel Date",required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))  
    TFODSECT = forms.CharField(label="Sector",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    TFODCURR = forms.CharField(label="Currency",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
   
        
    class Meta:
        model = Travelforexdetails 
        fields = [ 
                  "TFDTRVTID",
                  "TFODTRAVDTE",
                  "TFODSECT",
                  "TFODCURR",                  
                  ]
        
        
class Travelcarbookingdetailsform(forms.ModelForm):
    TCBDTHID = forms.ModelChoiceField(queryset=Travelrequestheader.objects.all(),required=False, widget=forms.Select(attrs={'class': 'form-select'}))       
    TCBDTRAVDTE = forms.DateField(label="Travel Date",required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))
    TCBDFRLOC = forms.CharField(label="From",required=True, widget=forms.TextInput(attrs={'class': 'form-control '}))
    TCBDTOLOC = forms.CharField(label="To",required=True, widget=forms.TextInput(attrs={'class': 'form-control '}))
    TCBDPIKU = forms.DateField(label="Pickup Date",required=True, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))
    TCBDDROP = forms.DateField(label="Drop Date",required=True, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))
    TCBDPROGSTA = forms.ModelChoiceField(
        required=False,
        queryset=ProgressStatus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    # TCBDREM = forms.CharField(label="From",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    
    class Meta:
        model = Travelcarbookingdetails 
        # fields = "__all__"
        fields = [ 
                  "TCBDTHID",
                  "TCBDTRAVDTE",
                  "TCBDFRLOC",
                  "TCBDTOLOC",
                  "TCBDPIKU",
                  "TCBDDROP",
                  "TCBDCTYP", 
                  "TCBDPROGSTA",                
                  ]
        
        widgets = {
                 "TCBDCTYP":forms.Select(attrs={"class":"form-select"}),
            }

    

class Expenseclaimheadform(forms.ModelForm):
    ECHEHEDID = forms.IntegerField(label="Expense Head Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '}))
    ECHCLMMNT = forms.CharField(label="Expense Claim Month",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    ECHCLMHEDASIGD = forms.CharField(label="Expense Claim Head",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    ECHCLMHEDPYMTDTE = forms.DateField(label="Payment Date",required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))
           
    class Meta:
        model = Expenseclaimhead 
        fields = [ 
                  "ECHEHEDID",
                  "ECHCLMMNT",
                  "ECHCLMHEDASIGD",
                  "ECHCLMHEDPYMTDTE",
                  "ECHCLMSTUS",                  
                  ]
        
    widgets = {
                 "ECHCLMSTUS":forms.Select(attrs={"class":"form-select"}),
            }
    
    
class Workbreakdownstructureform(forms.ModelForm):
    WBSELMT = forms.CharField(label="WorkBreakdown Element",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    WBSDESP = forms.CharField(label="WorkBreakdown Description",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    WBSPMINTRID = forms.CharField(label="Project Id",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    
    class Meta:
        model = Workbreakdownstructure 
        fields = [ 
                  "WBSELMT",
                  "WBSDESP",
                  "WBSPMINTRID",
                  "WBSSTUS",
                                    
                  ]
        
    widgets = {
                 "WBSSTUS":forms.Select(attrs={"class":"form-select"}),
            }
 
    
class Pettycashheaderform(forms.ModelForm):
    PCHCLMMNT = forms.CharField(label="Petty Cash Month",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    PCHCLMHEDASIGD = forms.CharField(label="Petty Cash Assigned Manager",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    PCHHEDPYMTDTE = forms.DateField(label="Petty Cash Date",required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))
    PCHVCHRNO = forms.CharField(label="Voucher No",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    PCHVCHRDTE = forms.DateField(label="Voucher Date",required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))
    
    class Meta:
        model = Pettycashheader 
        fields = [ 
                  "PCHCLMMNT",
                  "PCHCLMHEDASIGD",
                  "PCHHEDPYMTDTE",                 
                  "PCHVCHRNO",
                  "PCHVCHRDTE",
                  "PCHCLMSTUS",
                                    
                  ]
        
    widgets = {
                 "PCHCLMSTUS":forms.Select(attrs={"class":"form-select"}),
            }
    
    
class Pettycashdetailsform(forms.ModelForm):
    PCDTYP = forms.CharField(label="Petty Cash Type",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))  
    # PCDHEDID = forms.IntegerField(label="Expense Head Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    # PCDSBHDID = forms.IntegerField(label="Expense SubHead Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    # PCDPROJID = forms.IntegerField(label="Expense Project Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    # PCDWRKBRKDWNSTRCTRID = forms.IntegerField(label="Expense WBS Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    # PCDINTRLORDRID = forms.IntegerField(label="Expense InternalOrder Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    PCDDTEOFCLM = forms.DateField(label="Date Of Claim",required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' })) 
    PCDWRKCNTR = forms.IntegerField(label="Petty Cash WorkCenter ",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    PCDBSECSTCNTR = forms.IntegerField(label="Base Cost Center",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    PCDEXPCSTCNTR = forms.IntegerField(label="Expense Cost Center",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    PCDDESP = forms.CharField(label="Petty Cash Description",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    # PCDAMT = forms.CharField(label="Petty Cash Amount",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    # PCDAPPVDAMT = forms.CharField(label="Petty Cash Approved Amount",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    
    class Meta:
        model = Pettycashdetails 
        fields = [ 
                  "PCDTYP",
                #   "PCDHEDID",
                #   "PCDSBHDID",                 
                #   "PCDPROJID",
                #   "PCDWRKBRKDWNSTRCTRID",
                #   "PCDINTRLORDRID",
                  "PCDDTEOFCLM",
                  "PCDWRKCNTR",
                  "PCDBSECSTCNTR",                 
                  "PCDDESP",
                #   "PCDAMT",
                #   "PCDAPPVDAMT",                                    
                
                ]
        
    
class Expenseclaimdetailsform(forms.ModelForm):
    ECDTYP = forms.CharField(label="Petty Cash Type",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))  
    ECDECHEHEDID = forms.IntegerField(label="Expense Head Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ECDEXSSBHDID = forms.IntegerField(label="Expense SubHead Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ECDPMPROJID = forms.IntegerField(label="Expense Project Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ECDWRKBRKDWNSTRCTRID = forms.IntegerField(label="Expense WBS Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ECDINTRLORDRID = forms.IntegerField(label="Expense InternalOrder Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ECDDTEOFCLM = forms.DateField(label="Date Of Claim",required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' })) 
    ECDWRKCNTR = forms.IntegerField(label="Petty Cash WorkCenter ",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ECDBSECSTCNTR = forms.IntegerField(label="Base Cost Center",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ECDEXPCSTCNTR = forms.IntegerField(label="Expense Cost Center",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ECDDESP = forms.CharField(label="Petty Cash Description",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    ECDAMT = forms.CharField(label="Petty Cash Amount",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    ECDAPPVDAMT = forms.CharField(label="Petty Cash Approved Amount",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    
    class Meta:
        model = Expenseclaimdetails 
        fields = [ 
                  "ECDTYP",
                  "ECDECHEHEDID",
                  "ECDEXSSBHDID",                 
                  "ECDPMPROJID",
                  "ECDWRKBRKDWNSTRCTRID",
                  "ECDINTRLORDRID",
                  "ECDDTEOFCLM",
                  "ECDWRKCNTR",
                  "ECDBSECSTCNTR",                 
                  "ECDDESP",
                  "ECDAMT",
                  "ECDAPPVDAMT",                                    
                
                ]


class AdvanceRequestdetailsform(forms.ModelForm):
    ARDTYP = forms.CharField(label="Petty Cash Type",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))  
    ARDECDHEDID = forms.IntegerField(label="Expense Head Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ARDECDSBHDID = forms.IntegerField(label="Expense SubHead Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    AARDECDPROJID = forms.IntegerField(label="Expense Project Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ARDECDWRKBRKDWNSTRCTRID = forms.IntegerField(label="Expense WBS Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ARDECDINTRLORDRID = forms.IntegerField(label="Expense InternalOrder Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ARDDTEOFCLM = forms.DateField(label="Date Of Claim",required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' })) 
    ARDWRKCNTR = forms.IntegerField(label="Petty Cash WorkCenter ",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ARDBSECSTCNTR = forms.IntegerField(label="Base Cost Center",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    ARDDESP = forms.CharField(label="Petty Cash Description",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    ARDAMT = forms.CharField(label="Petty Cash Amount",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    ARDAPPVDAMT = forms.CharField(label="Petty Cash Approved Amount",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    
    class Meta:
        model = AdvanceRequestdetails 
        fields = [ 
                  "ARDTYP",
                  "ARDECDHEDID",
                  "ARDECDSBHDID",                 
                  "AARDECDPROJID",
                  "ARDECDWRKBRKDWNSTRCTRID",
                  "ARDECDINTRLORDRID",
                  "ARDDTEOFCLM",
                  "ARDWRKCNTR",
                  "ARDBSECSTCNTR",                 
                  "ARDDESP",
                  "ARDAMT",
                  "ARDAPPVDAMT",                                    
                
                ]
       
        
class Tileautherizationdetailsform(forms.ModelForm):
    # TADTITDID = forms.CharField(label="Tile Id",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    # TADURROLTLE = forms.CharField(label="User Role Id",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    # TADDIVMINTRID = forms.CharField(label="Div Id ",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    TADSEQ = forms.IntegerField(label="Sequence Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    
    class Meta:
        model = Tileautherizationdetails 
        fields = [ 
                  "TADTITDID",
                  "TADURROLTLE",
                  "TADSEQ", 
                  "TADDIVMINTRID",
        ]
        widgets = {
                        "TADTITDID":forms.Select(attrs={"class":"form-select"}),
                        "TADURROLTLE":forms.Select(attrs={"class":"form-select"}),
                        "TADDIVMINTRID":forms.Select(attrs={"class":"form-select"}),
                }
        

class Divassignmentuserform(forms.ModelForm):
    # DIVASSUURROLTLE = forms.CharField(label="User Role",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    # DIVASSUDIVMID = forms.CharField(label="Div Id",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    DIVASSUSEQ = forms.IntegerField(label="Sequence Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
   
   
    class Meta:
        model = Divassignmentuser 
        fields = [ 
                  "DIVASSUURROLTLE",
                  "DIVASSUDIVMID",
                  "DIVASSUSEQ", 
        ]
        widgets = {
                        "DIVASSUDIVMID":forms.Select(attrs={"class":"form-select"}),
                        "DIVASSUURROLTLE":forms.Select(attrs={"class":"form-select"}),

                }
        
        
class Grade(forms.ModelForm):
    GDGRD = forms.CharField(label='Grade', required=True, error_messages={
        'required': 'Enter Grade'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    GDGRDDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
        
    class Meta:
        model = GradeModel
        fields = [
            "GDGRD",
            "GDGRDDESP",
        ]
        widgets = {
                        "GDGRD":forms.Select(attrs={"class":"form-select"}),
                }


class Workcenter(forms.ModelForm):
    WCWRKCNTR = forms.CharField(label='Workcenter', required=True, error_messages={
        'required': 'Enter Workcenter ID'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    WCWRKCNTRDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = WorkcenterModel
        exclude = ['WCCREABY','WCCREAON','WCMODIBY','WCMODION','WCWRKCNTR']
        fields = [
            "WCWRKCNTR",
            "WCWRKCNTRDESP",
            "status",
            "WCCREABY",
            "WCCREAON",
            "WCMODIBY",
            "WCMODION",
        ]
        widgets = {
                        "status":forms.RadioSelect(),
                }

class ProfileForm(forms.ModelForm):
    TPFCNAME = forms.CharField(label='Profile Name', required=True, error_messages={
        'required': 'Profile Name'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # TPFCMANID = forms.CharField(label='Manager ID', required=True, error_messages={
    #     'required': 'Select Manager'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = ProfileModel
        fields = [
            "TPFCNAME",
            "TPFCMANID",
        ]
        widgets = {
                        "TPFCMANID":forms.Select(attrs={"class":"form-select"}),

                }
        
# ProfileFormSet = formset_factory(ProfileForm, extra=1)
        
# class AssignProfileForm(forms.ModelForm):
#     TPFAFROMD = forms.DateField(label='From Date', required=True, error_messages={
#         'required': 'From Date'}, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': timezone.now().date()}))
#     TPFATODATE = forms.DateField(label='To Date', required=True, error_messages={
#         'required': 'To Date'}, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': timezone.now().date()}))
#     TPFAPRNAME = forms.ModelChoiceField(
#         queryset=ProfileModel.objects.all(),
#         label='Profile',
#         required=True,
#         widget=forms.Select(attrs={'class': 'form-select'})
#     )

#     class Meta:
#         model = AssignProfileModel
#         fields = [
#             "TPFAEMPID",
#             "TPFAPRNAME",
#             "TPFAFROMD",
#             "TPFATODATE",
#         ]
#         widgets = {
#             "TPFAEMPID": forms.Select(attrs={"class": "form-select"}),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['TPFAPRNAME'].choices = self.get_profile_choices()

#     # def get_profile_choices(self):
#     #     profiles = ProfileModel.objects.order_by('TPFCNAME').values('TPFCINTID', 'TPFCNAME').distinct()
#     #     unique_profiles = [(k, list(g)) for k, g in itertools.groupby(profiles, key=lambda x: x['TPFCNAME'])]
#     #     choices = []
#     #     for group in unique_profiles:
#     #         group_label = group[0]
#     #         group_profiles = group[1]
#     #         choice_group = [(profile['TPFCINTID'], profile['TPFCNAME']) for profile in group_profiles]
#     #         choices.append((group_label, choice_group))
#     #     return choices

#     def get_profile_choices(self):
#         profiles = ProfileModel.objects.order_by('TPFCNAME')
#         unique_profiles = []

#         added_profiles = set()
#         for profile in profiles:
#             if profile.TPFCNAME not in added_profiles:
#                 unique_profiles.append(profile)
#                 added_profiles.add(profile.TPFCNAME)

#         choices = [(profile.TPFCINTID, profile.TPFCNAME) for profile in unique_profiles]
#         return choices

#     def clean(self):
#         cleaned_data = super().clean()
#         profile = cleaned_data.get('TPFAPRNAME')

#         if not profile:
#             raise forms.ValidationError('Invalid profile.')

#         cleaned_data['TPFAPRNAME'] = profile
#         return cleaned_data

class AssignProfileForm(forms.ModelForm):
    TPFAFROMD = forms.DateField(label='From Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': timezone.now().date()}))
    TPFATODATE = forms.DateField(label='To Date',widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    TPFAPRNAME = forms.ChoiceField(label='Profile', required=True, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = AssignProfileModel
        fields = [
            "TPFAEMPID",
            "TPFAPRNAME",
            "TPFAFROMD",
            "TPFATODATE",
            "TPFASTATUS",
        ]
        widgets = {
            "TPFAEMPID": forms.Select(attrs={"class": "form-select"}),
            "TPFASTATUS":forms.RadioSelect(),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['TPFASTATUS'].required = False
        self.fields['TPFAFROMD'].required = False
        self.fields['TPFATODATE'].required = False
        self.fields['TPFATODATE'].widget.attrs['readonly'] = 'readonly'
        self.fields['TPFAFROMD'].initial = timezone.now().date()
        default_date = "9999-12-31"
        self.fields['TPFATODATE'].initial = default_date
        self.fields['TPFAPRNAME'].choices = self.get_profile_choices()


    def get_profile_choices(self):
        profiles = ProfileModel.objects.order_by('TPFCNAME')
        choices = []
        added_profiles = set()
        for profile in profiles:
            if profile.TPFCNAME not in added_profiles:
                employees = MyUser.objects.filter(id=profile.TPFCMANID_id)
                employee_names = [employee.first_name for employee in employees]
                employee_names_str = '/'.join(employee_names)
                choice_label = f"{profile.TPFCNAME}/{employee_names_str}"
                choices.append((profile.TPFCINTID, choice_label))
                added_profiles.add(profile.TPFCNAME)
            else:
                existing_choice = next((choice for choice in choices if choice[1].startswith(profile.TPFCNAME)), None)
                if existing_choice:
                    existing_employee_names = existing_choice[1].split('/')[1:]
                    employees = MyUser.objects.filter(id=profile.TPFCMANID_id)
                    new_employee_names = [employee.first_name for employee in employees]
                    combined_employee_names = existing_employee_names + new_employee_names
                    employee_names_str = '/'.join(combined_employee_names)
                    existing_choice_label = f"{profile.TPFCNAME}/{employee_names_str}"
                    choices.remove(existing_choice)
                    choices.append((profile.TPFCINTID, existing_choice_label))
        return choices

    def clean_TPFAPRNAME(self):
        profile_id = self.cleaned_data['TPFAPRNAME']
        try:
            profile = ProfileModel.objects.get(TPFCINTID=int(profile_id))
        except (ProfileModel.DoesNotExist, ValueError):
            raise forms.ValidationError('Invalid profile.')
        return profile


class Department(forms.ModelForm):
    DDDEPRT = forms.CharField(label='Department', required=True, error_messages={
        'required': 'Enter Department'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    DDDEPRTDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = DepartmentModel
        fields = [
            "DDDEPRT",
            "DDDEPRTDESP",
        ]
        widgets = {
                        "DDDEPRT":forms.Select(attrs={"class":"form-select"}),
                }


class Expenseheadmaster(forms.ModelForm):
    EXHEXPHEDID = forms.IntegerField(label='Head ID', required=True, error_messages={
        'required': 'Enter ID'}, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    EXHHEDTLE = forms.CharField(label='Title', required=True, error_messages={
        'required': 'Enter Title'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    EXHHEDDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Expenseheadmaster
        fields = [
            "EXHEXPHEDID",
            "EXHHEDTLE",
            "EXHHEDDESP",
        ]


class Expensesubheadmaster(forms.ModelForm):
    EXSEXPID = forms.IntegerField(label='Subhead ID', required=True, error_messages={
        'required': 'Enter ID'}, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    EXSTLE = forms.CharField(label='Title', required=True, error_messages={
        'required': 'Enter Title'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    EXSDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Expensesubheadmaster
        fields = [
            "EXSEXPID",
            "EXSTLE",
            "EXSDESP",
        ]


class Basecostcenterform(forms.ModelForm):
    BCCDESP =  forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    BCCEXPCSTCNTR =  forms.IntegerField(label='ID', required=True, error_messages={
        'required': 'Enter Base Cost ID'}, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Basecostcenter
        exclude = ['BCCCREABY','BCCCREAON','BCCMODIBY','BCCMODION']
        fields = [
            "BCCDESP",
            "BCCEXPCSTCNTR",
            "BCCCREABY",
            "BCCCREAON",
            "BCCMODIBY",
            "BCCMODION",
        ]


class Projectmaster(forms.ModelForm):
    PMPROJID = forms.IntegerField(label='Project ID', required=True, error_messages={
        'required': 'Enter ID'}, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    PMSTUS = forms.Select(attrs={"class":"form-select"})
    PMDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Projectmaster
        fields = [
            "PMPROJID",
            "PMSTUS",
            "PMDESP",
        ]
    
    
class Internalorder(forms.ModelForm):
    IODINTRID = forms.IntegerField(label='Internal ID', required=True, error_messages={
        'required': 'Enter ID'}, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    IODSTUS = forms.Select(attrs={"class":"form-select"})
    IODDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Internalorder
        fields = [
            "IODINTRID",
            "IODSTUS",
            "IODDESP",
        ]


# class EmployeeMaster(forms.ModelForm):
#     EMEMPCOD = forms.IntegerField(label='Code', required=True, error_messages={
#         'required': 'Enter code'}, widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     EMEMLID = forms.CharField(label='Email Id', required=True, error_messages={
#         'required': 'Enter Email'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     EMGRD = forms.CharField(label='Grade', required=True, error_messages={
#         'required': 'Enter Grade'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     EMDESG = forms.CharField(label='Designation', required=True, error_messages={
#         'required': 'Enter Designation'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     EMMOBLNO = forms.CharField(label='Mobile No', required=True, error_messages={
#         'required': 'Enter Mobile No'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     EMDEPRT = forms.CharField(label='Department', required=True, error_messages={
#         'required': 'Enter Department'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     EMWRKCNTR = forms.CharField(label='Workcenter', required=True, error_messages={
#         'required': 'Enter Workcenter'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     EMCOMPNAM = forms.CharField(label='Company Name', required=True, error_messages={
#         'required': 'Enter Company Name'}, widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = EmployeeMaster
#         fields = [
#             "EMEMPCOD",
#             "EMEMLID",
#             "EMGRD",
#             "EMDESG",
#             "EMMOBLNO",
#             "EMDEPRT",
#             "EMWRKCNTR",
#             "EMCOMPNAM",
#         ]


class Advancerequesthead(forms.ModelForm):
    ARHEMPCOD =  forms.IntegerField(label='Code', required=True, error_messages={
        'required': 'Enter code'}, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ARHMNT = forms.CharField(label='Title', required=True, error_messages={
        'required': 'Enter Title'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ARHSTUS = forms.Select(attrs={"class":"form-select"})
    ARHASIGD = forms.CharField(label='Title', required=True, error_messages={
        'required': 'Enter Title'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ARHPYMTDTE = forms.CharField(label='Title', required=True, error_messages={
        'required': 'Enter Title'}, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Advancerequesthead
        fields = [
            "ARHEMPCOD",
            "ARHMNT",
            "ARHSTUS",
            "ARHASIGD",
            "ARHPYMTDTE",
        ]


class Advancerequestsubheadmaster(forms.ModelForm):
    ARSMID = forms.IntegerField(label='ID', required=True, error_messages={
        'required': 'Enter ID'}, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ARSMTLE = forms.CharField(label='Title', required=True, error_messages={
        'required': 'Enter Title'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ARSMDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Advancerequestsubheadmaster
        fields = [
            "ARSMID",
            "ARSMTLE",
            "ARSMDESP",
        ]


class Divmaster(forms.ModelForm):
    DIVMTLE = forms.CharField(label='Title', required=True, error_messages={
        'required': 'Enter Title'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    DIVMDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = DivmasterModel
        fields = [
            "DIVMTLE",
            "DIVMDESP",
        ]


class Userrole(forms.ModelForm):
    URROLTLE = forms.CharField(label='Title', required=True, error_messages={
        'required': 'Enter Title'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    URROLDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = UserroleModel
        exclude = ['URMODION','URCREAON','URCREABY','URMODIBY']
        fields = [
            "URROLTLE",
            "URROLDESP",
            "URRESP",
            "URCREABY",
            "URMODIBY",
            "URMODION",
            "URCREAON",
        ]

        widgets = {
                        "URRESP":forms.Select(attrs={"class":"form-select"}),
                }
    


class Titledetails(forms.ModelForm):
    TITDTLTLE = forms.CharField(label='Title', required=True, error_messages={
        'required': 'Enter Title'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    TITDDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    TITDURL = forms.CharField(label='URL', required=True, error_messages={
        'required': 'Enter URL'}, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = TitledetailsModel
        fields = [
            "TITDTLTLE",
            "TITDDESP",
            "TITDURL",
        ]

