from django import forms
from .models import Machine, TechnicalService, Reclamation


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machineNumber', 'machineModel', 'engineModel', 'engineNumber', 'transmissionModel',
                  'transmissionNumber', 'driveAxleModel', 'driveAxleNumber', 'steeringAxleModel', 'steeringAxleNumber',
                  'deliveryContract_N_data', 'deliveryDate', 'consignee', 'deliveryAdress', 'completeSet', 'client',
                  'serviceCompany']


class TechnicalServiceForm(forms.ModelForm):
    class Meta:
        model = TechnicalService
        fields = ['technicalServiceType', 'technicalServiceDate', 'operatingTime', 'orderNumber', 'orderDate',
                  'technicalServiceCompany', 'machine']


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['failureDate', 'operatingTime', 'failureNode', 'failureDescription', 'repairMethod',
                  'usedSpareParts', 'repairDate', 'machineDowntime', 'machine', 'serviceCompany', ]
