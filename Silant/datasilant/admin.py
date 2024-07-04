from django.contrib import admin
from .models import *


admin.site.register(MachineModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveAxleModel)
admin.site.register(SteeringAxleModel)
admin.site.register(TechnicalServiceType)
admin.site.register(FailureNode)
admin.site.register(RepairMethod)

admin.site.register(Client)
admin.site.register(ServiceCompany)
admin.site.register(Manager)

admin.site.register(Machine)
admin.site.register(TechnicalService)
admin.site.register(Reclamation)


