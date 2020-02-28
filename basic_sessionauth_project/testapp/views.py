from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[SessionAuthentication,]
    permission_classes=[IsAuthenticated,]
