from django.shortcuts import render
import requests
def get_geographic_info(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get('REMOTE_ADRR')
    url='http://api.ipstack.com/24.45.165.236?access_key=d04ededc06d922754ba059a24b3868b7&format=1'
    response=requests.get(url)
    data=response.json()
    return render(request,'testapp/info.html',data)
