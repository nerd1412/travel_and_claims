from datetime import date
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from Travel.forms import Grade,Workcenter,Department,Loginform,UserroleModel
from .models import GradeModel,WorkcenterModel,DepartmentModel,UserroleModel,TitledetailsModel
from django.conf import settings
# from travel.forms import Travelform, Loginform
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.core.paginator import Paginator
from django.db.models import Sum
from django.contrib.auth.forms import AuthenticationForm
from Travel.forms import Pettycashdetailsform
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db import transaction
from django.forms import modelformset_factory
# from django.contrib.auth.forms import AuthenticationForm,MyUserCreationForm
from .forms import *
from django.contrib.auth import authenticate,login,logout

# from Travel.forms import CreateUserform
class SignUpView(SuccessMessageMixin,CreateView):
    model = MyUser
    form_class = MyUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('SignIn')
    success_message = 'signed up successfully'

# def signup(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             # u = form.save(commit=False)
#             # u.username = f'{u.username}@aakit.com'
#             u.save()
#             # username = form.cleaned_data.get('username')
#             username = u.username
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             p = PersonalModel.objects.create(user=user,PDUSERID= user.username,
#                             PDFIRSTN= user.first_name, PDLASTN = user.last_name,PDEMAIL = user.username,PDCREBY = request.user.username)
#             p.save()
#             return redirect('/admin')
#     else:
#         form = RegisterUserForm()
#         # form = RegisterUserForm(initial={'username':'@aakit.com'})
#     return render(request, 'registration/signup.html', {'form': form})

def mylogin(req):
    print(req.method)
    if req.method=='POST':
        form = AuthenticationForm(req.POST)
        username = req.POST['username']
        password = req.POST['password']
        if username and password :
            user = authenticate(req,username=username,password=password)
            if user:
                login(req,user)
                # if not req.user.is_superuser:
                #     req.session['pid']=PersonalModel.objects.filter(user=req.user)[0].pk
                messages.success(req,"Login Successfull.")
                # print(user.is_superuser)
                # if user.is_superuser:
                #     return redirect('/admin')
                return redirect("/home")
            else:
                messages.error(req,"Invalid Username or Password")
        else:
            messages.error(req,"Please Enter the username and Password")
    else:
        form = AuthenticationForm()
    return render(req,'login.html',{'form':form})


def home(request):
    return render(request,"home.html")




# def home(request):
#     if request.method == 'POST':
#         er = EmployeeMaster.objects.filter(user=request.user)
#         if len(er)>0:
#             form = EmployeeMaster(request.POST,request.FILES,isinstance=er[0])
#         else:
#             form = EmployeeMaster(request.POST,request.FILES)
#         if form.is_valid:
#             try:
#                 object = form.save()
#                 object.user = request.user
#                 object.EEMCREABY = request.user
#                 object.save()
#                 if len(er)>0:
#                     message.

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required(redirect_field_name='next',login_url='/mylogin')
# def home(request):
#     if request.method == 'POST':
#         pr = EmployeeMaster.objects.filter(user=request.user)
#         if len(pr)>0:
#             # print("if")
#             form = EmployeeMaster(request.POST,request.FILES,instance=pr[0])
#             # print(PersonalForm.PDPROIMG)
#         else:
#             # print("else")
#             form = EmployeeMaster(request.POST,request.FILES)
#         if form.is_valid:
#             try:
#                 object = form.save()
#                 object.user = request.user
#                 object.EMCREABY= request.user.username
#                 # object.PDMODBY
                
#                 object.save()
#                 if len(pr)>0:
#                     messages.success(request,"Details updated")
#                 else:
#                     form = EmployeeMaster(request.POST)
#                     messages.success(request,"Employee is added")
#                 # return HTTPResponse("Data Saved")
#             except Exception as e:
#                 print("Failed", e)
#                 pass
#             # form = EmployeeMaster()
#             # pr = EmployeeMaster.objects.filter(user=request.user)
#             # if pr:
#             #     pr.update(EMMODIBY=request.user.username)
#             #     form = EmployeeMaster(instance=pr[0])
#             return render(request, 'home.html', {'eform': form, 'pr': pr})

def expense(request):
    return render(request,"expense.html")

def advanceexp(request):
    return render(request,"advanceexp.html")

def dashboard(request):
    return render(request,"dashboard.html")

def emp(request):
    return render(request,"emp.html")

class SignUpView(SuccessMessageMixin,CreateView):
    model = MyUser
    form_class = MyUserCreationForm
    template_name = 'emp.html'
    success_url = reverse_lazy('home')
    success_message = 'signed up successfully'


def role(request):
    ctx ={}
    form = Userrole(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.URCREABY = request.user
        obj.save()
        print(request.user)
        messages.success(request,"Details added")
        
        print("Saved")
    else:
        print(form.errors)   
    data = UserroleModel.objects.all()
    paginator = Paginator(data, 10)
    page_number = 0
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages
    ctx={
        # 'data':data,
        'page_obj': page_obj,
        'nums': nums,
        'form':form
    }
    return render(request, "role.html", ctx)

# def grade_edit(request,id):
#     ge = GradeModel.objects.get(pk=id)   
#     if request.method == 'POST':
#         form = Grade(request.POST,instance=ge)
#         obj = form.save()
#         obj.GDMODIBY = request.user
#         obj.save()
#         messages.success(request,"Data is updated")
#     else:
#         form = Grade(instance=ge)
#     return render(request,'grade_edit.html',{'gform':form, 'g': ge })

def role_edit(request,id):
    ge = UserroleModel.objects.get(pk=id)
    if request.method == 'POST':
        form = Userrole(request.POST,instance=ge)
        obj = form.save()
        obj.URMODIBY = request.user
        obj.save()
        messages.success(request,"Data is updated")
        return redirect('/role/')
    else:
        form = Userrole(instance=ge)
    return render(request,'role_edit.html',{'uform':form,'g': ge})


def addiv(request):
    ctx ={}
    form = Divmaster(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.DIVMCREABY = request.user
        obj.save()
        print(request.user)
        messages.success(request,"Details added")
        
        print("Saved")
    else:
        print(form.errors)   
    data = DivmasterModel.objects.all()
    paginator = Paginator(data, 10)
    page_number = 0
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages
    ctx={
        # 'data':data,
        'page_obj': page_obj,
        'nums': nums,
        'form':form
    }
    return render(request, "addiv.html", ctx)


# def addtile(request):
#     context ={}
#     form = Titledetails(request.POST or None)
#     if form.is_valid():
#         print("valid")
#         obj = form.save()
#         print(request.user.id)
#         obj.TITDCREABY = request.user
#         obj.save()
#         messages.success(request,"Details added")
#         print("Saved")
#     else:
#         print(form.errors)
#         form = Titledetails()
#     context['form']= form
#     return render(request, "tile.html",context)

def addtile(request):
    ctx ={}
    form = Titledetails(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.TITDCREABY = request.user
        obj.save()
        print(request.user)
        messages.success(request,"Details added")
        
        print("Saved")
    else:
        print(form.errors)   
    data = TitledetailsModel.objects.all()
    paginator = Paginator(data, 10)
    page_number = 0
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages
    ctx={
        # 'data':data,
        'page_obj': page_obj,
        'nums': nums,
        'form':form
    }
    return render(request, "tile.html", ctx)


def pettycash(request):
    context ={}
    form = Pettycashdetailsform(request.POST or None)
    if form.is_valid():
        print("valid")
        form = form.save()
        form.user = request.user
        form.save()
        messages.success(request,"Details added")
        form = Pettycashdetailsform()
        print("Saved")
    else:
        print(form.errors)
        form = Pettycashdetailsform()   
    context['form']= form
    return render(request, "pettycash.html", context)


def grade_save(request):
    ctx ={}
    form = Grade(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.GDCREABY = request.user
        obj.save()
        print(request.user)
        messages.success(request,"Details added")
        
        print("Saved")
    else:
        print(form.errors)   
    data = GradeModel.objects.all()
    paginator = Paginator(data, 10)
    page_number = 0
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages
    ctx={
        # 'data':data,
        'page_obj': page_obj,
        'nums': nums,
        'form':form
    }
    return render(request, "grade.html", ctx)


def grade_edit(request,id):
    ge = GradeModel.objects.get(pk=id)   
    if request.method == 'POST':
        form = Grade(request.POST,instance=ge)
        obj = form.save()
        obj.GDMODIBY = request.user
        obj.save()
        messages.success(request,"Data is updated")
        return redirect('/grade_save/')
    else:
        form = Grade(instance=ge)
    return render(request,'grade_edit.html',{'gform':form, 'g': ge })



# def work_save(request):
#     ctx ={}
#     form = Workcenter(request.POST or None)
#     if form.is_valid():
#         print("valid")
#         form = form.save()
#         form.user = request.user
#         form.save()
#         messages.success(request,"Details added")
#         form = Workcenter()
#         print("Saved")
#     else:
#         print(form.errors)
#     data = WorkcenterModel.objects.all()
#     paginator = Paginator(data, 10)
#     page_number = 0
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     nums = "a" * page_obj.paginator.num_pages
#     ctx={
#         # 'data':data,
#         'page_obj': page_obj,
#         'nums': nums,
#         'form':form
#     }
#     return render(request, 'workcenter.html', ctx)

def work_save(request):
    ctx ={}
    form = Workcenter(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.WCCREABY = request.user
        obj.save()
        print(request.user)
        messages.success(request,"Details added")      
        print("Saved")
    else:
        print(form.errors)   
    data = WorkcenterModel.objects.all()
    paginator = Paginator(data, 10)
    page_number = 0
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages
    ctx={
        # 'data':data,
        'page_obj': page_obj,
        'nums': nums,
        'form':form
    }
    return render(request, "workcenter.html", ctx)



def work_edit(request,id):
    we = WorkcenterModel.objects.get(pk=id)   
    if request.method == 'POST':
        form = Workcenter(request.POST,instance=we)
        form.save()
        messages.success(request,"Data is updated")
    else:
        form = Workcenter(instance=we)
    
    return render(request,'workcenter_edit.html',{'wform':form, 'w': we })


# def depart_save(request):
#     ctx ={}
#     form = Department(request.POST or None)
#     if form.is_valid():
#         print("valid")
#         form = form.save()
#         form.user = request.user
#         form.save()
#         messages.success(request,"Details added")
#         form = Department()
#         print("Saved")
#     else:
#         print(form.errors)
#     data = DepartmentModel.objects.all()
#     paginator = Paginator(data, 10)
#     page_number = 0
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     nums = "a" * page_obj.paginator.num_pages
#     ctx={
#         # 'data':data,
#         'page_obj': page_obj,
#         'nums': nums,
#         'form':form
#     }
#     return render(request, "depart.html", ctx)

def depart_save(request):
    ctx ={}
    form = Department(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.DDCREABY = request.user
        obj.save()
        print(request.user)
        messages.success(request,"Details added")
        
        print("Saved")
    else:
        print(form.errors)   
    data = DepartmentModel.objects.all()
    paginator = Paginator(data, 10)
    page_number = 0
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages
    ctx={
        # 'data':data,
        'page_obj': page_obj,
        'nums': nums,
        'form':form
    }
    return render(request, "depart.html", ctx)


def depart_edit(request,id):
    de = DepartmentModel.objects.get(pk=id)
    print(de) 
    if request.method == 'POST':
        form = Department(request.POST,instance=de)
        obj = form.save()
        obj.DDMODIBY = request.user
        obj.save()    
        messages.success(request,"Data is updated")
    else:
        form = Department(instance=de)
    return render(request,'depart_edit.html',{'dform':form, 'd': de })

def trip(request):
    return render(request,"trip.html")


# def add_flight(from_location,to_location,depart_date,return_date,createdby,trip,pref,pref_air,booking_type='Round Trip'):
#     try:
#         booking = Travelflightdetails(TFLDFRMPLC=from_location,TFLDTOPLC=to_location,TFLDDTEOFTRV=depart_date,TFLDRETURN = None,TFLDCREABY=createdby,TFLDTRPNAME=trip,TFLDPREF=pref,TFLDPREFAIR=pref_air,TFLDTRPTYP=booking_type)
#         if return_date and booking_type == 'Round Trip':
#             # print("if")
#             return_booking = Travelflightdetails(TFLDFRMPLC=to_location,TFLDTOPLC=from_location,TFLDDTEOFTRV=return_date,TFLDCREABY=createdby,TFLDTRPNAME=trip,TFLDPREF=pref,TFLDPREFAIR=pref_air,TFLDTRPTYP=booking_type)
#             # return_booking.TFLDCREABY = depart_date
#             booking.save()
#             return_booking.save()
#         else:
#             # print("else")
#             booking = Travelflightdetails(TFLDFRMPLC=from_location,TFLDTOPLC=to_location,TFLDDTEOFTRV=depart_date,TFLDRETURN=return_date,TFLDCREABY=createdby,TFLDTRPNAME=trip,TFLDPREF=pref,TFLDPREFAIR=pref_air,TFLDTRPTYP=booking_type)
#             booking.save()
#             return [booking]
#     except Exception as e:
#         print(f"An error occurred while adding flight details: {e}")

def add_flight(from_location, to_location, depart_date, return_date, createdby, trip, pref, pref_air, booking_type='Round Trip', flight_form_data=None):
    try:
        if flight_form_data:
            for form_data in flight_form_data:
                flight = Travelflightdetails(TFLDFRMPLC=form_data['TFLDFRMPLC'], TFLDTOPLC=form_data['TFLDTOPLC'], TFLDDTEOFTRV=form_data['TFLDDTEOFTRV'], TFLDRETURN=form_data['TFLDRETURN'], TFLDCREABY=createdby, TFLDTRPNAME=trip, TFLDPREF=pref, TFLDPREFAIR=pref_air, TFLDTRPTYP=booking_type)
                flight.save()
        else:
            booking = Travelflightdetails(TFLDFRMPLC=from_location, TFLDTOPLC=to_location, TFLDDTEOFTRV=depart_date, TFLDRETURN=return_date, TFLDCREABY=createdby, TFLDTRPNAME=trip, TFLDPREF=pref, TFLDPREFAIR=pref_air, TFLDTRPTYP=booking_type)
            booking.save()
            if return_date and booking_type == 'Round Trip':
                return_booking = Travelflightdetails(TFLDFRMPLC=to_location, TFLDTOPLC=from_location, TFLDDTEOFTRV=return_date, TFLDCREABY=createdby, TFLDTRPNAME=trip, TFLDPREF=pref, TFLDPREFAIR=pref_air, TFLDTRPTYP=booking_type)
                return_booking.save()
            return [booking]
    except Exception as e:
        print(f"An error occurred while adding flight details: {e}")






def travel(request):
    MulticityFormSet = formset_factory(MulticityForm)
    MultiHotelFormSet = formset_factory(Travelhoteldetailsform)
    
    if request.method == 'POST':
        header_form = Travelrequestheaderform(request.POST)
        flight_form = Travelflightdetailsform(request.POST)
        hotel_form = Travelhoteldetailsform(request.POST)
        car_form = Travelcarbookingdetailsform(request.POST)
        visa_form = TravelVisaForm(request.POST)
        forex_form = TravelForexForm(request.POST)
        multicity_formset = MulticityFormSet(request.POST, prefix='multicity')
        multihotel_formset = MultiHotelFormSet(request.POST, prefix='multihotel')

        print(f"multicity_formset is valid: {multicity_formset.is_valid()}")
        if not multicity_formset.is_valid():
            print(f"multicity_formset errors: {multicity_formset.errors}")
        # print(f"trip_id: {header_form}")

        print(f"multihotel_formset is valid: {multihotel_formset.is_valid()}")
        if not multihotel_formset.is_valid():
            print(f"multihotel_formset errors: {multihotel_formset.errors}")

        if header_form.is_valid():
            travel_header = header_form.save(commit=False)
            header_form.save_m2m()
            travel_header.THRCREABY = request.user
            travel_header.save()
            header_form = Travelrequestheaderform()

            # Get the radio button value
            radio_button = request.POST.get('radio_button')

            # If radio button is checked, set not_required to True, otherwise False
            not_required = True if radio_button == 'on' else False

            # Set required field based on checkbox
            flight_form.fields['TFLDFRMPLC'].required = not not_required
            flight_form.fields['TFLDTOPLC'].required = not not_required
            flight_form.fields['TFLDDTEOFTRV'].required = not not_required



            if flight_form.is_valid():
                current_user = request.user
                from_location = flight_form.cleaned_data['TFLDFRMPLC']    
                to_location = flight_form.cleaned_data['TFLDTOPLC'] 
                depart_date = flight_form.cleaned_data['TFLDDTEOFTRV']    
                return_date = flight_form.cleaned_data['TFLDRETURN']
                booking_type = flight_form.cleaned_data['TFLDTRPTYP']
                trip_id = travel_header.THINTRID
                trip = Travelrequestheader.objects.get(THINTRID=trip_id)
                createdby = current_user
                pref = flight_form.cleaned_data['TFLDPREF']
                pref_air = flight_form.cleaned_data['TFLDPREFAIR']

                # not_required = request.POST.get('radio_button') == 'on'

                # # Set required field based on checkbox
                # flight_form.fields['TFLDFRMPLC'].required = not not_required
                # print(not_required)
                # print(flight_form.fields['TFLDFRMPLC'].required)

                if depart_date and depart_date < date.today():
                    messages.error(request, 'Departure date cannot be in the past')
                elif return_date and return_date < date.today():
                    messages.error(request, 'Return date cannot be in the past')
                elif booking_type == 'Round Trip' and not return_date:
                            if radio_button == 'on':
                                flight_form.fields['TFLDRETURN'].required = False
                            else:
                                messages.error(request, 'Return cannot be blank')
                else:
                    flight_form.fields['TFLDRETURN'].required = True
                     # here
                    if booking_type == 'Multi-city':
                        if not any(form.cleaned_data for form in multicity_formset.forms):
                            messages.error(request, 'Please provide multi-city flight details or delete section')
                        elif multicity_formset.is_valid():
                            print("true")
                            for i, form in enumerate(multicity_formset.forms):
                                if form.cleaned_data:
                                    from_city = form.cleaned_data.get('TFLDFRMPLC')
                                    to_city = form.cleaned_data.get('TFLDTOPLC')
                                    date_of_travel = form.cleaned_data.get('TFLDDTEOFTRV')

                                    if date_of_travel and date_of_travel < date.today():
                                        print('past')
                                        messages.error(request, 'Departure date cannot be in the past')
                                    else:                                      
                                        multicity_flight = form.save(commit=False)
                                        multicity_flight.TFLDFRMPLC = from_city
                                        multicity_flight.TFLDTOPLC = to_city
                                        multicity_flight.TFLDDTEOFTRV = date_of_travel
                                        multicity_flight.createdby = createdby
                                        multicity_flight.trip = trip
                                        multicity_flight.pref = pref
                                        multicity_flight.pref_air = pref_air
                                        add_flight(from_city, to_city, date_of_travel, None, createdby, trip, pref, pref_air, booking_type)
                                        messages.success(request, "Multi-city flights saved successfully")
                        else:
                            messages.error(request, "Multi-city formset is not valid. Please check your input.")
                            # print(multicity_formset.errors)
                    add_flight(from_location, to_location, depart_date, return_date, createdby, trip, pref, pref_air, booking_type)
                    messages.success(request, "Request saved successfully") 
                    flight_form = Travelflightdetailsform()

                if hotel_form.is_valid():
                    hotel = hotel_form.save(commit=False)
                    hotel.travel_header = travel_header
                    hotel.save()
                    hotel_form = Travelhoteldetailsform()
                    messages.success(request, "Hotel request saved successfully")

                if car_form.is_valid():
                    car = car_form.save(commit=False)
                    car.travel_header = travel_header
                    car.save()
                if visa_form.is_valid():
                    visa = visa_form.save(commit=False)
                    visa.travel_header = travel_header
                    visa.save()
                if forex_form.is_valid():
                    forex = forex_form.save(commit=False)
                    forex.travel_header = travel_header
                    forex.save()
            else:
                messages.error(request, "Flight form is not valid. Please check your input.")
                print(flight_form.errors)
        else:
            messages.error(request, "Header form is not valid. Please check your input.")
    else:
        header_form = Travelrequestheaderform()
        flight_form = Travelflightdetailsform()
        hotel_form = Travelhoteldetailsform()
        car_form = Travelcarbookingdetailsform()
        visa_form = TravelVisaForm()
        forex_form = TravelForexForm()
        multicity_formset = MulticityFormSet(prefix='multicity')
        # print(multicity_formset)
        
    return render(request, 'trip.html', {
        'header_form': header_form,
        'flight_form': flight_form,
        'hotel_form': hotel_form,
        'car_form': car_form,
        'visa_form': visa_form,
        'forex_form': forex_form,
        'multicity_formset': multicity_formset,
    })







# def travel(request):
#     MulticityFormSet = formset_factory(Travelflightdetailsform, extra=2)
#     if request.method == 'POST':
#         header_form = Travelrequestheaderform(request.POST)
#         flight_form = Travelflightdetailsform(request.POST)
#         hotel_form = Travelhoteldetailsform(request.POST)
#         car_form = Travelcarbookingdetailsform(request.POST)
#         visa_form = TravelVisaForm(request.POST)
#         forex_form = TravelForexForm(request.POST)
#         multicity_formset = MulticityFormSet(request.POST, prefix='multicity')
#         # print(f"multicity_formset total forms: {multicity_formset.total_form}")
#         # multicity_formset.total_form = int(request.POST.get('multicity-TOTAL_FORMS', 0))

#         print(f"multicity_formset is valid: {multicity_formset.is_valid()}")
#         if not multicity_formset.is_valid():
#             print(f"multicity_formset errors: {multicity_formset.errors}")
#         print(f"trip_id: {header_form}")
    
#         try:
#             with transaction.atomic():
#                 if header_form.is_valid():
#                     travel_header = header_form.save(commit=False)
#                     header_form.save_m2m()
#                     travel_header.THRCREABY = request.user
#                     travel_header.save()
#                     header_form = Travelrequestheaderform()
#                     # print(f"trip_id: {travel_header.THINTRID}")

#                     if flight_form.is_valid():
#                         current_user = request.user
#                         from_location = flight_form.cleaned_data['TFLDFRMPLC']    
#                         to_location = flight_form.cleaned_data['TFLDTOPLC'] 
#                         depart_date = flight_form.cleaned_data['TFLDDTEOFTRV']    
#                         return_date = flight_form.cleaned_data['TFLDRETURN']
#                         booking_type = flight_form.cleaned_data['TFLDTRPTYP']
#                         trip_id = travel_header.THINTRID
#                         trip = Travelrequestheader.objects.get(THINTRID=trip_id)
#                         createdby = current_user
#                         pref = flight_form.cleaned_data['TFLDPREF']
#                         pref_air = flight_form.cleaned_data['TFLDPREFAIR']

#                         add_flight(from_location, to_location, depart_date, return_date, createdby, trip, pref, pref_air, booking_type)
#                         messages.success(request,"Request saved Succesfully")

#                         flight_form = Travelflightdetailsform()
#                     else:
#                         print(flight_form.errors)
#                     # if booking_type == 'Multi-city' and multicity_formset.is_valid():
#                     #     for form in multicity_formset.forms:
#                     #         if form.cleaned_data:
#                     #             flight_form = Travelflightdetailsform(data=form.cleaned_data)
#                     #             if flight_form.is_valid():
#                     #                 flight = flight_form.save(commit=False)
#                     #                 flight.travel_header = travel_header
#                     #                 flight.save()
#                     #             else:
#                     #                 print(flight_form.errors)
#                     # elif booking_type == 'Multi-city' and not multicity_formset.is_valid():
#                     #     print(multicity_formset.errors)
#                     if hotel_form.is_valid():
#                         hotel = hotel_form.save(commit=False)
#                         hotel.travel_header = travel_header
#                         hotel.save()
#                     else:
#                         print(hotel_form.errors)
#                     if car_form.is_valid():
#                         car = car_form.save(commit=False)
#                         car.travel_header = travel_header
#                         car.save()
#                     if visa_form.is_valid():
#                         visa = visa_form.save(commit=False)
#                         visa.travel_header = travel_header
#                         visa.save()
#                     if forex_form.is_valid():
#                         forex = forex_form.save(commit=False)
#                         forex.travel_header = travel_header
#                         forex.save()
#                 else:
#                     print(header_form.errors)
        
#         except Exception as e:
#             print(f"An error occurred while creating trip: {e}")
            
#     else:
#         header_form = Travelrequestheaderform()
#         flight_form = Travelflightdetailsform()
#         hotel_form = Travelhoteldetailsform()
#         car_form = Travelcarbookingdetailsform()
#         visa_form = TravelVisaForm()
#         forex_form = TravelForexForm()
#         multicity_formset = MulticityFormSet(prefix='multicity')
        
#     # print(multicity_formset) 
#     return render(request, 'trip.html', {'header_form': header_form, 'flight_form': flight_form, 'hotel_form': hotel_form, 'car_form': car_form, 'visa_form': visa_form, 'forex_form': forex_form,'multicity_formset': multicity_formset})

# def save_travel_forms(request):
#     if request.method == 'POST':
#         travel_header_form = Travelrequestheaderform(request.POST)
#         flight_form = Travelflightdetailsform(request.POST)
#         hotel_form = Travelhoteldetailsform(request.POST)
#         car_form = Travelcarbookingdetailsform(request.POST)
#         visa_form = TravelVisaForm(request.POST)
#         forex_form = TravelForexForm(request.POST)
        
#         try:
#             with transaction.atomic():  # wrap all database operations in a transaction
#                 if travel_header_form.is_valid(): 
#                     travel_header = travel_header_form.save() # Save the travel_header form first
#                     if flight_form.is_valid():
#                         flight = flight_form.save(commit=False)
#                         flight.travel_header = travel_header
#                         flight.save()
#                     if hotel_form.is_valid():
#                         hotel = hotel_form.save(commit=False)
#                         hotel.travel_header = travel_header
#                         hotel.save()
#                     if car_form.is_valid():
#                         car = car_form.save(commit=False)
#                         car.travel_header = travel_header
#                         car.save()
#                     if visa_form.is_valid():
#                         visa = visa_form.save(commit=False)
#                         visa.travel_header = travel_header
#                         visa.save()
#                     if forex_form.is_valid():
#                         forex = forex_form.save(commit=False)
#                         forex.travel_header = travel_header
#                         forex.save()
#                     return redirect('success')
#                 else:
#                     raise ValueError("Invalid form data.")
        
#         except Exception as e:
#             print(f"An error occurred while creating trip: {e}")
#             return render(request, 'error.html', {'error': str(e)})
            
#     else:
#         travel_header_form = Travelrequestheaderform()
#         flight_form = Travelflightdetailsform()
#         hotel_form = Travelhoteldetailsform()
#         car_form = Travelcarbookingdetailsform()
#         visa_form = TravelVisaForm()
#         forex_form = TravelForexForm()
        
#     return render(request, 'trip.html', {'travel_header_form': travel_header_form, 'flight_form': flight_form, 'hotel_form': hotel_form, 'car_form': car_form, 'visa_form': visa_form, 'forex_form': forex_form})


def travel_details(req):
    ctx ={}
    form = TravelDetailsform(req.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.TDCREABY = req.user
        obj.save()
        print(req.user)
        messages.success(req,"Trip Saved")
        print("Saved")
        form = TravelDetailsform()
    else:
        print(form.errors)
    td = TravelDetails.objects.all()
    ctx={
        'form':form,
        'td':td
    }
    return render(req, "trip.html", ctx)

def travel_visa(req):
    ctx ={}
    form = TravelVisaForm(req.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.TVDCREABY = req.user
        obj.save()
        print(req.user)
        messages.success(req,"Visa Request Saved")
        print("Saved")
        form = TravelVisaForm()
    else:
        print(form.errors)
    vd = Travelvisadetails.objects.all()
    ctx={
        'form':form,
        'vd':vd
    }
    return render(req, "trip.html", {'vform': form,'vd':vd})

# def flight(request):
#     ctx ={}
#     form = Travelflightdetailsform(request.POST or None)
#     if form.is_valid():
#         print("valid")      
#         obj = form.save()
#         obj.TFLDCREABY = request.user
#         obj.save()
#         print(request.user)
#         messages.success(request,"Details added")
#         print("Saved")
#         form = Travelflightdetailsform()
#     else:
#         print(form.errors)
#     ctx={
#         'tform':form
#     }
#     return render(request, "trip.html", ctx)