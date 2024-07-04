from django.db import models
from django.contrib.auth.models import User


# Справочники
class MachineModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class EngineModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class TransmissionModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class DriveAxleModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class SteeringAxleModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class TechnicalServiceType(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class FailureNode(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class RepairMethod(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'

# ----------------------------------------------------------------------------


# Роли
class Client(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class ServiceCompany(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class Manager(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'
# ----------------------------------------------------------------------------


class Machine(models.Model):
    machineNumber = models.TextField(verbose_name='№ машины')
    machineModel = models.ForeignKey(MachineModel, on_delete=models.CASCADE, verbose_name='Модель техники')
    engineModel = models.ForeignKey(EngineModel, on_delete=models.CASCADE, verbose_name='Модель двигателя')
    engineNumber = models.TextField(verbose_name='№ двигателя')
    transmissionModel = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE, verbose_name='Модель трансмиссии')
    transmissionNumber = models.TextField(verbose_name='№ трансмиссии')
    driveAxleModel = models.ForeignKey(DriveAxleModel, on_delete=models.CASCADE, verbose_name='Модель ведущего моста')
    driveAxleNumber = models.TextField(verbose_name='№ Ведущего моста')
    steeringAxleModel = models.ForeignKey(SteeringAxleModel, on_delete=models.CASCADE, verbose_name='Модель управляемого моста')
    steeringAxleNumber = models.TextField(verbose_name='№ управляемого моста')
    deliveryContract_N_data = models.TextField(verbose_name='Договор поставки №, дата')
    deliveryDate = models.DateField(verbose_name='Дата отгрузки с завода (Год-Месяц-День)')
    consignee = models.TextField(verbose_name='Грузополучатель (конечный потребитель)')
    deliveryAdress = models.TextField(verbose_name='Адрес поставки (эксплуатации)')
    completeSet = models.TextField(verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    serviceCompany = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.machineNumber}'


class TechnicalService(models.Model):
    technicalServiceType = models.ForeignKey(TechnicalServiceType, on_delete=models.CASCADE, verbose_name='Вид ТО')
    technicalServiceDate = models.DateField(verbose_name='Дата проведения ТО (Год-Месяц-День)')
    operatingTime = models.IntegerField(verbose_name='Наработка, м/час')
    orderNumber = models.TextField(verbose_name='№ заказ-наряда')
    orderDate = models.DateField(verbose_name='Дата заказ-наряда (Год-Месяц-День)')
    technicalServiceCompany = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Организация, проводившая ТО')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='Машина')


class Reclamation(models.Model):
    failureDate = models.DateField(verbose_name='Дата отказа (Год-Месяц-День)')
    operatingTime = models.IntegerField(verbose_name='Наработка, м/час')
    failureNode = models.ForeignKey(FailureNode, on_delete=models.CASCADE, verbose_name='Узел отказа')
    failureDescription = models.TextField(verbose_name='Описание отказа')
    repairMethod = models.ForeignKey(RepairMethod, on_delete=models.CASCADE, verbose_name='Способ восстановления')
    usedSpareParts = models.TextField(verbose_name='Используемые запасные части')
    repairDate = models.DateField(verbose_name='Дата восстановления (Год-Месяц-День)')
    machineDowntime = models.IntegerField(verbose_name='Время простоя техники')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='Mашина')
    serviceCompany = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Cервисная компания')