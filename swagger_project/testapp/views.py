from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
class EmployeeCRUDCBV(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
