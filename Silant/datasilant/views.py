from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .filters import *
from .models import *
from .forms import *


class MachineGusetList(ListView):
    model = Machine
    ordering = 'machineNumber'
    template_name = 'main.html'
    context_object_name = 'main'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.search = MachineSearch(self.request.GET, queryset)

        return self.search.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.search
        return context


class MachineList(PermissionRequiredMixin, ListView):
    permission_required = ('datasilant.view_machine',)
    model = Machine
    ordering = 'machineNumber'
    template_name = 'machine.html'
    context_object_name = 'machine'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MachineFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class MachineCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('datasilant.add_machine',)
    form_class = MachineForm
    model = Machine
    template_name = 'machine_create.html'
    success_url = reverse_lazy('main')


class MachineUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('datasilant.change_machine',)
    form_class = MachineForm
    model = Machine
    template_name = 'machine_create.html'
    success_url = reverse_lazy('main')


class TechnicalServiceList(PermissionRequiredMixin, ListView):
    permission_required = ('datasilant.view_technicalservice',)
    model = TechnicalService
    ordering = 'technicalServiceDate'
    template_name = 'service.html'
    context_object_name = 'service'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TechnicalServiceFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class TechnicalServiceCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('datasilant.add_technicalservice',)
    form_class = TechnicalServiceForm
    model = TechnicalService
    template_name = 'service_create.html'
    success_url = reverse_lazy('service')


class TechnicalServiceUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('datasilant.change_technicalservice',)
    form_class = TechnicalServiceForm
    model = TechnicalService
    template_name = 'service_create.html'
    success_url = reverse_lazy('service')


class ReclamationList(PermissionRequiredMixin, ListView):
    permission_required = ('datasilant.view_reclamation',)
    model = Reclamation
    ordering = 'failureDate'
    template_name = 'reclamation.html'
    context_object_name = 'reclamation'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ReclamationFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ReclamationCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('datasilant.add_reclamation',)
    form_class = ReclamationForm
    model = Reclamation
    template_name = 'reclamation_create.html'
    success_url = reverse_lazy('reclamation')


class ReclamationUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('datasilant.change_reclamation',)
    form_class = ReclamationForm
    model = Reclamation
    template_name = 'reclamation_create.html'
    success_url = reverse_lazy('reclamation')


# Cправочник
class MachineModelView(DetailView):
    model = MachineModel
    template_name = 'default.html'
    context_object_name = 'client'


class EngineModelView(DetailView):
    model = EngineModel
    template_name = 'default.html'
    context_object_name = 'client'


class TransmissionModelView(DetailView):
    model = TransmissionModel
    template_name = 'default.html'
    context_object_name = 'client'


class DriveAxleModelView(DetailView):
    model = DriveAxleModel
    template_name = 'default.html'
    context_object_name = 'client'


class SteeringAxleModelView(DetailView):
    model = SteeringAxleModel
    template_name = 'default.html'
    context_object_name = 'client'


class TechnicalServiceTypeView(DetailView):
    model = TechnicalServiceType
    template_name = 'default.html'
    context_object_name = 'client'


class FailureNodeView(DetailView):
    model = FailureNode
    template_name = 'default.html'
    context_object_name = 'client'


class RepairMethodView(DetailView):
    model = RepairMethod
    template_name = 'default.html'
    context_object_name = 'client'


# Роли
class ClientView(DetailView):
    model = Client
    template_name = 'default.html'
    context_object_name = 'client'


class ServiceCompanyView(DetailView):
    model = ServiceCompany
    template_name = 'default.html'
    context_object_name = 'service_comp'


class MangerView(DetailView):
    model = Manager
    template_name = 'default.html'
    context_object_name = 'manager'


