from datetime import date
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
# from Travel.forms import Grade,Workcenter,Department,Loginform,UserroleModel
# from .models import GradeModel,WorkcenterModel,DepartmentModel,UserroleModel,TitledetailsModel
from .models import *
from django.conf import settings
# from travel.forms import Travelform, Loginform
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.core.paginator import Paginator
from django.db.models import Sum
from django.contrib.auth.forms import AuthenticationForm
# from Travel.forms import Pettycashdetailsform
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
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.views import PasswordResetConfirmView
from django.http import JsonResponse
from django.http import FileResponse
from django.http import HttpResponse
import os
from datetime import datetime, timedelta
from django.core.mail import send_mail




def mylogout(request):
    logout(request)
    return redirect('/login')

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    # template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        print("Form is valid")
        user = form.save()
        user.set_password(form.cleaned_data['new_password1'])
        user.save()
        return super().form_valid(form)

def check_password_expiration(request):
    user = request.user  # Assuming the user is logged in
    pass_date_changed = user.pass_date_changed

    if pass_date_changed is not None:
        # Calculate the date 90 days ago
        ninety_days_ago = timezone.now() - timezone.timedelta(days=1)

        if pass_date_changed < ninety_days_ago:
            # Password has expired, redirect to the "password_exp.html" page
            return render(request, 'password_exp.html')

# def send_password_change_email(user):
#     # Get the user's last password change date
#     last_password_change_date = user.pass_date_changed  # You should adjust this field name
#     # Calculate the expiration date (90 days from the last change)
#     expiration_date = last_password_change_date + timedelta(days=1)
#     # Get the current date
#     current_date = datetime.now().date()

#     if current_date > expiration_date:
#         # Send an email to the user
#         subject = 'Change Your Password'
#         message = 'Your password has expired. Please change it immediately.'
#         from_email = 'malikrao14@gmail.com'  # Set your email
#         recipient_list = [user.email]

#         send_mail(subject, message, from_email, recipient_list)


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

def trip_app(request):
    return render(request,"trip_app.html")

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

# def travel_app(request):
#     return render(request,"travel_app.html")

# def travel_app(request):
#     logged_in_user = request.user

#     assigned_profile = AssignProfileModel.objects.filter(TPFAEMPID=logged_in_user).first()

#     if assigned_profile:
#         # Get the approver details based on the assigned profile
#         profile_internal_id = assigned_profile.TPFAPRNAME_id
#         approver_details = ProfileModel.objects.get(TPFCINTID=profile_internal_id)
#         # approver_id = approver_details.TPFCMANID_id
#         # sequence = approver_details.TPFCLSEQ

#         trips = Travelrequestheader.objects.filter(
#             THTASTATUS=2,  # Filter based on the 'Applied' status
#         )

#         return render(request, 'travel_app.html', {'trips': trips})
#     return render(request, 'travel_app.html', {'trips': []})



# def travel_app(request):
#     logged_in_user = request.user

#     assigned_profile = AssignProfileModel.objects.filter(TPFAEMPID=logged_in_user).first()

#     if assigned_profile:
#         # Get the approver details based on the assigned profile
#         approver_profile = ProfileModel.objects.get(TPFCINTID=assigned_profile.TPFAPRNAME_id)

#         # Check if the logged-in user is the approver
#         if logged_in_user == approver_profile.TPFCMANID:
#             # Fetch trips based on conditions
#             trips = Travelrequestheader.objects.filter(
#                 THTASTATUS=2,  # Filter based on the 'Approved' status
#                 THRCREABY=logged_in_user,  # Additional condition for the logged-in user
#             )

#             return render(request, 'travel_app.html', {'trips': trips})

#     return render(request, 'travel_app.html', {'trips': []})

# def travel_app(request):
#     logged_in_user = request.user

#     assigned_profile = AssignProfileModel.objects.filter(TPFAEMPID=logged_in_user).first()

#     if assigned_profile:
#         try:
#             # Get the approver details based on the assigned profile
#             approver_profile = ProfileModel.objects.get(TPFCINTID=assigned_profile.TPFAPRNAME_id)

#             # Check if the logged-in user is the approver and has sequence 1
#             if logged_in_user == approver_profile.TPFCMANID and approver_profile.TPFCLSEQ == 1:
#                 print("Condition met: Logged in user is the approver with sequence 1")

#                 # Fetch trips based on conditions
#                 trips = Travelrequestheader.objects.filter(
#                     THTASTATUS=2,  # Filter based on the 'Approved' status
#                     THPROJ__PMSTUS='Active',  # Additional condition for Project status
#                 )

#                 return render(request, 'travel_app.html', {'trips': trips})

#         except ProfileModel.DoesNotExist:
#             # Handle the case where no profile is found for the assigned profile
#             print("ProfileModel.DoesNotExist: No profile found for the assigned profile.")
#         except Exception as e:
#             # Handle other exceptions and print the details for debugging
#             print(f"An error occurred: {str(e)}")

#     return render(request, 'travel_app.html', {'trips': []})

# def travel_app(request):
#     logged_in_user = request.user

#     try:
#         # Get the user who created the Travelrequestheader
#         created_user_id = Travelrequestheader.objects.filter().values_list('THRCREABY_id', flat=True).first()
#         print(f"created_user_id: {created_user_id}")
        
#         # Get the profile assigned to the user who created the Travelrequestheader
#         created_user_profile = get_object_or_404(AssignProfileModel, TPFAEMPID_id=created_user_id)
#         print(f"created_user_profile: {created_user_profile}")
        
#         # Follow the relationship to get the approver details
#         approver_profile = created_user_profile.TPFAPRNAME
#         print(f"approver_profile: {approver_profile}")

