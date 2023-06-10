from rest_framework import serializers
from django.db import transaction
from main.models import  CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        
        fields = ['id', 'first_name','last_name', 'username', 'password', 
                  'email', 'is_staff', 'is_teacher','is_student']
        read_only_fields = ['id', 'is_teacher', 'is_student']
        extra_kwargs = {'password': {'write_only': True},
                    
                        }


    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['first_name'] is None or  data['last_name'] is None or data['email'] is None:
            raise serializers.ValidationError("These fields are required")
        return data