from .models import Plan, Task, User, Report
from django.db.models import QuerySet

class PlanDAO:
    """Класс для работы с Plan."""

    @staticmethod
    def get_all_plans() -> QuerySet:
        """Получить список всех планов."""
        return Plan.objects.all()

    @staticmethod
    def get_plan_by_id(plan_id: int) -> Plan:
        """Получить план по ID."""
        return Plan.objects.get(pk=plan_id)

    @staticmethod
    def create_plan(data: dict) -> Plan:
        """Создать новый план."""
        return Plan.objects.create(**data)

    @staticmethod
    def update_plan(plan: Plan, data: dict) -> Plan:
        """Обновить существующий план."""
        for key, value in data.items():
            setattr(plan, key, value)
        plan.save()
        return plan

    @staticmethod
    def delete_plan(plan: Plan) -> None:
        """Удалить план."""
        plan.delete()


class TaskDAO:
    """Класс для работы с Task."""

    @staticmethod
    def get_all_tasks() -> QuerySet:
        return Task.objects.all()

    @staticmethod
    def get_task_by_id(task_id: int) -> Task:
        return Task.objects.get(pk=task_id)

    @staticmethod
    def create_task(data: dict) -> Task:
        return Task.objects.create(**data)

    @staticmethod
    def update_task(task: Task, data: dict) -> Task:
        for key, value in data.items():
            setattr(task, key, value)
        task.save()
        return task

    @staticmethod
    def delete_task(task: Task) -> None:
        task.delete()


class UserDAO:
    """Класс для работы с User."""

    @staticmethod
    def get_all_users() -> QuerySet:
        return User.objects.all()

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return User.objects.get(pk=user_id)

    @staticmethod
    def create_user(data: dict) -> User:
        return User.objects.create(**data)

    @staticmethod
    def update_user(user: User, data: dict) -> User:
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def delete_user(user: User) -> None:
        user.delete()


class ReportDAO:
    """Класс для работы с Report."""

    @staticmethod
    def get_all_reports() -> QuerySet:
        return Report.objects.all()

    @staticmethod
    def get_report_by_id(report_id: int) -> Report:
        return Report.objects.get(pk=report_id)

    @staticmethod
    def create_report(data: dict) -> Report:
        return Report.objects.create(**data)

    @staticmethod
    def update_report(report: Report, data: dict) -> Report:
        for key, value in data.items():
            setattr(report, key, value)
        report.save()
        return report

    @staticmethod
    def delete_report(report: Report) -> None:
        report.delete()
