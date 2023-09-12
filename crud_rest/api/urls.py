from django.urls import path 
from . import views

urlpatterns = [
    path('v1/get-stu', views.get_stu, name='get_stu'),
    path('v1/create-stu', views.create_stu, name='create_stu'),
    path('v1/update-stu/<uuid:stu_uid>', views.update_stu, name='update_stu'),
    path('v1/delete-stu/<uuid:stu_uid>', views.delete_stu, name='delete_stu'),
    ]


