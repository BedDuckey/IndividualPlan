from django import forms
from .models import Plan, Task, User, Report

class PlanForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=User.objects.all(), label="Student")
    supervisor = forms.ModelChoiceField(queryset=User.objects.filter(role__name="Teacher"), label="Supervisor")

    class Meta:
        model = Plan
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
