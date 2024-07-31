"""
Принципы SOLID в Python:

1. Single Responsibility Principle (Принцип единственной ответственности)
2. Open/Closed Principle (Принцип открытости/закрытости)
3. Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
4. Interface Segregation Principle (Принцип разделения интерфейса)
5. Dependency Inversion Principle (Принцип инверсии зависимостей)
"""


# 1. Single Responsibility Principle (Принцип единственной ответственности)
class ReportGenerator:
    """ Класс ReportGenerator отвечает только за генерацию отчета """

    def generate_report(self):
        return "Report data"  # Генерация отчета


class ReportSaver:
    """ Класс ReportSaver отвечает только за сохранение отчета """

    def save_to_file(self, report):
        with open("report.txt", "w") as f:
            f.write(report)  # Сохранение отчета в файл
        print("Отчет сохранен в файл 'report.txt'")  # Сообщение о сохранении


# Демонстрация работы принципа единственной ответственности
generator = ReportGenerator()
report = generator.generate_report()
print(f"Сгенерированный отчет: {report}")  # Вывод сгенерированного отчета

saver = ReportSaver()
saver.save_to_file(report)


# 2. Open/Closed Principle (Принцип открытости/закрытости)
class PaymentProcessor:
    """ Класс PaymentProcessor открыт для расширения (новые способы оплаты), но закрыт для изменения """

    def process(self, payment_method):
        payment_method.process()  # Использование метода process()


class CreditCard:
    def process(self):
        print("Processing credit card")  # Обработка кредитной карты


class PayPal:
    def process(self):
        print("Processing PayPal")  # Обработка PayPal


# Демонстрация работы принципа открытости/закрытости
payment_processor = PaymentProcessor()
payment_processor.process(CreditCard())  # Обработка через кредитную карту
payment_processor.process(PayPal())  # Обработка через PayPal


# 3. Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
class Bird:
    def move(self):
        pass


class FlyingBird(Bird):
    """ FlyingBird расширяет Bird, добавляя возможность летать """

    def move(self):
        self.fly()

    def fly(self):
        print("Flying")


class WalkingBird(Bird):
    """ WalkingBird расширяет Bird, добавляя возможность ходить """

    def move(self):
        print("Walking")


class Duck(FlyingBird):
    pass


class Ostrich(WalkingBird):
    pass


# Демонстрация работы принципа подстановки Лисков
bird1 = Duck()
bird1.move()  # Вывод: "Flying"

bird2 = Ostrich()
bird2.move()  # Вывод: "Walking"


# 4. Interface Segregation Principle (Принцип разделения интерфейса)
class Workable:
    """ Интерфейс Workable для работы """

    def work(self):
        pass


class Eatable:
    """ Интерфейс Eatable для еды """

    def eat(self):
        pass


class Programmer(Workable, Eatable):
    def work(self):
        print("Coding")  # Программист работает

    def eat(self):
        print("Eating lunch")  # Программист ест


class Robot(Workable):
    def work(self):
        print("Assembling parts")  # Робот работает


# Демонстрация работы принципа разделения интерфейса
programmer = Programmer()
programmer.work()  # Вывод: "Coding"
programmer.eat()  # Вывод: "Eating lunch"

robot = Robot()
robot.work()  # Вывод: "Assembling parts"


# 5. Dependency Inversion Principle (Принцип инверсии зависимостей)
class Database:
    """ Интерфейс Database для подключения к базе данных """

    def connect(self):
        pass


class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL"  # Подключение к MySQL


class UserRepository:
    """ Класс UserRepository использует абстракцию Database для подключения к БД """

    def __init__(self, db: Database):
        self.db = db

    def get_user(self, user_id):
        connection = self.db.connect()
        print(connection)  # Вывод сообщения о подключении
        return "User data"  # Получение данных пользователя


# Демонстрация работы принципа инверсии зависимостей
mysql_db = MySQLDatabase()
user_repo = UserRepository(mysql_db)
user_data = user_repo.get_user(1)
print(user_data)  # Вывод: "User data"
