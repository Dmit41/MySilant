import django_filters
from .models import Machine, TechnicalService, Reclamation


class MachineSearch(django_filters.FilterSet):
    machineNumber = django_filters.CharFilter(lookup_expr='exact', label='Введите Номер Машины:')

    class Meta:
        model = Machine
        fields = {
           'machineNumber',
        }


class MachineFilter(django_filters.FilterSet):
    # machineNumber = django_filters.CharFilter(lookup_expr='exact', label='Введите Номер Машины:')

    class Meta:
        model = Machine
        fields = {
           'machineModel', 'engineModel', 'transmissionModel', 'driveAxleModel', 'steeringAxleModel'
        }


class TechnicalServiceFilter(django_filters.FilterSet):

    class Meta:
        model = TechnicalService
        fields = {
           'technicalServiceType', 'technicalServiceCompany', 'machine',
        }


class ReclamationFilter(django_filters.FilterSet):

    class Meta:
        model = Reclamation
        fields = {
           'failureNode', 'repairMethod', 'serviceCompany',
        }