#         if logged_in_user == approver_profile.TPFCMANID and approver_profile.TPFCLSEQ == 1:
#             # Fetch trips based on conditions
#             trips = Travelrequestheader.objects.filter(
#                 THTASTATUS=2,  # Filter based on the 'Approved' status
#                 THPROJ__PMSTUS='Active',  # Additional condition for Project status
#             )

#             return render(request, 'travel_app.html', {'trips': trips})
#         else:
#             return render(request, 'travel_app.html', {'trips': []})
#     except AssignProfileModel.DoesNotExist:
#         return render(request, 'travel_app.html', {'trips': []})
    
# def travel_app(request):
#     logged_in_user = request.user

#     try:
#         # Get all Travelrequestheader records
#         travel_headers = Travelrequestheader.objects.all()

#         for travel_header in travel_headers:
#             # Get the user who created the Travelrequestheader
#             created_user_id = travel_header.THRCREABY_id
#             print(f"created_user_id: {created_user_id}")

            
#             # Get the profile assigned to the user who created the Travelrequestheader
#             created_user_profile = get_object_or_404(AssignProfileModel, TPFAEMPID_id=created_user_id)
#             print(f"created_user_profile: {created_user_profile}")
            
#             # Follow the relationship to get the approver details
#             approver_profile = created_user_profile.TPFAPRNAME
#             print(f"approver_profile: {approver_profile}")

#             # Check conditions
#             if logged_in_user == approver_profile.TPFCMANID and approver_profile.TPFCLSEQ == 1:
#                 # Fetch trips based on conditions
#                 trips = Travelrequestheader.objects.filter(
#                     THTASTATUS=2,  # Filter based on the 'Approved' status
#                     THPROJ__PMSTUS='Active',  # Additional condition for Project status
#                 )

#                 return render(request, 'travel_app.html', {'trips': trips})

#         # If no matching records are found, return an empty list
#         return render(request, 'travel_app.html', {'trips': []})

#     except AssignProfileModel.DoesNotExist:
#         return render(request, 'travel_app.html', {'trips': []})

def travel_app(request):
    logged_in_user = request.user

    try:
        travel_headers = Travelrequestheader.objects.filter(THTASTATUS=2)
        matching_trips = []

        for travel_header in travel_headers:
            # Get the user who created the Travelrequestheader
            created_user = travel_header.THRCREABY

            # Get all profiles assigned to the user who created the Travelrequestheader
            created_user_profiles = AssignProfileModel.objects.filter(TPFAEMPID=created_user)

            # Follow the relationship to get the approver details
            for created_user_profile in created_user_profiles:
                approver_profile = created_user_profile.TPFAPRNAME

                # Check conditions
                if logged_in_user == approver_profile.TPFCMANID and approver_profile.TPFCLSEQ == 1:
                    matching_trips.append(travel_header)

        # Render the template with matching trips
        return render(request, 'travel_app.html', {'trips': matching_trips})

    except AssignProfileModel.DoesNotExist:
        return render(request, 'travel_app.html', {'trips': []})



# def dashboard(request):
#     return render(request,"dashboard.html")

# def dashboard(request):
#     print("User Role:", request.user.role)
#     user_role_id = request.user.role_id if request.user.role else None
#     user_div_assignments = Divassignmentuser.objects.filter(DIVASSUURROLTLE=user_role_id).order_by('DIVASSUSEQ')
#     div_master_data = DivmasterModel.objects.all()
#     context = {
#         'user_div_assignments': user_div_assignments,
#         'div_master_data': div_master_data,
#     }
#     return render(request, "dashboard.html", context)

def dashboard(request):
    print("User Role:", request.user.role)
    user_role_id = request.user.role_id if request.user.role else None
    user_div_assignments = Divassignmentuser.objects.filter(DIVASSUURROLTLE=user_role_id).order_by('DIVASSUSEQ')
    div_master_data = DivmasterModel.objects.all()

    for div_assignment in user_div_assignments:
        div_instance = div_assignment.DIVASSUDIVMID
        div_instance.tile_auth_details = div_instance.tileautherizationdetails_set.all()

    context = {
        'user_div_assignments': user_div_assignments,
        'div_master_data': div_master_data,
    }
    return render(request, "dashboard.html", context)



def emp(request):
    return render(request,"emp.html")

# class SignUpView(SuccessMessageMixin,CreateView):
#     model = MyUser
#     form_class = MyUserCreationForm
#     template_name = 'emp.html'
#     success_url = reverse_lazy('home')
#     success_message = 'signed up successfully'

def singup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['emp_created_by'] = request.user.id
            form.cleaned_data['emp_mod_by'] = request.user.id
            form.save()
            messages.success(request, 'User created successfully.')
            # Check and send password change email
            # send_password_change_email(user)
            form = MyUserCreationForm()
    else:
        form = MyUserCreationForm()
        for field in form:
            print(field.name, field.errors)
    # context = {
    #     'form': form,
    # }
    search_query = request.GET.get('name_contains')
    if search_query:
        data = MyUser.objects.filter(
            Q(first_name__icontains=search_query) | Q(email__icontains=search_query)
        )
    else:
        data = MyUser.objects.all()

    # data = ProfileModel.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        'page_obj': page_obj,
        'form': form,
    }
    return render(request, 'emp.html', ctx)

def employee_edit(request, pk):
    emp = get_object_or_404(MyUser, pk=pk)
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, instance=emp)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.emp_mod_by = request.user
            obj.emp_mod_on = timezone.now()
            obj.save()
            messages.success(request, "Details updated")
            return redirect('singup')
        else:
            print(form.errors)
    else:
        form = MyUserCreationForm(instance=emp)
    return render(request, "emp_edit.html", {'form': form, 'emp': emp})


