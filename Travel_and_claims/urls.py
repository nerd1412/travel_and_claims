"""Travel_and_claims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Travel import views
from Travel.views import add_flight
from django.views.generic.base import TemplateView
# from Travel.views import SignUpView
from Travel.views import mylogin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
app_name='Travel'


urlpatterns = [
    # path("signup/", SignUpView.as_view(template_name="emp.html"), name="singup"),
    path("signup/", views.singup, name="singup"),
    path("",views.mylogin,name='mylogin'),
    path("login/", views.mylogin, name="login"),
    path('mylogout',views.mylogout,name='mylogout'),
    path('admin/', admin.site.urls),
    path("home/", views.home, name="home"),
    path("trip_app/", views.trip_app, name="trip_app"),
    path('password-reset/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path("view_trip/", views.view_trip, name="view_trip"),
    path('trip/<int:trip_id>/', views.trip_details, name='trip_details'),
    path('flight/<int:trip_id>/add/', views.add_flight_list, name='add_flight_list'),
    path('flight/<int:flight_id>/edit/', views.edit_flight, name='edit_flight'),
    path('flight/<int:flight_id>/delete/', views.delete_flight, name='delete_flight'),
    path('hotel/<int:trip_id>/add/', views.add_hotel_list, name='add_hotel_list'),
    path('hotel/<int:hotel_id>/edit/', views.edit_hotel, name='edit_hotel'),
    path('hotel/<int:hotel_id>/delete/', views.delete_hotel, name='delete_hotel'),
    path('car/<int:trip_id>/add/', views.add_car_list, name='add_car_list'),
    path('car/<int:car_id>/edit/', views.edit_car, name='edit_car'),
    path('car/<int:car_id>/delete/', views.delete_car, name='delete_car'),
    path('visa/<int:trip_id>/add/', views.add_visa_list, name='add_visa_list'),
    path('visa/<int:visa_id>/edit/', views.edit_visa, name='edit_visa'),
    path('visa/<int:visa_id>/delete/', views.delete_visa, name='delete_visa'),
    path('forex/<int:trip_id>/add/', views.add_forex_list, name='add_forex_list'),
    path('forex/<int:forex_id>/edit/', views.edit_forex, name='edit_forex'),
    path('forex/<int:forex_id>/delete/', views.delete_forex, name='delete_forex'),
    path('booking_status/add/', views.booking_status_add, name='booking_status_add'),
    path('booking_status/edit/<int:pk>/', views.booking_status_edit, name='booking_status_edit'),
    path('booking_status/delete/<int:pk>/', views.booking_status_delete, name='booking_status_delete'),
    path('progress_status/add/', views.progress_status_add, name='progress_status_add'),
    path('progress_status/<int:pk>/edit/', views.progress_status_edit, name='progress_status_edit'),
    path('progress_status/<int:pk>/delete/', views.progress_status_delete, name='progress_status_delete'),
    path('get_progress_status/', views.get_progress_status, name='get_progress_status'),
    path("travel/", views.travel, name="travel"),
    path("travel_app/", views.travel_app, name="travel_app"),
    path('get_unread_notification_count/', views.get_unread_notification_count, name='get_unread_notification_count'),
    path('mark_notifications_as_read/', views.mark_notifications_as_read, name='mark_notifications_as_read'),
    # path("travel_app/<int:trip_id>/", views.travel_app, name="travel_app_with_trip_id"),
    path('view-trip/', views.view_trip, name='view_trip'),
    path('update_status/', views.update_status, name='update_status'),
    path('cancel_request/', views.cancel_request, name='cancel_request'),
    path("emp/", views.emp, name="emp"),
    path("role/", views.role, name="role"),
    path("role/search", views.role, name="role"),
    path("add_profile/", views.add_profile, name="add_profile"),
    path("employee_edit/<int:pk>", views.employee_edit, name="employee_edit"),
    path("profile_edit/<int:pk>", views.profile_edit, name="profile_edit"),
    path("ass_profile_edit/<int:pk>", views.ass_profile_edit, name="ass_profile_edit"),
    path("app_request/<int:pk>", views.app_request, name="app_request"),
    path("ass_profile/", views.ass_profile, name="ass_profile"),
    path('get_user_choices/', views.get_user_choices, name='get_user_choices'),
    # path("role_edit/<int:id>", views.role_edit, name="role_edit"),
    path("role_edit/<int:pk>", views.role_edit, name="role_edit"),
    path("center_edit/<int:pk>", views.center_edit, name="center_edit"),
    path("addiv/", views.addiv, name="addiv"),
    path("add_div/", views.add_div, name="add_div"),
    path("div_edit/<int:pk>", views.div_edit, name="div_edit"),
    path("div_auth/", views.div_auth, name="div_auth"),
    path("div_auth_edit/<int:pk>", views.div_auth_edit, name="div_auth_edit"),
    path("addiv/search", views.addiv, name="addiv"),
    path("addtile/", views.addtile, name="addtile"),
    path("tile_edit/<int:pk>", views.tile_edit, name="tile_edit"),
    path("tile_auth/", views.tile_auth, name="tile_auth"),
    path("tile_auth_edit/<int:pk>", views.tile_auth_edit, name="tile_auth_edit"),
    path('get_filtered_div_tiles/', views.get_filtered_div_tiles, name='get_filtered_div_tiles'),
    path("expense/", views.expense, name="expense"),
    path("pettycash/",views.pettycash, name='pettycash'),
    path("advanceexp/", views.advanceexp, name="advanceexp"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("grade_save/", views.grade_save, name="grade_save"),
    path("grade_edit/<int:id>", views.grade_edit, name="grade_edit"),
    path("work_save/", views.work_save, name="work_save"),
    path("work_save/search", views.work_save, name="work_save"),
    path("work_edit/<int:pk>", views.work_edit, name="work_edit"),
    path("depart_save/", views.depart_save, name="depart_save"),
    path("depart_edit/<int:id>", views.depart_edit, name="depart_edit"),
    path('help_doc/', views.help_doc, name='help_doc'),
    path('password-expired/', views.check_password_expiration, name='password_expired'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)