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
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


def mylogout(request):
    logout(request)
    return redirect('/login')

# from Travel.forms import CreateUserform
class SignUpView(SuccessMessageMixin,CreateView):
    model = MyUser
    form_class = MyUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('SignIn')
    success_message = 'signed up successfully'


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required(redirect_field_name='next',login_url='/login')
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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(redirect_field_name='next',login_url='/login')
def home(request):
    return render(request,"home.html")

# def view_trip(request):
#     return render(request,"view_trip.html")

# def view_trip_details(request):
#     return render(request,"view_trip_details.html")

def flight_edit(request):
    return render(request,"flight_edit.html")


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


# def view_trip(request):
#     form_data = Travelrequestheader.objects.all()
#     # Get the filter values from the GET parameters
#     thintrid = request.GET.get('thintrid', '')
#     thproj = request.GET.get('thproj', '')
#     thtrvtyp = request.GET.get('thtrvtyp', '')

#     # Apply filtering based on the provided values
#     if thintrid:
#         form_data = form_data.filter(THINTRID=thintrid)
#     if thproj:
#         form_data = form_data.filter(THPROJ__icontains=thproj)
#     if thtrvtyp:
#         form_data = form_data.filter(THTRVTYP__icontains=thtrvtyp)

#     items_per_page = 10
#     paginator = Paginator(form_data, items_per_page)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'view_trip.html', {'page_obj': page_obj})

@login_required
def view_trip(request):
    form_data = Travelrequestheader.objects.filter(THRCREABY_id=request.user.id)
    # Rest of the code remains the same
    thintrid = request.GET.get('thintrid', '')
    thproj = request.GET.get('thproj', '')
    thtrvtyp = request.GET.get('thtrvtyp', '')

    # Apply filtering based on the provided values
    if thintrid:
        form_data = form_data.filter(THINTRID=thintrid)
    if thproj:
        form_data = form_data.filter(THPROJ__icontains=thproj)
    if thtrvtyp:
        form_data = form_data.filter(THTRVTYP__icontains=thtrvtyp)

    items_per_page = 10
    paginator = Paginator(form_data, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'view_trip.html', {'page_obj': page_obj})



def trip_details(request, trip_id):
    trip = get_object_or_404(Travelrequestheader, THINTRID=trip_id)
    # print(trip)
    flights = Travelflightdetails.objects.filter(TFLDTRPNAME=trip)
    # print(flights)
    hotels = Travelhoteldetails.objects.filter(THDTRHINTRID=trip)
    cars = Travelcarbookingdetails.objects.filter(TCBDTHID=trip)
    visas = Travelvisadetails.objects.filter(TVDTRAVEL=trip)
    forex = Travelforexdetails.objects.filter(TFDTRVTID=trip)

    return render(request, 'view_trip_details.html', {
        'trip': trip,
        'flights': flights,
        'hotels': hotels,
        'cars': cars,
        'visas': visas,
        'forex': forex,
    })


def add_flight_list(request, trip_id):
    # print("trip_id:", trip_id)
    if request.method == 'POST':    
        form = Travelflightdetailsform(request.POST)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.TFLDTRPNAME_id = trip_id
            flight.TFLDCREABY_id = request.user.id
            flight.save()
            return redirect('trip_details', trip_id=trip_id)
    else:
        form = Travelflightdetailsform()
        print(form.errors)
    return render(request, 'flight_add.html', {'form': form})


