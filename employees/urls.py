from django.urls import path

from .views import (
    EmployeeListCreateView,
    landing,
    home,
    employee_list,
    add_employee,
    edit_employee,
    delete_employee,
    admin_login,
    user_login,
    signup,


)




from .excel_upload import ExcelUploadAPIView

urlpatterns = [

    path('', landing, name='landing'),

    path('dashboard/', home, name='home'),

    path('admin-login/', admin_login, name='admin_login'),

    path('login/', user_login, name='login'),

    path('signup/', signup, name='signup'),

    path('employee-list/', employee_list, name='employee_list'),



   


    path('add-employee/', add_employee, name='add_employee'),

    path(
    'edit-employee/<int:emp_id>/',
    edit_employee,
    name='edit_employee'
),

    path(
    'delete-employee/<int:emp_id>/',
    delete_employee,
    name='delete_employee'
),

    path('employees/', EmployeeListCreateView.as_view()),

    path('upload-excel/', ExcelUploadAPIView.as_view()),
]