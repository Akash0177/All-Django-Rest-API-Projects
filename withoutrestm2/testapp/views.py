from django.shortcuts import render
from django.views.generic import View
from testapp.utils import is_json
from testapp.mixins import HttpResponseMixin,SerializeMixin
import json
from testapp.models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.forms import StudentForm
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            s=Student.objects.get(id=id)
        except:
            s=None
        return s

    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json only'}),status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            std=self.get_object_by_id(id)
            if std is None:
                return self.render_to_http_response(json.dumps({'msg':'No matched record found with matched id'}),status=400)
            json_data=self.serialize([std,])
            return self.render_to_http_response(json_data)
        qs=Student.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json only'}),status=400)
        std_data=json.loads(data)
        form=StudentForm(std_data)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'Resource created succefully'}))
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json only'}),status=400)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            if std is None:
                return self.render_to_http_response(json.dumps({'msg':'To perform updation operation id is mandatory..plzz provide'}),status=400)
        std=self.get_object_by_id(id)
        if std is None:
            return self.render_to_http_response(json.dumps({'msg':'No matched record found with the given id'}),status=400)
        original_data={
        'name':std.name,
        'rollno':std.rollno,
        'marks':std.marks,
        'gf':std.gf,
        'bf':std.bf,
        }
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=std)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'Resource updated succefully'}))
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json only'}),status=400)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'To perform deletion operation id is mandatory..plzz provide'}),status=400)
        std=self.get_object_by_id(id)
        if std is None:
            return self.render_to_http_response(json.dumps({'msg':'No matched record found with the given id..not posible to delete'}),status=400)
        status,deleted_item=std.delete()
        if status==1:
            json_data=json.dumps({'msg':'Resource Deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg','unable to delete..please try again....'})
        return self.render_to_http_response(json_data,status=500)
