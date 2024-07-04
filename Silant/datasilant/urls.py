from django.urls import path
from .views import *

urlpatterns = [
   path('machine', MachineList.as_view(), name='machine'),
   path('machine/create', MachineCreate.as_view(), name='machine_create'),
   path('machine/<int:pk>/update/', MachineUpdate.as_view(), name='machine_update'),
   path('service', TechnicalServiceList.as_view(), name='service'),
   path('service/create', TechnicalServiceCreate.as_view(), name='service_create'),
   path('service/<int:pk>/update/', TechnicalServiceUpdate.as_view(), name='service_update'),
   path('reclamation', ReclamationList.as_view(), name='reclamation'),
   path('reclamation/create', ReclamationCreate.as_view(), name='reclamation_create'),
   path('reclamation/<int:pk>/update/', ReclamationUpdate.as_view(), name='reclamation_update'),
]