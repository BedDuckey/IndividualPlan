from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Plan, Task, User, Report
from .forms import PlanForm, TaskForm, UserForm, ReportForm


def home(request):
    return render(request, 'plan_site/home.html')

# CRUD для Plan
def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'plan_site/plan_list.html', {'plans': plans})

def plan_create(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plan_list')
    else:
        form = PlanForm()
    return render(request, 'plan_site/plan_form.html', {'form': form})

def plan_detail(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    return render(request, 'plan_site/plan_detail.html', {'plan': plan})

def plan_update(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('plan_list')
    else:
        form = PlanForm(instance=plan)
    return render(request, 'plan_site/plan_form.html', {'form': form, 'plan': plan})


def plan_delete(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == 'POST':
        plan.delete()
        return redirect('plan_list')  # Перенаправление на список планов
    return render(request, 'plan_site/plan_confirm_delete.html', {'plan': plan})

# CRUD для Task
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'plan_site/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm()
    return render(request, 'plan_site/task_form.html', {'form': form})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'plan_site/task_detail.html', {'task': task})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm(instance=task)
    return render(request, 'plan_site/task_form.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect(reverse('task_list'))
    return render(request, 'plan_site/task_confirm_delete.html', {'task': task})


# CRUD для User
def user_list(request):
    users = User.objects.all()
    return render(request, 'plan_site/user_list.html', {'users': users})


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_list'))
    else:
        form = UserForm()
    return render(request, 'plan_site/user_form.html', {'form': form})


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'plan_site/user_detail.html', {'user': user})


def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_list'))
    else:
        form = UserForm(instance=user)
    return render(request, 'plan_site/user_form.html', {'form': form})


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('user_list'))
    return render(request, 'plan_site/user_confirm_delete.html', {'user': user})


# CRUD для Report
def report_list(request):
    reports = Report.objects.all()
    return render(request, 'plan_site/report_list.html', {'reports': reports})


def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('report_list'))
    else:
        form = ReportForm()
    return render(request, 'plan_site/report_form.html', {'form': form})


def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'plan_site/report_detail.html', {'report': report})


def report_update(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('report_list'))
    else:
        form = ReportForm(instance=report)
    return render(request, 'plan_site/report_form.html', {'form': form})


def report_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        report.delete()
        return HttpResponseRedirect(reverse('report_list'))
    return render(request, 'plan_site/report_confirm_delete.html', {'report': report})