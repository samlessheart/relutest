from django.urls import path 
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,    TokenRefreshView)
from .views import userdetails, addteacher, addstaff, addstudent, AllUser , AllTeacher, AllStudent, UserDetail
urlpatterns = [ 
    
    path('userdetail/<int:pk>/', UserDetail.as_view(), name  = 'userdetail'),

    path('teacherlist/', AllTeacher.as_view(), name  = 'teacherlist'),
    path('studentlist/', AllStudent.as_view(), name  = 'studentlist'),
    path('userlist/', AllUser.as_view(), name  = 'userlist'),

    # path('stafflist/', AllStaff.as_view(), name  = 'stafflist'),


    path('addteacher/', addteacher, name  = 'addteacher'),
    path('addstudent/', addstudent, name  = 'addstudent'),
    path('addstaff/', addstaff, name  = 'addstaff'),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),





]