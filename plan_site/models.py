from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Модель статусов для индивидуальных планов
class PlanStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Название статуса
    description = models.TextField(blank=True, null=True)  # Описание статуса

    def __str__(self):
        return self.name


# Модель статусов для задач
class TaskStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Название статуса
    description = models.TextField(blank=True, null=True)  # Описание статуса (опционально)

    def __str__(self):
        return self.name


# Модель статусов для отчетов
class ReportStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Название статуса
    description = models.TextField(blank=True, null=True)  # Описание статуса (опционально)

    def __str__(self):
        return self.name


# Модель Ролей
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Название роли
    description = models.TextField(blank=True, null=True)  # Описание роли (опционально)

    def __str__(self):
        return self.name


# Расширенная модель пользователя
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='role')  # Связь с ролями
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


# Модель индивидуального плана
class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    student = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='plans',
                                )
    supervisor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='supervised_plans',
                                   )
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)  # Описание
    start_date = models.DateTimeField(default=timezone.now)  # Дата начала с дефолтным значением
    end_date = models.DateTimeField(blank=True, null=True)  # Дата окончания
    status = models.ForeignKey(PlanStatus, on_delete=models.SET_NULL, null=True, related_name="plan_status")  # Статус плана

    def __str__(self):
        return self.name


# Модель задачи в плане
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False, default="Task")
    description = models.TextField(blank=True, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, related_name="tasks")  # Связь с планом
    status = models.ForeignKey(TaskStatus, on_delete=models.SET_NULL, null=True, related_name='task_status')  # Связь со статусами


    def __str__(self):
        return self.name


# Модель отчета
class Report(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='report_url')
    file = models.FileField(upload_to='reports/' , null=True)
    uploaded_at = models.DateTimeField( default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)  # Время последнего обновления
    status = models.ForeignKey(ReportStatus, on_delete=models.SET_NULL, null=True, related_name="report_status")  # Статус отчета

    def __str__(self):
        return self.name


