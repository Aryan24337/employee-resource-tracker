from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from rest_framework import generics


from .models import Employee
from .serializers import EmployeeSerializer


# Existing API (DO NOT CHANGE)
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def landing(request):
    return render(request, 'landing.html')


# Home Page
# Home Page
# Home Page
def home(request):

    total_employees = Employee.objects.count()

    customer_selected = Employee.objects.filter(
        profile_status__icontains="Customer Selected"
    ).count()

    tp1_pending = Employee.objects.filter(
        profile_status__icontains="TP-1"
    ).count()

    rejected = Employee.objects.filter(
        profile_status__icontains="Rejected"
    ).count()

    profile_shared = Employee.objects.filter(
        profile_status="Profile Shared"
    ).count()

    tp1_selected = Employee.objects.filter(
        profile_status="TP-1 Selected"
    ).count()

    tp2_selected = Employee.objects.filter(
        profile_status="TP-2 Selected"
    ).count()

    final_selected = Employee.objects.filter(
        profile_status="Final Select Using Demand"
    ).count()

    ras_in_progress = Employee.objects.filter(
        profile_status="RAS In Progress"
    ).count()

    # Employee list for dashboard
    employee_list = Employee.objects.all()

    paginator = Paginator(employee_list, 10)

    page_number = request.GET.get('page')

    employees = paginator.get_page(page_number)

    return render(
        request,
        'dashboard.html',
        {
            'total_employees': total_employees,
            'customer_selected': customer_selected,
            'tp1_pending': tp1_pending,
            'rejected': rejected,
            'employees': employees,
            'profile_shared': profile_shared,
            'tp1_selected': tp1_selected,
            'tp2_selected': tp2_selected,
            'final_selected': final_selected,
            'ras_in_progress': ras_in_progress
        }
    )


# Employee List Page
# Employee List Page
def employee_list(request):

    employee_list = Employee.objects.all()

    paginator = Paginator(employee_list, 10)   # 10 employees per page

    page_number = request.GET.get('page')

    employees = paginator.get_page(page_number)

    return render(
        request,
        'employee_list.html',
        {
            'employees': employees
        }
    )

# Add Employee Page
def add_employee(request):

    if request.method == 'POST':

        if Employee.objects.filter(emp_id=request.POST['emp_id']).exists():

           return render(
               request,
               'add_employee.html',
               {
                    'error': 'Employee ID already exists.'
               }
            )

        Employee.objects.create(
            emp_id=request.POST['emp_id'],
            emp_name=request.POST['emp_name'],
            email=request.POST['email'],
            experience=request.POST['experience'],
            primary_skill=request.POST['primary_skill'],
            secondary_skill=request.POST['secondary_skill'],
            cm_name=request.POST['cm_name'],
            profile_status=request.POST['profile_status'],
            customer=request.POST['customer'],
            date_shared=request.POST['date_shared'],
            project_owner=request.POST['project_owner']
        )

        return redirect('employee_list')

    return render(request, 'add_employee.html')

# Edit Employee Page
def edit_employee(request, emp_id):

    employee = get_object_or_404(Employee, id=emp_id)

    if request.method == 'POST':

        employee.cm_name = request.POST['cm_name']
        employee.profile_status = request.POST['profile_status']
        employee.customer = request.POST['customer']

        employee.save()

        return redirect('employee_list')

    return render(
        request,
        'edit_employee.html',
        {
            'employee': employee
        }
    )

# Admin Login Page
def admin_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_superuser:

            login(request, user)

            return redirect('home')

        else:

            return render(
                request,
                'admin_login.html',
                {
                    'error': 'Invalid admin credentials'
                }
            )

    return render(request, 'admin_login.html')

# User Login Page
def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and not user.is_superuser:

            login(request, user)

            return redirect('home')

        else:

            return render(
                request,
                'login.html',
                {
                    'error': 'Invalid user credentials'
                }
            )

    return render(request, 'login.html')

# User Sign Up Page
def signup(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'signup.html',
                {
                    'error': 'Username already exists'
                }
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'signup.html')


def delete_employee(request, emp_id):

    employee = get_object_or_404(Employee, id=emp_id)

    if request.method == "POST":

        employee.delete()

        return redirect('employee_list')

    return redirect('edit_employee', emp_id=emp_id)





