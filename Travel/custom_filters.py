from django.contrib import template
from .models import MyUser

register = template.Library()

@register.filter
def get_employee_name(employee_id):
    try:
        employee = MyUser.objects.get(emp_id=employee_id)
        return f"{employee.first_name} {employee.last_name}"
    except MyUser.DoesNotExist:
        return "Unknown"