# def booking_status_add(request):
#     if request.method == 'POST':
#         form = BookingStatusForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking_status_add')  # Redirect to the same page
#     else:
#         form = BookingStatusForm()
    
#     booking_statuses = BookingStatus.objects.all()
#     return render(request, 'booking_status_add.html', {'form': form, 'booking_statuses': booking_statuses})

def booking_status_add(request):
    ctx ={}
    form = BookingStatusForm(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.status_createdby = request.user
        obj.status_createdon = timezone.now()
        obj.save()
        print(request.user)
        messages.success(request,"Booking Status saved")
        form = BookingStatusForm()
        print("Saved")
    else:
        print(form.errors)

    search_query = request.GET.get('name_contains')
    if search_query:
        data = BookingStatus.objects.filter(
            Q(status__icontains=search_query)
        )
    else:
        data = BookingStatus.objects.all()

    # data = WorkcenterModel.objects.all()
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
    return render(request, "booking_status_add.html", ctx)

def booking_status_edit(request, pk):
    booking_status = get_object_or_404(BookingStatus, pk=pk)

    if request.method == 'POST':
        form = BookingStatusForm(request.POST, instance=booking_status)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.status_modiby = request.user
            obj.status_modon = timezone.now()
            form.save()
            return redirect('booking_status_add')  # Redirect to the same page or desired URL
    else:
        form = BookingStatusForm(instance=booking_status)

    return render(request, 'booking_status_edit.html', {'form': form, 'booking_status': booking_status})

def booking_status_delete(request, pk):
    booking_status = get_object_or_404(BookingStatus, pk=pk)
    if request.method == 'POST':
        booking_status.delete()
    return redirect('booking_status_add')


# def progress_status_add(request):
#     if request.method == 'POST':
#         form = ProgressStatusForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('progress_status_add')  # Redirect to the same page
#     else:
#         form = ProgressStatusForm()
    
#     progress_statuses = ProgressStatus.objects.all()
#     return render(request, 'progress_status_add.html', {'form': form, 'progress_statuses': progress_statuses})

def progress_status_add(request):
    ctx ={}
    form = ProgressStatusForm(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.pstatus_createdby = request.user
        obj.pstatus_createdon = timezone.now()
        obj.save()
        print(request.user)
        messages.success(request,"Progress Status saved")
        form = ProgressStatusForm()
        print("Saved")
    else:
        print(form.errors)

    search_query = request.GET.get('name_contains')
    if search_query:
        data = ProgressStatus.objects.filter(
            Q(status__icontains=search_query)
        )
    else:
        data = ProgressStatus.objects.all()

    # data = WorkcenterModel.objects.all()
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
    return render(request, "progress_status_add.html", ctx)

def progress_status_delete(request, pk):
    booking_status = get_object_or_404(ProgressStatus, pk=pk)
    
    if request.method == 'POST':
        booking_status.delete()
    
    return redirect('progress_status_add')

def progress_status_edit(request, pk):
    progress_status = get_object_or_404(ProgressStatus, pk=pk)

    if request.method == 'POST':
        form = ProgressStatusForm(request.POST, instance=progress_status)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.pstatus_modiby = request.user
            obj.pstatus_modon = timezone.now()
            form.save()
            return redirect('progress_status_add')  # Redirect to the same page
    else:
        form = ProgressStatusForm(instance=progress_status)

    return render(request, 'progress_status_edit.html', {'form': form, 'progress_status': progress_status})

def get_progress_status(request):
    progress_status_values = ProgressStatus.objects.values_list('id', 'status')
    return JsonResponse(list(progress_status_values), safe=False)

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



# def trip_details(request, trip_id):
#     trip = get_object_or_404(Travelrequestheader, THINTRID=trip_id)
#     # print(trip)
#     flights = Travelflightdetails.objects.filter(TFLDTRPNAME=trip)
#     # print(flights)
#     hotels = Travelhoteldetails.objects.filter(THDTRHINTRID=trip)
#     cars = Travelcarbookingdetails.objects.filter(TCBDTHID=trip)
#     visas = Travelvisadetails.objects.filter(TVDTRAVEL=trip)
#     forex = Travelforexdetails.objects.filter(TFDTRVTID=trip)

#     return render(request, 'view_trip_details.html', {
#         'trip': trip,
#         'flights': flights,
#         'hotels': hotels,
#         'cars': cars,
#         'visas': visas,
#         'forex': forex,
#         'trip_id': trip_id,
#     })

def trip_details(request, trip_id):
    trip = get_object_or_404(Travelrequestheader, THINTRID=trip_id)
    flights = Travelflightdetails.objects.filter(TFLDTRPNAME=trip)
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

def update_status(request):
    if request.method == 'POST':
        trip_id = request.POST.get('trip')
        trip = get_object_or_404(Travelrequestheader, THINTRID=trip_id)
        trip.THTASTATUS_id = 2
        trip.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


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



def add_flight(from_location, to_location, depart_date, return_date, createdby, trip, pref, pref_air,flight_prog=None, booking_type='Round Trip', flight_form_data=None):
    try:
        if flight_form_data:
            for form_data in flight_form_data:
                flight = Travelflightdetails(TFLDFRMPLC=form_data['TFLDFRMPLC'], TFLDTOPLC=form_data['TFLDTOPLC'], TFLDDTEOFTRV=form_data['TFLDDTEOFTRV'], TFLDRETURN=form_data['TFLDRETURN'], TFLDCREABY=createdby, TFLDTRPNAME=trip, TFLDPREF=pref, TFLDPREFAIR=pref_air,TFLDPROGSTA=flight_prog, TFLDTRPTYP=booking_type)
                flight.save()
        else:
            booking = Travelflightdetails(TFLDFRMPLC=from_location, TFLDTOPLC=to_location, TFLDDTEOFTRV=depart_date, TFLDRETURN=return_date, TFLDCREABY=createdby, TFLDTRPNAME=trip, TFLDPREF=pref, TFLDPREFAIR=pref_air,TFLDPROGSTA=flight_prog, TFLDTRPTYP=booking_type)
            booking.save()
            if return_date and booking_type == 'Round Trip':
                return_booking = Travelflightdetails(TFLDFRMPLC=to_location, TFLDTOPLC=from_location, TFLDDTEOFTRV=return_date, TFLDCREABY=createdby, TFLDTRPNAME=trip, TFLDPREF=pref, TFLDPREFAIR=pref_air,TFLDPROGSTA=flight_prog, TFLDTRPTYP=booking_type)
                return_booking.save()
            return [booking]
    except Exception as e:
        print(f"An error occurred while adding flight details: {e}")


def add_hotel(room_type, checkin_date, checkout_date, pref_hotel, city,createdby, htrip,prog_status):
    try:
        hotel = Travelhoteldetails(
            THDCHKINDTE=checkin_date,
            THDCHKOTDTE=checkout_date,
            THDCITY=city,
            THDCREABY=createdby,
            THDTRHINTRID=htrip,
            THDPREFHOTL=pref_hotel,
            THDHTYPE=room_type,
            THDPROGSTA=prog_status
        )
        hotel.save()
        print("hotelsaved")
        return [hotel]
    except Exception as e:
        print(f"An error occurred while adding hotel details: {e}")

def add_car(car_type, car_from, car_to, car_pickup, car_drop,car_createdby, ctrip,car_prog):
    try:
        car = Travelcarbookingdetails(
            TCBDFRLOC=car_from,
            TCBDTOLOC=car_to,
            TCBDPIKU=car_pickup,
            TCBDDROP=car_drop,
            TCBDCREABY=car_createdby,
            TCBDTHID=ctrip,
            TCBDCTYP=car_type,
            TCBDPROGSTA = car_prog,

        )
        car.save()
        print("carsaved")
        return [car]
    except Exception as e:
        print(f"An error occurred while adding car details: {e}")

def add_visa(travel_date, visiting_country, fees, remarks,visa_createdby, visa_type,vtrip,visa_prog):
    try:
        visa = Travelvisadetails(
            TVDTRAVDTE=travel_date,
            TVDVISTGCOUN=visiting_country,
            TVDVSAFES=fees,
            TVDREMK=remarks,
            TVDTRAVEL=vtrip,
            TVDCREABY=visa_createdby,
            TVDVISTYPE=visa_type,
            TVDPROGSTA=visa_prog,
        )
        visa.save()
        print("visasaved")
        return [visa]
    except Exception as e:
        print(f"An error occurred while adding visa details: {e}")


def add_forex(forex_type, forext_date, amount, currency, remarks,forex_createdby, ftrip,forex_prog):
    try:
        forex = Travelforexdetails(
            TFDCSHTYPE=forex_type,
            TFDTRAVDTE=forext_date,
            TFDAMNT=amount,
            TFODCREABY=forex_createdby,
            TFDTRVTID=ftrip,
            TFDCURR=currency,
            TFDREMARK=remarks,
            TFDPROGSTA=forex_prog

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
            default_status = TravelStatus.objects.get(TSDESC='Entered')
            travel_header.THTASTATUS = default_status
            travel_header.save()
            header_form = Travelrequestheaderform()

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
                flight_prog = flight_form.cleaned_data['TFLDPROGSTA']
                print(flight_prog)
                multi_flight_prog = None


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
                        # multi_flight_prog = None
                        if multicity_formset.is_valid():
                            for form in multicity_formset:
                                form.fields['TFLDDTEOFTRV'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')

                            print("true")
                            for i, form in enumerate(multicity_formset.forms):
                                if form.cleaned_data:
                                    from_city = form.cleaned_data.get('TFLDFRMPLC')
                                    to_city = form.cleaned_data.get('TFLDTOPLC')
                                    date_of_travel = form.cleaned_data.get('TFLDDTEOFTRV')
                                    multi_flight_prog = form.cleaned_data.get('TFLDPROGSTA')


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
                                        multicity_flight.TFLDPROGSTA = multi_flight_prog
                                        print(multi_flight_prog)
                                        # print(from_city)


                                        add_flight(from_city, to_city, date_of_travel, None, createdby, trip, pref, pref_air,flight_prog=flight_prog, booking_type=booking_type)
                                        messages.success(request, "Multi-city flights saved successfully")
                        else:
                            messages.error(request, "Multi-city formset is not valid. Please check your input.")

                    
                            # print(multicity_formset.errors)
                    add_flight(from_location, to_location, depart_date, return_date, createdby, trip, pref, pref_air, flight_prog=multi_flight_prog if multi_flight_prog is not None else flight_prog, booking_type=booking_type)
                    # add_flight(from_location, to_location, depart_date, return_date, createdby, trip, pref, pref_air,flight_prog=multi_flight_prog, booking_type=booking_type)
                    messages.success(request, "Flight request saved successfully", extra_tags="flight_form_success")
                    flight_form = Travelflightdetailsform()
            else:
                messages.error(request, "Flight form is not valid. Please check your input.")
                # print(flight_form.errors)
                
            if hotel_form is not None and hotel_form.is_valid():
                    print('hotel_form')

                    
                    trip_id = travel_header.THINTRID
                    htrip = Travelrequestheader.objects.get(THINTRID=trip_id)
                    createdby = request.user
                    checkin_date = hotel_form.cleaned_data['THDCHKINDTE']
                    checkout_date = hotel_form.cleaned_data['THDCHKOTDTE']
                    room_type = hotel_form.cleaned_data['THDHTYPE']
                    pref_hotel = hotel_form.cleaned_data['THDPREFHOTL'] 
                    city = hotel_form.cleaned_data['THDCITY']
                    prog_status = hotel_form.cleaned_data['THDPROGSTA']



                    add_hotel(room_type, checkin_date, checkout_date, pref_hotel, city, createdby,htrip,prog_status)
                    messages.success(request, "Hotel Request saved successfully", extra_tags="hotel_form_success") 
                    hotel_form = Travelhoteldetailsform()
                    # hotel_form = Travelhoteldetailsform(initial={'THDPROGSTA': your_initial_value})


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
                                    prog_status = form.cleaned_data.get('THDPROGSTA')

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
                                        multi_hotel.THDPROGSTA = prog_status

                                        add_hotel(room_type, checkin_date, checkout_date, pref_hotel, city, createdby,htrip,prog_status)
                                        messages.success(request, "Multi-hotel details saved successfully", extra_tags="hotel_form_success")
                    else:
                        print(multihotel_formset.errors)
                        for i, form in enumerate(multihotel_formset.forms):
                            print(f"Form {i+1} errors:")
                            print(form.errors)
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
                    car_prog = car_form.cleaned_data['TCBDPROGSTA']


                    add_car(car_type, car_from, car_to, car_pickup, car_drop,car_createdby, ctrip,car_prog)
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
                                    car_prog = form.cleaned_data.get('TCBDPROGSTA')


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
                                        multi_car.TCBDPROGSTA = car_prog

                                        add_car(car_type, car_from, car_to, car_pickup, car_drop,car_createdby, ctrip,car_prog)
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
                    visa_prog = visa_form.cleaned_data['TVDPROGSTA']

                    add_visa(travel_date, visiting_country, fees, remarks,visa_createdby, visa_type,vtrip,visa_prog)
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
                                    visa_prog = form.cleaned_data.get('TVDPROGSTA')



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
                                        multi_visa.TVDPROGSTA = visa_prog


                                        add_visa(travel_date, visiting_country, fees, remarks,visa_createdby, visa_type,vtrip,visa_prog)
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
                    forex_prog = forex_form.cleaned_data['TFDPROGSTA']


                    add_forex(forex_type, forext_date, amount, currency, remarks,forex_createdby, ftrip,forex_prog)
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
                                    forex_prog = form.cleaned_data.get('TFDPROGSTA')

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

                                        add_forex(forex_type, forext_date, amount, currency, remarks,forex_createdby, ftrip,forex_prog)
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


# def role(request):
#     ctx ={}
#     form = Userrole(request.POST or None)
#     if form.is_valid():
#         print("valid")      
#         obj = form.save()
#         obj.URCREABY = request.user
#         obj.URMODIBY = request.user
#         obj.save()
#         print(request.user)
#         messages.success(request,"Details added")      
#         print("Saved")
#         form = Userrole()
#     else:
#         print(form.errors)
#     data = UserroleModel.objects.all()
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
#     return render(request, "role.html", ctx)

def role(request):
    ctx = {}
    form = Userrole(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.URCREABY = request.user
        obj.URMODIBY = request.user
        obj.save()
        messages.success(request, "Details added")
        form = Userrole()
    else:
        print(form.errors)

    search_query = request.GET.get('name_contains')
    if search_query:
        data = UserroleModel.objects.filter(
            Q(URROLTLE__icontains=search_query) | Q(URRESP__icontains=search_query)
        )
    else:
        data = UserroleModel.objects.all()

    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages
    ctx = {
        'page_obj': page_obj,
        'nums': nums,
        'form': form,
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

def role_edit(request, pk):
    role = get_object_or_404(UserroleModel, pk=pk)
    if request.method == 'POST':
        form = Userrole(request.POST, instance=role)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.URMODIBY = request.user
            obj.URMODION = timezone.now()
            obj.save()
            messages.success(request, "Details updated")
            return redirect('role')
        else:
            print(form.errors)
    else:
        form = Userrole(instance=role)
    return render(request, "role_edit.html", {'form': form, 'role': role})



# def addiv(request):
#     ctx ={}
#     form = Basecostcenterform(request.POST or None)
#     if form.is_valid():
#         print("valid")      
#         obj = form.save()
#         obj.BCCCREABY = request.user
#         obj.save()
#         print(request.user)
#         messages.success(request,"Details added")
        
#         print("Saved")
#     else:
#         print(form.errors)   
#     data = Basecostcenter.objects.all()
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
#     return render(request, "addiv.html", ctx)

def addiv(request):
    ctx = {}
    form = Basecostcenterform(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.BCCCREABY = request.user
        obj.save()
        messages.success(request, "Details added")
        form = Basecostcenterform()
    else:
        print(form.errors)

    search_query = request.GET.get('name_contains')

    if search_query:
        data = Basecostcenter.objects.filter(
            Q(BCCEXPCSTCNTR__icontains=search_query) | Q(BCCDESP__icontains=search_query)
        )
    else:
        data = Basecostcenter.objects.all()

    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages
    ctx = {
        'page_obj': page_obj,
        'nums': nums,
        'form': form,
    }
    return render(request, "addiv.html", ctx)

def center_edit(request, pk):
    center = get_object_or_404(Basecostcenter, pk=pk)
    if request.method == 'POST':
        form = Basecostcenterform(request.POST, instance=center)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.BCCMODIBY = request.user
            obj.BCCMODION = timezone.now()
            obj.save()
            messages.success(request, "Details updated")
            return redirect('addiv')
        else:
            print(form.errors)
    else:
        form = Basecostcenterform(instance=center)
    return render(request, "center_edit.html", {'form': form, 'center': center})

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
#         obj = form.save()
#         obj.WCCREABY = request.user
#         obj.save()
#         print(request.user)
#         messages.success(request,"Details added")
#         form = Workcenter()
#         print("Saved")
#     else:
#         print(form.errors)

#     search_query = request.GET.get('name_contains')
#     if search_query:
#         data = WorkcenterModel.objects.filter(
#             Q(WCWRKCNTR__icontains=search_query) | Q(WCWRKCNTRDESP__icontains=search_query)
#         )
#     else:
#         data = WorkcenterModel.objects.all()

#     # data = WorkcenterModel.objects.all()
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
#     return render(request, "workcenter.html", ctx)

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
        form = Workcenter()
        print("Saved")
    else:
        print(form.errors)

    search_query = request.GET.get('name_contains')
    if search_query:
        data = WorkcenterModel.objects.filter(
            Q(WCWRKCNTR__icontains=search_query) | Q(WCWRKCNTRDESP__icontains=search_query)
        )
    else:
        data = WorkcenterModel.objects.all()

    # data = WorkcenterModel.objects.all()
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



def work_edit(request, pk):
    work = get_object_or_404(WorkcenterModel, pk=pk)
    if request.method == 'POST':
        form = Workcenter(request.POST, instance=work)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.WCMODIBY = request.user
            obj.WCMODION = timezone.now()
            obj.save()
            messages.success(request, "Details updated")
            return redirect('work_save')
        else:
            print(form.errors)
    else:
        form = Workcenter(instance=work)
    return render(request, "workcenter_edit.html", {'form': form, 'work': work})

# ProfileFormSet = formset_factory(ProfileForm, extra=1, can_delete=True)

# def add_profile(request):
#     formset = ProfileFormSet(request.POST or None, prefix='profile')
#     ctx = {}
    
#     if request.method == 'POST':
#         if formset.is_valid():
#             for form in formset:
#                 if form.is_valid():
#                     obj = form.save(commit=False)
#                     obj.TPFCCREBY = request.user
#                     obj.save()
#                     messages.success(request, "Details added")
#             return redirect('profile')
#         else:
#             print(formset.errors)
#     else:
#         formset = ProfileFormSet(prefix='profile')
    
#     data = ProfileModel.objects.all()
#     paginator = Paginator(data, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     nums = "a" * page_obj.paginator.num_pages
#     ctx = {
#         'page_obj': page_obj,
#         'nums': nums,
#         'formset': formset,
#         # 'form':form
#     }
#     return render(request, "profile.html", ctx)
# def get_user_choices(request):
#     users = MyUser.objects.all()
#     choices = [{"value": user.id, "label": user.first_name} for user in users]
#     return JsonResponse(list(choices), safe=False)

def get_user_choices(request):
    users = MyUser.objects.all().distinct()
    choices = [{"value": user.id, "label": user.first_name} for user in users]
    return JsonResponse(list(choices), safe=False)



# def add_profile(request):
#     multi_profile = formset_factory(ProfileForm)
#     multiprofile_formset = multi_profile(request.POST, prefix='multiprofile')
#     ctx ={}
#     form = ProfileForm(request.POST or None)
#     if form.is_valid():
#         print("valid")      
#         obj = form.save()
#         obj.TPFCCREBY = request.user
#         obj.save()
#         print(request.user)
#         messages.success(request,"Details added")
#         form = ProfileForm()
#         print("Saved")
#     else:
#         print(form.errors)   
#     data = ProfileModel.objects.all()
#     paginator = Paginator(data, 5)
#     page_number = 0
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     nums = "a" * page_obj.paginator.num_pages
#     ctx={
#         # 'data':data,
#         'page_obj': page_obj,
#         'nums': nums,
#         'form':form,
#         'multiprofile_formset':multiprofile_formset
#     }
#     return render(request, "profile.html", ctx)



def add_profile(request):
    # ProfileFormSet = formset_factory(ProfileForm)
    ProfileFormSet = formset_factory(ProfileForm, extra=0)
    ctx = {}

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        multiprofile_formset = ProfileFormSet(request.POST, prefix='multiprofile')
        ftseq = 1

        # print(f"request.POST data: {request.POST}")
        # print(f"formset is bound: {multiprofile_formset.is_bound}")
        # print(f"formset is valid: {multiprofile_formset.is_valid()}")

        User = get_user_model()

        if multiprofile_formset.is_valid() and form.is_valid():
            # print("multiprofile_formset POST data:")
            # for key, value in request.POST.items():
            #     if key.startswith('multiprofile'):
            #         print(f"{key}: {value}")
            print("formandformset")
            obj = form.save(commit=False)
            obj.TPFCCREBY = request.user
            obj.TPFCLSEQ = ftseq
            obj.save()

            # Save TPFCMANID values from formset
            tseq = 2
            tpfc_name = form.cleaned_data.get('TPFCNAME')
            for i, multiprofile_form in enumerate(multiprofile_formset):
                multiprofile = multiprofile_form.save(commit=False)
                user_id = int(request.POST.get(f'multiprofile-{i}-THDPROGSTA'))
                user_instance = User.objects.get(id=user_id)
                multiprofile.TPFCMANID = user_instance
                print(multiprofile.TPFCMANID)
                multiprofile.TPFCNAME = tpfc_name
                multiprofile.TPFCLSEQ = tseq
                multiprofile.TPFCCREBY = request.user
                multiprofile.save()
                tseq += 1
                
            messages.success(request, "Details added")
            return redirect('add_profile')
        elif form.is_valid():
            print("form")
            obj = form.save(commit=False)
            obj.TPFCCREBY = request.user
            obj.save()

            messages.success(request, "Details added")
            return redirect('add_profile')
        else:
            print(form.errors)
            for i, form in enumerate(multiprofile_formset.forms):
                            print(f"Form {i+1} errors:")
                            print(form.errors)
    else:
        form = ProfileForm()
        multiprofile_formset = ProfileFormSet(prefix='multiprofile')

    search_query = request.GET.get('name_contains')
    if search_query:
        data = ProfileModel.objects.filter(
            Q(TPFCNAME__icontains=search_query) | Q(TPFCINTID__icontains=search_query)
        )
    else:
        data = ProfileModel.objects.all()

    # data = ProfileModel.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        'page_obj': page_obj,
        'form': form,
        'multiprofile_formset': multiprofile_formset
    }
    return render(request, "profile.html", ctx)

def profile_edit(request, pk):
    profile = get_object_or_404(ProfileModel, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.TPFCMODBY = request.user
            obj.TPFCMODON = timezone.now()
            obj.save()
            messages.success(request, "Details updated")
            return redirect('addiv')
        else:
            print(form.errors)
    else:
        form = ProfileForm(instance=profile)
    return render(request, "profile_edit.html", {'form': form, 'profile': profile})

def ass_profile_edit(request, pk):
    profile = get_object_or_404(AssignProfileModel, pk=pk)
    if request.method == 'POST':
        form = AssignProfileForm(request.POST, instance=profile)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.TPFAMODBY = request.user
            obj.TPFAMODON = timezone.now()
            obj.save()
            messages.success(request, "Details updated")
            return redirect('ass_profile')
        else:
            print(form.errors)
    else:
        form = AssignProfileForm(instance=profile)
    return render(request, "ass_profile_edit.html", {'form': form, 'profile': profile})



# def ass_profile(request):
#     ctx = {}
#     form = AssignProfileForm(request.POST or None)

#     if form.is_valid():
#         form.instance.TPFACREDBY = request.user
#         profile_name = form.cleaned_data['TPFAPRNAME']
#         # id_TPFAPRNAME
#         form.instance.TPFAPRNAME = profile_name
#         form.save()
#         messages.success(request, "Details added")
#         form = AssignProfileForm()
#     else:
#         for field in form:
#             print(field.name, field.errors)

#     search_query = request.GET.get('name_contains')
#     if search_query:
#         data = AssignProfileModel.objects.filter(
#             Q(TPFAPRNAME__TPFCNAME__icontains=search_query) | Q(TPFASTATUS__icontains=search_query)
#         )
#     else:
#         data = AssignProfileModel.objects.all()

#     paginator = Paginator(data, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     nums = "a" * page_obj.paginator.num_pages

#     # Get the employee name for each row in the table
#     for row in page_obj:
#         employee = MyUser.objects.get(id=row.TPFAEMPID_id)
#         row.employee_name = employee.first_name

#     ctx = {
#         'page_obj': page_obj,
#         'nums': nums,
#         'form': form,
#     }
#     return render(request, "ass_profile.html", ctx)

def ass_profile(request):
    ctx = {}
    form = AssignProfileForm(request.POST or None)

    if form.is_valid():
        form.instance.TPFACREDBY = request.user
        selected_employee_id = form.cleaned_data['TPFAEMPID'].id

        profile_name = form.cleaned_data['TPFAPRNAME'].TPFCNAME
        profile_instances = ProfileModel.objects.filter(TPFCNAME=profile_name)
        from_date = form.cleaned_data['TPFAFROMD']
        to_date = form.cleaned_data['TPFATODATE']

        for profile_instance in profile_instances:
            # Check if the combination already exists
            if not AssignProfileModel.objects.filter(
                TPFAEMPID_id=selected_employee_id,
                TPFAPRNAME=profile_instance,
            ).exists():
                # If not, save the instance
                assign_profile_instance = AssignProfileModel(
                    TPFAEMPID_id=selected_employee_id,
                    TPFAPRNAME=profile_instance,
                    TPFAFROMD=from_date,
                    TPFATODATE=to_date,
                    TPFACREDBY=request.user,
                )
                assign_profile_instance.save()
                print(f"Saved AssignProfileModel for approver: {selected_employee_id}")
            else:
                messages.error(request, f"Profile already assigned to employee with ID: {selected_employee_id}")

        messages.success(request, "Details added")
        form = AssignProfileForm()
    else:
        for field in form:
            print(field.name, field.errors)

    search_query = request.GET.get('name_contains')
    if search_query:
        data = AssignProfileModel.objects.filter(
            Q(TPFAPRNAME__TPFCNAME__icontains=search_query) | Q(TPFASTATUS__icontains=search_query)
        )
    else:
        data = AssignProfileModel.objects.all()

    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages

    # Get the employee name for each row in the table
    for row in page_obj:
        employee = MyUser.objects.get(id=row.TPFAEMPID_id)
        row.employee_name = employee.first_name

    ctx = {
        'page_obj': page_obj,
        'nums': nums,
        'form': form,
    }
    return render(request, "ass_profile.html", ctx)



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


def add_div(request):
    ctx ={}
    form = Divmaster(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.DIVMCREABY = request.user
        obj.DIVMMODION = timezone.now()
        obj.save()
        print(request.user)
        messages.success(request,"Division details saved")
        form = Divmaster()
        print("Saved")
    else:
        print(form.errors)

    search_query = request.GET.get('name_contains')
    if search_query:
        data = DivmasterModel.objects.filter(
            Q(DIVMTLE__icontains=search_query) | Q(DIVMDESP__icontains=search_query)
        )
    else:
        data = DivmasterModel.objects.all()

    # data = WorkcenterModel.objects.all()
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
    return render(request, "add_div.html", ctx)

def div_auth(request):
    ctx ={}
    form = Divassignmentuserform(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.DIVASSUCREABY = request.user
        obj.DIVASSUMODION = timezone.now()
        obj.save()
        print(request.user)
        messages.success(request,"Division details saved")
        form = Divassignmentuserform()
        print("Saved")
    else:
        print(form.errors)

    search_query = request.GET.get('name_contains')
    if search_query:
        data = Divassignmentuser.objects.filter(
            Q(DIVMTLE__icontains=search_query) | Q(DIVMDESP__icontains=search_query)
        )
    else:
        data = Divassignmentuser.objects.all()

    # data = WorkcenterModel.objects.all()
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
    return render(request, "div_auth.html", ctx)

def addtile(request):
    ctx ={}
    form = Titledetails(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.TITDCREABY = request.user
        obj.TITDCREAON = timezone.now()
        obj.save()
        print(request.user)
        messages.success(request,"Details added")
        print("Saved")
        form = Titledetails()
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

def tile_auth(request):
    ctx ={}
    form = Tileautherizationdetailsform(request.POST or None)
    if form.is_valid():
        print("valid")      
        obj = form.save()
        obj.TADCREABY = request.user
        obj.TADCREAON = timezone.now()
        obj.save()
        print(request.user)
        messages.success(request,"Tile authorization saved")
        form = Tileautherizationdetailsform()
        print("Saved")
    else:
        print(form.errors)

    search_query = request.GET.get('name_contains')
    if search_query:
        data = Tileautherizationdetails.objects.filter(
            Q(DIVMTLE__icontains=search_query) | Q(DIVMDESP__icontains=search_query)
        )
    else:
        data = Tileautherizationdetails.objects.all()

    # data = WorkcenterModel.objects.all()
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
    return render(request, "tile_auth.html", ctx)


def get_filtered_div_tiles(request):
    role_id = request.GET.get('role_id')

    if role_id is None:
        return JsonResponse({'div_tiles': []})  # Return an empty list of div tiles
    try:
        role_id = int(role_id)
    except ValueError:
        return JsonResponse({'error': 'Invalid role ID format'}, status=400)

    # Retrieve Div Tiles associated with the selected Role Title
    filtered_div_tiles = DivmasterModel.objects.filter(divassignmentuser__DIVASSUURROLTLE=role_id)
    div_tiles_data = []
    for div_tile in filtered_div_tiles:
        div_tiles_data.append({
            'id': div_tile.DIVMID,
            'text': div_tile.DIVMTLE
        })
    return JsonResponse({'div_tiles': div_tiles_data})


def div_edit(request, pk):
    div = get_object_or_404(DivmasterModel, DIVINTID=pk)
    if request.method == 'POST':
        form = Divmaster(request.POST, instance=div)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.DIVMMODIBY = request.user
            obj.DIVMMODION = timezone.now()
            obj.save()
            messages.success(request, "Details updated")
            return redirect('add_div')
        else:
            print(form.errors)
    else:
        form = Divmaster(instance=div)
    return render(request, "div_edit.html", {'form': form, 'div': div})

def div_auth_edit(request, pk):
    div_auth = get_object_or_404(Divassignmentuser, DIVASSUINTRID=pk)
    if request.method == 'POST':
        form = Divassignmentuserform(request.POST, instance=div_auth)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.DIVASSUMODIBY = request.user
            obj.DIVASSUMODION = timezone.now()
            obj.save()
            messages.success(request, "Details updated")
            return redirect('div_auth')
        else:
            print(form.errors)
    else:
        form = Divassignmentuserform(instance=div_auth)
    return render(request, "div_auth_edit.html", {'form': form, 'div_auth': div_auth})

def tile_edit(request, pk):
    tile = get_object_or_404(TitledetailsModel, TITDINTRID=pk)
    if request.method == 'POST':
        form = Titledetails(request.POST, instance=tile)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.TITDMODIBY = request.user
            obj.TITDMODION = timezone.now()
            obj.save()
            messages.success(request, "Details updated")
            return redirect('addtile')
        else:
            print(form.errors)
    else:
        form = Titledetails(instance=tile)
    return render(request, "tile_edit.html", {'form': form, 'tile': tile})

def tile_auth_edit(request, pk):
    tile_auth = get_object_or_404(Tileautherizationdetails, TADINTRID=pk)
    if request.method == 'POST':
        form = Tileautherizationdetailsform(request.POST, instance=tile_auth)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.TADMODIBY = request.user
            obj.TADMODION = timezone.now()
            obj.save()
            messages.success(request, "Details updated")
            return redirect('tile_auth')
        else:
            print(form.errors)
    else:
        form = Tileautherizationdetailsform(instance=tile_auth)
    return render(request, "tile_auth_edit.html", {'form': form, 'tile_auth': tile_auth})


# def help_doc(request):
#     return render(request, "help_doc.html")

# def help_doc(request):
#     documents = [
#         {"title": "specs", "specs": "specs.docx"},
#     ]
#     context = {"documents": documents}
#     return render(request, "help_doc.html", context)

# def help_doc(request):
#     media_root = settings.MEDIA_ROOT
#     document_files = []

#     for root, dirs, files in os.walk(media_root):
#         for file in files:
#             if file.endswith('.doc') or file.endswith('.docx'):
#                 document_files.append(file)
    
#     print("Document files:", document_files)  # Debug statement
#     context = {"document_files": document_files}
#     return render(request, "help_doc.html", context)

def help_doc(request):
    documents = [
        {"title": "Specifications", "file_name": "specs.docx"},
        {"title": "Adding Employee", "file_name": "addemp.docx"},
        {"title": "Adding Div and Tiles", "file_name": "divandtile.docx"},

    ]
    context = {"documents": documents}
    return render(request, "help_doc.html", context)

# def help_doc(request):
#     document_path = os.path.join(settings.MEDIA_ROOT, document_name)
#     with open(document_path, 'rb') as document_file:
#         response = HttpResponse(document_file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = f'inline; filename="{document_name}"'
#         return response
