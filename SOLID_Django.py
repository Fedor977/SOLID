"""
Принципы SOLID в Django:

1. Single Responsibility Principle (Принцип единственной ответственности)
2. Open/Closed Principle (Принцип открытости/закрытости)
3. Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
4. Interface Segregation Principle (Принцип разделения интерфейса)
5. Dependency Inversion Principle (Принцип инверсии зависимостей)
"""

# 1. Single Responsibility Principle (Принцип единственной ответственности)
# views.py
from django.shortcuts import render
from .services import fetch_data


def data_view(request):
    data = fetch_data()  # Получение данных
    return render(request, 'data.html', {'data': data})  # Отображение данных


# services.py
def fetch_data():
    """ Функция fetch_data отвечает только за получение данных """
    return "Some data"


# 2. Open/Closed Principle (Принцип открытости/закрытости)
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


@receiver(post_save, sender=Order)
def notify_customer(sender, instance, **kwargs):
    """ Уведомление клиента о заказе, открыто для новых действий при сохранении заказа """
    pass


# 3. Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
class User:
    def has_permission(self):
        return False


class AdminUser(User):
    """ AdminUser расширяет User, добавляя возможность выдачи разрешений """

    def has_permission(self):
        return True


class RegularUser(User):
    """ RegularUser реализует метод has_permission в соответствии с принципом подстановки Лисков """
    pass


# 4. Interface Segregation Principle (Принцип разделения интерфейса)
# mixins.py
class CreateMixin:
    """ Интерфейс CreateMixin для создания объектов """

    def create(self):
        pass


class UpdateMixin:
    """ Интерфейс UpdateMixin для обновления объектов """

    def update(self):
        pass


class DeleteMixin:
    """ Интерфейс DeleteMixin для удаления объектов """

    def delete(self):
        pass


# views.py
from .mixins import CreateMixin, UpdateMixin


class DataView(CreateMixin, UpdateMixin):
    def create(self):
        # Реализация метода создания
        pass

    def update(self):
        # Реализация метода обновления
        pass


# 5. Dependency Inversion Principle (Принцип инверсии зависимостей)
# storage.py
class Storage:
    """ Интерфейс Storage для абстракции хранилища данных """

    def save(self, data):
        pass


class FileStorage(Storage):
    def save(self, data):
        with open("file.txt", "w") as f:
            f.write(data)  # Сохранение данных в файл


class DBStorage(Storage):
    def save(self, data):
        # Сохранение данных в базу данных
        pass


# views.py
from .storage import Storage


class DataView:
    def __init__(self, storage: Storage):
        self.storage = storage

    def save_data(self, data):
        self.storage.save(data)  # Использование абстрактного хранилища
