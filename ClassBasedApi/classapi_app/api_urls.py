from . import views
from django.urls import path

urlpatterns =[
     path('', views.StudentList.as_view(), name='home'),
     path("StudentDetail1/<int:pk>", views.StudentDetail.as_view(),name='StudentDetail'),

]