from django.urls import path
from . import views

urlpatterns=[
    path('',views.EmployeeList.as_view(),name='home'),
    path('EmployeeEdit/<int:id>',views.EmployeeEdit.as_view(),name='edit')
]