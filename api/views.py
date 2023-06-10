from django.shortcuts import render
from api.serializers import UserSerializer
from main.models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTeacherorStaff, IsOwnerorStaff, IsStaff
from  rest_framework.mixins import RetrieveModelMixin


@api_view(['GET'])
@permission_classes([IsAuthenticated , IsOwnerorStaff])
def userdetails(request, pk):
    user = CustomUser.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return Response( serializer.data )


class UserDetail(generics.GenericAPIView, RetrieveModelMixin):
    queryset = CustomUser.objects.all() 
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerorStaff]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    



@api_view(['POST'])
@permission_classes([IsAuthenticated, IsTeacherorStaff])
def addteacher(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save(is_teacher=True)
    user.set_password(request.data['password'])
    user.save()
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated, IsTeacherorStaff])
def addstudent(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save(is_student = True)
    user.set_password(request.data['password'])
    user.save()
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated, IsStaff])
def addstaff(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save(is_staff = True)
    user.set_password(request.data['password'])
    user.save()
    return Response(serializer.data)


class AllStudent(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [ IsAuthenticated, IsTeacherorStaff]
    def get_queryset(self):        
        queryset = CustomUser.objects.filter(is_student = True)        
        return queryset        
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many =True)
        return Response(serializer.data)




class AllTeacher(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [ IsAuthenticated, IsTeacherorStaff]
    def get_queryset(self):        
        queryset = CustomUser.objects.filter(is_teacher = True)        
        return queryset        
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many =True)
        return Response(serializer.data)




class AllUser(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [ IsAuthenticated, IsStaff]
    def get_queryset(self):        
        queryset = CustomUser.objects.all()        
        return queryset        
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many =True)
        return Response(serializer.data)