def edit_flight(request, flight_id):
    flight = get_object_or_404(Travelflightdetails, TFLDINTRID=flight_id)
    
    if request.method == 'POST':
        form = Travelflightdetailsform(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            trip_id = flight.TFLDTRPNAME_id
            # messages.success(request,"Details updated")
            return redirect('trip_details', trip_id=trip_id) 
        else:
            print(form.errors)
    else:
        form = Travelflightdetailsform(instance=flight)
    return render(request, 'flight_edit.html', {'form': form})

def delete_flight(request, flight_id):
    flight = Travelflightdetails.objects.get(TFLDINTRID=flight_id)
    if request.method == 'POST':
        # Delete the flight object
        flight.delete()
        return redirect('trip_details', trip_id=flight.TFLDTRPNAME.THINTRID)
    return render(request, 'view_trip_details.html', {'flight': flight})

def add_hotel_list(request, trip_id):
    # print("trip_id:", trip_id)
    if request.method == 'POST':    
        form = Travelhoteldetailsform(request.POST)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.THDTRHINTRID_id = trip_id
            hotel.THDCREABY_id = request.user.id
            hotel.save()
            return redirect('trip_details', trip_id=trip_id)
    else:
        form = Travelhoteldetailsform()
        print(form.errors)
    return render(request, 'hotel_add.html', {'form': form})

def edit_hotel(request, hotel_id):
    hotel = get_object_or_404(Travelhoteldetails, THDINTRID=hotel_id)
    
    if request.method == 'POST':
        form = Travelhoteldetailsform(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            # messages.success(request,"Details updated")
            trip_id = hotel.THDTRHINTRID_id
            return redirect('trip_details', trip_id=trip_id) 
        else:
            print(form.errors)
    else:
        form = Travelhoteldetailsform(instance=hotel)
    return render(request, 'hotel_edit.html', {'form': form})


def delete_hotel(request, hotel_id):
    hotel = Travelhoteldetails.objects.get(THDINTRID=hotel_id)
    if request.method == 'POST':
        hotel.delete()
        return redirect('trip_details', trip_id=hotel.THDTRHINTRID.THINTRID)
    return render(request, 'view_trip_details.html', {'hotel': hotel})

def add_car_list(request, trip_id):
    # print("trip_id:", trip_id)
    if request.method == 'POST':    
        form = Travelcarbookingdetailsform(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.TCBDTHID_id = trip_id
            car.TCBDCREABY_id = request.user.id
            car.save()
            return redirect('trip_details', trip_id=trip_id)
    else:
        form = Travelcarbookingdetailsform()
        print(form.errors)
    return render(request, 'car_add.html', {'form': form})

def edit_car(request, car_id):
    car = get_object_or_404(Travelcarbookingdetails, TCBDINTID=car_id)
    
    if request.method == 'POST':
        form = Travelcarbookingdetailsform(request.POST, instance=car)
        if form.is_valid():
            form.save()
            # messages.success(request,"Details updated")
            trip_id = car.TCBDTHID_id
            return redirect('trip_details', trip_id=trip_id) 
        else:
            print(form.errors)
    else:
        form = Travelcarbookingdetailsform(instance=car)
    return render(request, 'car_edit.html', {'form': form})

def delete_car(request, car_id):
    car = Travelcarbookingdetails.objects.get(TCBDINTID=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('trip_details', trip_id=car.TCBDTHID.THINTRID)
    print(f"{car.TCBDTHID.THINTRID}")
    return render(request, 'view_trip_details.html', {'car': car})

def add_visa_list(request, trip_id):
    # print("trip_id:", trip_id)
    if request.method == 'POST':    
        form = TravelVisaForm(request.POST)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.TVDTRAVEL_id = trip_id
            flight.TVDCREABY_id = request.user.id
            flight.save()
            return redirect('trip_details', trip_id=trip_id)
    else:
        form = TravelVisaForm()
        print(form.errors)
    return render(request, 'visa_add.html', {'form': form})

def edit_visa(request, visa_id):
    visa = get_object_or_404(Travelvisadetails, TVDINTRID=visa_id)
    
    if request.method == 'POST':
        form = TravelVisaForm(request.POST, instance=visa)
        if form.is_valid():
            form.save()
            # messages.success(request,"Details updated")
            trip_id = visa.TVDTRAVEL_id
            return redirect('trip_details', trip_id=trip_id) 
        else:
            print(form.errors)
    else:
        form = TravelVisaForm(instance=visa)
    return render(request, 'visa_edit.html', {'form': form})

def delete_visa(request, visa_id):
    visa = Travelvisadetails.objects.get(TVDINTRID=visa_id)
    if request.method == 'POST':
        # Delete the flight object
        visa.delete()
        return redirect('trip_details', trip_id=visa.TVDTRAVEL.THINTRID)
    # print(f"{visa.TVDTRAVEL.THINTRID}")
    return render(request, 'view_trip_details.html', {'visa': visa})

def add_forex_list(request, trip_id):
    # print("trip_id:", trip_id)
    if request.method == 'POST':    
        form = TravelForexForm(request.POST)
        if form.is_valid():
            forex = form.save(commit=False)
            forex.TFDTRVTID_id = trip_id
            forex.TFODCREABY_id = request.user.id
            forex.save()
            return redirect('trip_details', trip_id=trip_id)
    else:
        form = TravelForexForm()
        print(form.errors)
    return render(request, 'forex_add.html', {'form': form})

def edit_forex(request, forex_id):
    forex = get_object_or_404(Travelforexdetails, TFDINTRID=forex_id)
    
    if request.method == 'POST':
        form = TravelForexForm(request.POST, instance=forex)
        if form.is_valid():
            form.save()
            # messages.success(request,"Details updated")
            trip_id = forex.TFDTRVTID_id
            return redirect('trip_details', trip_id=trip_id) 
        else:
            print(form.errors)
    else:
        form = TravelForexForm(instance=forex)
    return render(request, 'forex_edit.html', {'form': form})

def delete_forex(request, forex_id):
    forex = Travelforexdetails.objects.get(TFDINTRID=forex_id)
    if request.method == 'POST':
        # Delete the flight object
        forex.delete()
        return redirect('trip_details', trip_id=forex.TFDTRVTID.THINTRID)
    return render(request, 'view_trip_details.html', {'forex': forex})



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


def add_hotel(room_type, checkin_date, checkout_date, pref_hotel, city,createdby, htrip):
    try:
        hotel = Travelhoteldetails(
            THDCHKINDTE=checkin_date,
            THDCHKOTDTE=checkout_date,
            THDCITY=city,
            THDCREABY=createdby,
            THDTRHINTRID=htrip,
            THDPREFHOTL=pref_hotel,
            THDHTYPE=room_type
        )
        hotel.save()
        print("hotelsaved")
        return [hotel]
    except Exception as e:
        print(f"An error occurred while adding hotel details: {e}")

def add_car(car_type, car_from, car_to, car_pickup, car_drop,car_createdby, ctrip):
    try:
        car = Travelcarbookingdetails(
            TCBDFRLOC=car_from,
            TCBDTOLOC=car_to,
            TCBDPIKU=car_pickup,
            TCBDDROP=car_drop,
            TCBDCREABY=car_createdby,
            TCBDTHID=ctrip,
            TCBDCTYP=car_type,

        )
        car.save()
        print("carsaved")
        return [car]
    except Exception as e:
        print(f"An error occurred while adding car details: {e}")

def add_visa(travel_date, visiting_country, fees, remarks,visa_createdby, visa_type,vtrip):
    try:
        visa = Travelvisadetails(
            TVDTRAVDTE=travel_date,
            TVDVISTGCOUN=visiting_country,
            TVDVSAFES=fees,
            TVDREMK=remarks,
            TVDTRAVEL=vtrip,
            TVDCREABY=visa_createdby,
            TVDVISTYPE=visa_type
        )
        visa.save()
        print("visasaved")
        return [visa]
    except Exception as e:
        print(f"An error occurred while adding visa details: {e}")


def add_forex(forex_type, forext_date, amount, currency, remarks,forex_createdby, ftrip):
    try:
        forex = Travelforexdetails(
            TFDCSHTYPE=forex_type,
            TFDTRAVDTE=forext_date,
            TFDAMNT=amount,
            TFODCREABY=forex_createdby,
            TFDTRVTID=ftrip,
            TFDCURR=currency,
            TFDREMARK=remarks
        )
        forex.save()
        print("forexsaved")
        return [forex]
    except Exception as e:
        print(f"An error occurred while adding forex details: {e}")



# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required(redirect_field_name='next',login_url='/mylogin')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(redirect_field_name='next',login_url='/login')
def travel(request):
    MulticityFormSet = formset_factory(MulticityForm)
    MultiHotelFormSet = formset_factory(Travelhoteldetailsform)
    MultiCarFormSet = formset_factory(Travelcarbookingdetailsform)
    MultiVisaFormSet = formset_factory(TravelVisaForm)
    MulfiForexFormSet = formset_factory(TravelForexForm)

    
    if request.method == 'POST':
        if 'radio_button' in request.POST and request.POST['radio_button'] == 'on':
            flight_form = None
        else:
            flight_form = Travelflightdetailsform(request.POST)

        if 'hotel_radio_button' in request.POST and request.POST['hotel_radio_button'] == 'on':
            hotel_form = None
        else:
            hotel_form = Travelhoteldetailsform(request.POST)

        if 'car_radio_button' in request.POST and request.POST['car_radio_button'] == 'on':
            car_form = None
        else:
            car_form = Travelcarbookingdetailsform(request.POST)

        if 'visa_radio_button' in request.POST and request.POST['visa_radio_button'] == 'on':
            visa_form = None
        else:
            visa_form = TravelVisaForm(request.POST)

        if 'forex_radio_button' in request.POST and request.POST['forex_radio_button'] == 'on':
            forex_form = None
        else:
            forex_form = TravelForexForm(request.POST)

        header_form = Travelrequestheaderform(request.POST)
        # flight_form = Travelflightdetailsform(request.POST)
        # hotel_form = Travelhoteldetailsform(request.POST)
        # car_form = Travelcarbookingdetailsform(request.POST)
        # visa_form = TravelVisaForm(request.POST)
        # forex_form = TravelForexForm(request.POST)
        multicity_formset = MulticityFormSet(request.POST, prefix='multicity')
        multihotel_formset = MultiHotelFormSet(request.POST, prefix='multihotel')
        multicar_formset = MultiCarFormSet(request.POST, prefix='multicar')
        multivisa_formset = MultiVisaFormSet(request.POST, prefix='multivisa')
        multiforex_formset = MulfiForexFormSet(request.POST, prefix='multiforex')

        if header_form.is_valid():
            travel_header = header_form.save(commit=False)
            header_form.save_m2m()
            travel_header.THRCREABY = request.user
            travel_header.save()
            header_form = Travelrequestheaderform()

            # Get the radio button value
            # radio_button = request.POST.get('radio_button')

            # # If radio button is checked, set not_required to True, otherwise False
            # not_required = True if radio_button == 'on' else False

            # # Set required field based on checkbox
            # flight_form.fields['TFLDFRMPLC'].required = not not_required
            # flight_form.fields['TFLDTOPLC'].required = not not_required
            # flight_form.fields['TFLDDTEOFTRV'].required = not not_required
            if flight_form is not None and flight_form.is_valid():
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
                    # flight_form.fields['TFLDRETURN'].required = True
                     # here
                    if booking_type == 'Multi-city':
                        # if not any(form.cleaned_data for form in multicity_formset.forms):
                        # if not any(hasattr(form, 'cleaned_data') and form.cleaned_data for form in multicity_formset.forms):
                            # messages.error(request, 'Please provide multi-city flight details or delete section')
                        if multicity_formset.is_valid():
                            for form in multicity_formset:
                                form.fields['TFLDDTEOFTRV'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')

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
                    messages.success(request, "Flight request saved successfully", extra_tags="flight_form_success")
                    flight_form = Travelflightdetailsform()
            else:
                messages.error(request, "Flight form is not valid. Please check your input.")
                # print(flight_form.errors)
                
            if hotel_form is not None and hotel_form.is_valid():
                    print('hotel_form')
                    # radio_button = request.POST.get('hotel_radio_button')
                    # # If radio button is checked, set not_required to True, otherwise False
                    # not_required = True if radio_button == 'on' else False
                    # # Set required field based on checkbox
                    # hotel_form.fields['THDCHKINDTE'].required = not not_required
                    # hotel_form.fields['THDCHKOTDTE'].required = not not_required
                    # hotel_form.fields['THDCITY'].required = not not_required

                    trip_id = travel_header.THINTRID
                    htrip = Travelrequestheader.objects.get(THINTRID=trip_id)
                    createdby = request.user
                    checkin_date = hotel_form.cleaned_data['THDCHKINDTE']
                    checkout_date = hotel_form.cleaned_data['THDCHKOTDTE']
                    room_type = hotel_form.cleaned_data['THDHTYPE']
                    pref_hotel = hotel_form.cleaned_data['THDPREFHOTL'] 
                    city = hotel_form.cleaned_data['THDCITY']
                    add_hotel(room_type, checkin_date, checkout_date, pref_hotel, city, createdby,htrip)
                    messages.success(request, "Hotel Request saved successfully", extra_tags="hotel_form_success") 
                    hotel_form = Travelhoteldetailsform()

                    if multihotel_formset.is_valid():
                            print("multihotel_formset")
                            for i, form in enumerate(multihotel_formset.forms):
                                # print(form)
                                if form.cleaned_data:
                                    print('cleaned')
                                    checkin_date = form.cleaned_data.get('THDCHKINDTE')
                                    # print(checkin_date)
                                    checkout_date = form.cleaned_data.get('THDCHKOTDTE')
                                    room_type = form.cleaned_data.get('THDHTYPE')
                                    city = form.cleaned_data.get('THDCITY')
                                    pref_hotel = form.cleaned_data.get('THDPREFHOTL')

                                    if checkin_date < date.today():
                                        print('innerif')
                                        messages.error(request, 'Check-in date cannot be in the past')
                                    elif checkout_date < date.today():
                                        print('innerelif1')
                                        messages.error(request, 'Check-out date cannot be in the past')
                                    else: 
                                        print("mulhot")
                                        multi_hotel = form.save(commit=False)
                                        multi_hotel.THDCHKINDTE = checkin_date  
                                        print(checkin_date)
                                        multi_hotel.THDCHKOTDTE = checkout_date
                                        multi_hotel.THDHTYPE = room_type
                                        multi_hotel.THDCITY = city
                                        multi_hotel.THDCREABY = createdby
                                        multi_hotel.THDTRHINTRID = htrip
                                        multi_hotel.THDPREFHOTL = pref_hotel
                                        add_hotel(room_type, checkin_date, checkout_date, pref_hotel, city, createdby,htrip)
                                        messages.success(request, "Multi-hotel details saved successfully", extra_tags="hotel_form_success")
                    else:
                        messages.error(request, "Multi-hotel formset is not valid. Please check your input.")
            else:
                messages.error(request, "Hotel form is not valid. Please check your input.")
                # print(hotel_form.errors)
                print('hotel_not_valid')

            if car_form is not None and car_form.is_valid():
                    print("car_form")

                    trip_id = travel_header.THINTRID
                    ctrip = Travelrequestheader.objects.get(THINTRID=trip_id)
                    car_createdby = request.user
                    car_from = car_form.cleaned_data['TCBDFRLOC']
                    print(car_form.errors)
                    car_to = car_form.cleaned_data['TCBDTOLOC']
                    car_pickup = car_form.cleaned_data['TCBDPIKU']
                    car_drop = car_form.cleaned_data['TCBDDROP']
                    car_type = car_form.cleaned_data['TCBDCTYP']

                    add_car(car_type, car_from, car_to, car_pickup, car_drop,car_createdby, ctrip)
                    messages.success(request, "Car Request saved successfully",extra_tags="car_form_success")
                    car_form = Travelcarbookingdetailsform()
                    
                    # if not any(form.cleaned_data for form in multicar_formset.forms):
                    # if not any(form.is_valid() and form.cleaned_data for form in multicar_formset.forms):
                    #         messages.error(request, 'Please provide multi-city flight details or delete section')
                    if multicar_formset.is_valid():
                            print("car_valid")
                            for i, form in enumerate(multicar_formset.forms):
                                # print(form)
                                if form.cleaned_data:
                                    print('cleaned')
                                    car_pickup = form.cleaned_data.get('TCBDPIKU')
                                    # print(car_pickup)
                                    car_drop = form.cleaned_data.get('TCBDDROP')
                                    car_type = form.cleaned_data.get('TCBDCTYP')
                                    car_from = form.cleaned_data.get('TCBDFRLOC')
                                    car_to = form.cleaned_data.get('TCBDTOLOC')

                                    print(car_type)

                                    city = form.cleaned_data.get('THDCITY')
                                    # pref_hotel = form.cleaned_data.get('THDPREFHOTL')

                                    if car_pickup < date.today():
                                        print('innerif')
                                        messages.error(request, 'Check-in date cannot be in the past')
                                    elif car_drop < date.today():
                                        print('innerelif1')
                                        messages.error(request, 'Check-out date cannot be in the past')
                                    else: 
                                        print("multi_car")
                                        multi_car = form.save(commit=False)
                                        multi_car.TCBDPIKU = car_pickup  
                                        print(car_pickup)
                                        multi_car.TCBDDROP = car_drop
                                        multi_car.TCBDCTYP = car_type
                                        multi_car.TCBDFLOC = car_from
                                        multi_car.TCBDTLOC = car_to
                                        multi_car.TCBDCREABY = car_createdby
                                        multi_car.TCBDTHID = ctrip
                                        add_car(car_type, car_from, car_to, car_pickup, car_drop,car_createdby, ctrip)
                                        messages.success(request, "Multi-hotel details saved successfully")
                    else:
                        messages.error(request, "Multi-hotel formset is not valid. Please check your input.")
            else:
                messages.error(request, "Car form is not valid. Please check your input.")
                # print(car_form.errors)

            if visa_form is not None and visa_form.is_valid():
                    print("visa_form")

                    trip_id = travel_header.THINTRID
                    vtrip = Travelrequestheader.objects.get(THINTRID=trip_id)
                    visa_createdby = request.user
                    travel_date = visa_form.cleaned_data['TVDTRAVDTE']
                    visiting_country = visa_form.cleaned_data['TVDVISTGCOUN']
                    fees = visa_form.cleaned_data['TVDVSAFES']
                    remarks = visa_form.cleaned_data['TVDREMK']
                    visa_type = visa_form.cleaned_data['TVDVISTYPE']
                    add_visa(travel_date, visiting_country, fees, remarks,visa_createdby, visa_type,vtrip)
                    messages.success(request, "Visa Request saved successfully",extra_tags="visa_form_success") 
                    visa_form = TravelVisaForm()
                    
                    # if not any(form.cleaned_data for form in multivisa_formset.forms):
                    #         messages.error(request, 'Please provide multi-city flight details or delete section')
                    if multivisa_formset.is_valid():
                            print("visa_true")
                            for i, form in enumerate(multivisa_formset.forms):
                                # print(form)
                                if form.cleaned_data:
                                    travel_date = form.cleaned_data.get('TVDTRAVDTE')
                                    print(travel_date)
                                    visa_type = form.cleaned_data.get('TVDVISTYPE')
                                    fees = form.cleaned_data.get('TVDVSAFES')
                                    remarks = form.cleaned_data.get('TVDREMK')
                                    visiting_country = form.cleaned_data.get('TVDVISTGCOUN')


                                    if travel_date < date.today():
                                        messages.error(request, 'Travel date cannot be in the past')
                                    else: 
                                        multi_visa = form.save(commit=False)
                                        multi_visa.TVDTRAVDTE = travel_date
                                        print(travel_date)
                                        multi_visa.TVDVISTGCOUN = visiting_country
                                        multi_visa.TVDVISTYPE = visa_type
                                        multi_visa.TVDVSAFES = fees
                                        multi_visa.TVDCREABY = visa_createdby
                                        multi_visa.TVDTRAVEL = vtrip
                                        multi_visa.TVDREMK = remarks

                                        add_visa(travel_date, visiting_country, fees, remarks,visa_createdby, visa_type,vtrip)
                                        messages.success(request, "Multi-hotel details saved successfully")
                    else:
                        for form in multivisa_formset:
                            if form.errors:
                                print(form.errors)
                        messages.error(request, "Multi-hotel formset is not valid. Please check your input.")
            else:
                messages.error(request, "Visa form is not valid. Please check your input.")
                
            if forex_form is not None and forex_form.is_valid():
                    print("forex_form")

                    trip_id = travel_header.THINTRID
                    ftrip = Travelrequestheader.objects.get(THINTRID=trip_id)
                    forex_createdby = request.user
                    forext_date = forex_form.cleaned_data['TFDTRAVDTE']
                    amount = forex_form.cleaned_data['TFDAMNT']
                    remarks = forex_form.cleaned_data['TFDREMARK']
                    forex_type = forex_form.cleaned_data['TFDCSHTYPE']
                    currency = forex_form.cleaned_data['TFDCURR']
                    add_forex(forex_type, forext_date, amount, currency, remarks,forex_createdby, ftrip)
                    messages.success(request, "Forex Request saved successfully",extra_tags="forex_form_success") 
                    forex_form = TravelForexForm()
                    
                    # if not any(form.cleaned_data for form in multiforex_formset.forms):
                    #         messages.error(request, 'Please provide multi-city flight details or delete section')
                    if multiforex_formset.is_valid():
                            print("visa_true")
                            for i, form in enumerate(multiforex_formset.forms):
                                # print(form)
                                if form.cleaned_data:
                                    forext_date = form.cleaned_data.get('TFDTRAVDTE')
                                    print(forext_date)
                                    forex_type = form.cleaned_data.get('TFDCSHTYPE')
                                    amount = form.cleaned_data.get('TFDAMNT')
                                    remarks = form.cleaned_data.get('TFDREMARK')
                                    currency = form.cleaned_data.get('TFDCURR')
                                    print(currency)


                                    if forext_date < date.today():
                                        messages.error(request, 'Travel date cannot be in the past')
                                    else: 
                                        multi_forex = form.save(commit=False)
                                        multi_forex.TFDTRAVDTE = forext_date
                                        print(forext_date)
                                        multi_forex.TFDCSHTYPE = forex_type
                                        multi_forex.TFDAMNT = amount
                                        multi_forex.TFODCREABY = forex_createdby
                                        multi_forex.TFDTRVTID = ftrip 
                                        multi_forex.TFDCURR = currency
                                        multi_forex.TFDREMARK = remarks
                                        print(currency)

                                        add_forex(forex_type, forext_date, amount, currency, remarks,forex_createdby, ftrip)
                                        messages.success(request, "Multi-forex details saved successfully")
                    else:
                        for form in multiforex_formset:
                            if form.errors:
                                print(form.errors)
                        messages.error(request, "Multi-hotel formset is not valid. Please check your input.")
        else:
            messages.error(request, "Header form is not valid. Please check your input.", extra_tags='header_form_error')
    else:
        header_form = Travelrequestheaderform()
        flight_form = Travelflightdetailsform()
        hotel_form = Travelhoteldetailsform()
        car_form = Travelcarbookingdetailsform()
        visa_form = TravelVisaForm()
        forex_form = TravelForexForm()
        multicity_formset = MulticityFormSet(prefix='multicity')
        multihotel_formset = MultiHotelFormSet(prefix='multihotel')
        multicar_formset = MultiCarFormSet(prefix='multicar')
        multivisa_formset = MultiVisaFormSet(prefix='multivisa')
        multiforex_formset = MulfiForexFormSet(prefix='multiforex')



        # print(multicity_formset)
        
    return render(request, 'trip.html', {
        'header_form': header_form,
        'flight_form': flight_form,
        'hotel_form': hotel_form,
        'car_form': car_form,
        'visa_form': visa_form,
        'forex_form': forex_form,
        'multicity_formset': multicity_formset,
        'multihotel_formset': multihotel_formset,
        'multicar_formset':multicar_formset,
        'multivisa_formset':multivisa_formset,
        'multiforex_formset':multiforex_formset,


    })


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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(redirect_field_name='next',login_url='/login')
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