from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('edit/<int:id>',views.del_edit,name='edit1')
]