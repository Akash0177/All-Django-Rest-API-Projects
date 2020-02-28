from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerialzer
from rest_framework.viewsets import ViewSet
class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        colors=['RED','YELLOW','GREEN','BLUE']
        return Response({'msg':'Happy Pongal','colors':colors})
    def post(self,request,*args,**kwargs):
        serializer=NameSerialzer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {}, Happy Pongal!!!'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)
    def put(self,request,*args,**kwargs):
        return Response({'msg':'This response from put method of api view'})
    def patch(self,request,*args,**kwargs):
        return Response({'msg':'This response from patch method of api view'})
    def delete(self,request,*args,**kwargs):
        return Response({'msg':'This response from delete method of api view'})

class TestViewSet(ViewSet):
    def list(self,request):
        colors=['RED','YELLOW','GREEN','BLUE']
        return Response({'msg':'Happy New Year','colors':colors})
    def create(self,request):
        serializer=NameSerialzer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {}, Happy New Year!!!'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)
    def retrieve(self,request,pk=None):
        return Response({'msg':'This is from retrieve  method of ViewSet'})
    def update(self,request,pk=None):
        return Response({'msg':'This is from update  method of ViewSet'})
    def partial_update(self,request,pk=None):
        return Response({'msg':'This is from partial_update  method of ViewSet'})
    def destroy(self,request,pk=None):
        return Response({'msg':'This is from destroy  method of ViewSet'})                   
