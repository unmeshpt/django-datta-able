from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Staff
from django.contrib.auth.models import User
from .serializer import StaffSerializer


# Create your views here.
@api_view(['GET'])
def list_staff(request):
    staffs=User.objects.filter(is_staff=True).all()
    serializer = StaffSerializer(staffs, many=True)
    return Response(serializer.data)