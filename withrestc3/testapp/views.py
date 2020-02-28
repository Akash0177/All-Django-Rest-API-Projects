from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
# class EmployeeListAPIView(ListAPIView):
#     #queryset= Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     def get_queryset(self):
#         qs=Employee.objects.all()
#         name=self.request.GET.get('xxx')
#         if name is not None:
#             qs=qs.filter(ename__icontains=name)
#         return qs
#
# class EmployeeCreateAPIView(CreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#
# class EmployeeRetrieveAPIView(RetrieveAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='pk'
#
# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='pk'
#
# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='pk'

class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='pk'
# 
# class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='pk'

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='pk'
# class EmployeeListAPIView(APIView):
#     def get(self,request,fromat=None):
#         qs=Employee.objects.all()
#         serialzer=EmployeeSerializer(qs,many=True)
#         return Response(serialzer.data)
