from dataclasses import fields 
from datetime import datetime
from multiprocessing import AuthenticationError
from tkinter import Widget
from turtle import width
from unittest.util import _MAX_LENGTH
from .models import Travelrequestheader,Travelflightdetails,Travelhoteldetails,Non_Emp_Details,Travelvisadetails,Travelforexdetails,Travelcarbookingdetails,Expenseclaimhead,Workbreakdownstructure,Pettycashdetails,Pettycashheader,Expenseclaimdetails,AdvanceRequestdetails,Divassignmentuser
from .models import  GradeModel,WorkcenterModel,DepartmentModel,Expenseheadmaster,Expensesubheadmaster,Basecostcenter,Projectmaster,Internalorder,Advancerequesthead,Advancerequestsubheadmaster,DivmasterModel,UserroleModel,TitledetailsModel,TravelDetails,MulticityDetails       
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



class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('user_name','email','first_name','last_name','mobileno','password1','password2','address','role','grade','department','workcenter','dob')

        widgets = {
                        "role":forms.Select(attrs={"class":"form-select"}),
                        "grade":forms.Select(attrs={"class":"form-select"}),
                        "department":forms.Select(attrs={"class":"form-select"}),
                        "workcenter":forms.Select(attrs={"class":"form-select"}),
                        "dob":forms.DateInput(attrs={'class': 'form-control','type':'date' })

                }

class Loginform():
    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


class Travelrequestheaderform(forms.ModelForm):
    THTRPNAME = forms.CharField(label="Trip Name",required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'eg: Trip to Nashik'}))
    THPURPOSE = forms.CharField(label="Purpose Of Visit",required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'eg: Presentation Meeting'}))

    class Meta:
        model = Travelrequestheader 
        fields = [ 
                  "THTRPNAME",
                  "THPURPOSE",
                  "THTRVTYP",
                  "THSTUSTYP",
                  "THPROJ",
                  ]

        widgets = {
                            "THTRVTYP":forms.Select(attrs={"class":"form-select"}),
                            "THSTUSTYP":forms.Select(attrs={"class":"form-select"}),
                            "THPROJ":forms.Select(attrs={"class":"form-select"}),

                    }
    

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
                  ]

        widgets = {
                        # "TFLDTRPNAME":forms.Select(attrs={"class":"form-select"}),
                        # "TFLDPRJTRF":forms.Select(attrs={"class":"form-select"}),
                        "TFLDTRPTYP":forms.RadioSelect(),

                }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     date_of_travel = cleaned_data.get("TFLDDTEOFTRV")

    #     if date_of_travel and date_of_travel < date.today():
    #         raise forms.ValidationError("The date of travel cannot be in the past")

    #     return cleaned_data

    # def clean(self):
    #     cleaned_data = super().clean()
    #     is_optional = cleaned_data.get('is_optional')
    #     if is_optional:
    #         self.fields['TFLDFRMPLC'].required = False
    #         self.fields['TFLDTOPLC'].required = False
    #         self.fields['TFLDDTEOFTRV'].required = False
    #     return cleaned_data
    
# FlightFormSet = formset_factory(Travelflightdetailsform, extra=1)


class MulticityForm(forms.ModelForm):
    TFLDFRMPLC = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter City'})) 
    TFLDTOPLC = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter City'})) 
    TFLDDTEOFTRV = forms.DateField(label='Date Of Travel',required=True,widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))
    

    class Meta:
        model = Travelflightdetails 
        fields = [ 
                  "TFLDFRMPLC",
                  "TFLDTOPLC",
                  "TFLDDTEOFTRV",
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
    TVDVISTGCOUN = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Enter City'}))
    TVDVSAFES = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Enter Amount'}))
    TVDREMK = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Remarks'}))

    class Meta:
        model = Travelvisadetails
        fields = [
                "TVDTRAVEL",
                "TVDTRAVDTE",
                "TVDVISTGCOUN",
                "TVDVSAFES",
                "TVDREMK",
                "TVDVISTYPE",
        ]

        widgets = {
                        "TVDVISTYPE":forms.Select(attrs={"class":"form-select"}),

                }

class TravelForexForm(forms.ModelForm):
    TFDTRVTID = forms.ModelChoiceField(queryset=Travelrequestheader.objects.all(),required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    TFDTRAVDTE = forms.DateField(label='Travel Date',required=True,widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))
    TFDAMNT = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Enter Amount'}))
    TFDREMARK = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Remarks'}))
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
                  ]
        
        widgets = {
                "THDHTYPE":forms.Select(attrs={"class":"form-select"})
        }

    
    
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


class Travelvisadetailsform(forms.ModelForm):      
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    TVDTRAVEL = forms.ModelChoiceField(queryset=Travelrequestheader.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    TVDTRAVDTE = forms.DateField(label="Travel Date",required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date' }))  
    TVDVISTGCOUN = forms.CharField(label="Visiting Country",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    TVDVSAFES = forms.CharField(label="Visa Fees",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    TVDREMK = forms.CharField(label="Remarks",required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
   
    class Meta:
        model = Travelvisadetails 
        fields = [ 
                  "TVDTRAVEL",
                  "TVDTRAVDTE",
                  "TVDVISTGCOUN",
                  "TVDVSAFES",
                  "TVDREMK",
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
    TADTITDID = forms.CharField(label="Tile Id",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    TADURROLTLE = forms.CharField(label="User Role Id",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    TADDIVMINTRID = forms.CharField(label="Div Id ",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    TADSEQ = forms.IntegerField(label="Sequence Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
    
    class Meta:
        model = AdvanceRequestdetails 
        fields = [ 
                  "TADTITDID",
                  "TADURROLTLE",
                  "TADSEQ", 
        ]
        

class Divassignmentuserform(forms.ModelForm):
    DIVASSUURROLTLE = forms.CharField(label="User Role",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    DIVASSUDIVMID = forms.CharField(label="Div Id",required=False, widget=forms.TextInput(attrs={'class': 'form-control '})) 
    DIVASSUSEQ = forms.IntegerField(label="Sequence Id",required=False, widget=forms.NumberInput(attrs={'class': 'form-control '})) 
   
   
    class Meta:
        model = Divassignmentuser 
        fields = [ 
                  "DIVASSUURROLTLE",
                  "DIVASSUDIVMID",
                  "DIVASSUSEQ", 
        ]
        
        
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
        'required': 'Enter Workcenter'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    WCWRKCNTRDESP = forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = WorkcenterModel
        fields = [
            "WCWRKCNTR",
            "WCWRKCNTRDESP",
        ]
        widgets = {
                        "WCWRKCNTR":forms.Select(attrs={"class":"form-select"}),
                }


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


class Basecostcenter(forms.ModelForm):
    BCCDTLE = forms.CharField(label='Title', required=True, error_messages={
        'required': 'Enter Title'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    BCCDESP =  forms.CharField(label='Description', required=True, error_messages={
        'required': 'Enter Description'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    BCCEXPCSTCNTR =  forms.IntegerField(label='ID', required=True, error_messages={
        'required': 'Enter ID'}, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Basecostcenter
        fields = [
            "BCCDTLE",
            "BCCDESP",
            "BCCEXPCSTCNTR",
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
        fields = [
            "URROLTLE",
            "URROLDESP",
        ]
    


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

