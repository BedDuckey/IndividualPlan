from django.shortcuts import render, get_object_or_404, redirect

from .dao import *
from .models import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.http import HttpResponse

class GenerateReport(APIView):
    def get(self, request, *args, **kwargs):
        # Создаем HTTP-ответ с заголовками для PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # Создаем объект canvas для PDF
        p = canvas.Canvas(response, pagesize=letter)

        # Пример добавления текста
        p.drawString(100, 750, "Отчет по данным работы")
        p.drawString(100, 730, "Задача выполнена успешно.")

        # Завершаем создание PDF
        p.showPage()
        p.save()

        return response


def home(request):
    return render(request, 'plan_site/home.html')

# -----------------------------------------------Планы-----------------------------------------------
class PlanList(APIView):
    def get(self, request):
        plans = PlanDAO.get_all_plans()  # Используем DAO для получения данных
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            new_plan = PlanDAO.create_plan(serializer.validated_data)  # Используем DAO для создания плана
            return Response(PlanSerializer(new_plan).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanDetail(APIView):
    def get(self, request, pk):
        plan = get_object_or_404(PlanDAO.get_all_plans(), pk=pk)  # Используем DAO
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    def put(self, request, pk):
        plan = get_object_or_404(PlanDAO.get_all_plans(), pk=pk)
        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            updated_plan = PlanDAO.update_plan(plan, serializer.validated_data)  # Используем DAO
            return Response(PlanSerializer(updated_plan).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        plan = get_object_or_404(PlanDAO.get_all_plans(), pk=pk)
        PlanDAO.delete_plan(plan)  # Используем DAO
        return Response(status=status.HTTP_204_NO_CONTENT)


# -----------------------------------------------Задачи-----------------------------------------------
class TaskList(APIView):
    def get(self, request):
        tasks = TaskDAO.get_all_tasks()  # Используем DAO
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            new_task = TaskDAO.create_task(serializer.validated_data)  # Используем DAO
            return Response(TaskSerializer(new_task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    def get(self, request, pk):
        task = get_object_or_404(TaskDAO.get_all_tasks(), pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = get_object_or_404(TaskDAO.get_all_tasks(), pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            updated_task = TaskDAO.update_task(task, serializer.validated_data)  # Используем DAO
            return Response(TaskSerializer(updated_task).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(TaskDAO.get_all_tasks(), pk=pk)
        TaskDAO.delete_task(task)  # Используем DAO
        return Response(status=status.HTTP_204_NO_CONTENT)


#-----------------------------------------------Пользователи-----------------------------------------------
class UserList(APIView):
    def get(self, request):
        users = UserDAO.get_all_users()  # Используем DAO
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = UserDAO.create_user(serializer.validated_data)  # Используем DAO
            return Response(UserSerializer(new_user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get(self, request, pk):
        user = get_object_or_404(UserDAO.get_all_users(), pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(UserDAO.get_all_users(), pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            updated_user = UserDAO.update_user(user, serializer.validated_data)  # Используем DAO
            return Response(UserSerializer(updated_user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(UserDAO.get_all_users(), pk=pk)
        UserDAO.delete_user(user)  # Используем DAO
        return Response(status=status.HTTP_204_NO_CONTENT)


#-----------------------------------------------Отчеты-----------------------------------------------
class ReportList(APIView):
    def get(self, request):
        reports = ReportDAO.get_all_reports()  # Используем DAO
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            new_report = ReportDAO.create_report(serializer.validated_data)  # Используем DAO
            return Response(ReportSerializer(new_report).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportDetail(APIView):
    def get(self, request, pk):
        report = get_object_or_404(ReportDAO.get_all_reports(), pk=pk)
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    def put(self, request, pk):
        report = get_object_or_404(ReportDAO.get_all_reports(), pk=pk)
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            updated_report = ReportDAO.update_report(report, serializer.validated_data)  # Используем DAO
            return Response(ReportSerializer(updated_report).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        report = get_object_or_404(ReportDAO.get_all_reports(), pk=pk)
        ReportDAO.delete_report(report)  # Используем DAO
        return Response(status=status.HTTP_204_NO_CONTENT)


# Представление для страницы списка планов
def plan_list(request):
    return render(request, 'plan_site/plan.html')

# Представление для страницы списка задач
def task_list(request):
    return render(request, 'plan_site/task.html')

# Представление для страницы списка отчетов
def report_list(request):
    return render(request, 'plan_site/report.html')

# Представление для страницы списка пользователей
def user_list(request):
    return render(request, 'plan_site/user.html')
