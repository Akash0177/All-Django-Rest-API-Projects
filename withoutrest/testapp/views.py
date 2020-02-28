from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def emp_data_view(request):
    emp_data={
    'eno':100,
    'ename':'Akash',
    'esal':10000,
    'eaddr':'Mumbai',
    }
    resp='<h1>Employee Number:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

import json
def emp_data_jsonview(request):
    emp_data={
    'eno':100,
    'ename':'Akash',
    'esal':10000,
    'eaddr':'Mumbai',
    }
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data={
    'eno':100,
    'ename':'Akash',
    'esal':10000,
    'eaddr':'Mumbai',
    }
    return JsonResponse(emp_data)

from django.views.generic import View
from testapp.mixins import HttpResponseMixin
class jsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is from get Method'})
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is from post Method'})
        return self.render_to_http_response(json_data)

    def put(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is from put Method'})
        return self.render_to_http_response(json_data)

    def delete(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is from delete Method'})
        return self.render_to_http_response(json_data)
