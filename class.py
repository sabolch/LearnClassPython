# Эрик Мэтиз, классы
class Dog():
    """Простая модель собачатины."""

    sounds = "Гав-гав!"

    def __init__(self, name, age):
        """Инициализируем атрибуты нейм и эйдж."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print("\n" + self.name.title() + " садится.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " перекатывается!")

    def say(self):
        print(self.name.title() + ' говорит: \"' + self.sounds + "\"")


my_dog = Dog('вадик', 6)

print("Собаку мою, получается, зовут " + my_dog.name.title() + ".")
print("Ей, значит, получается, уже " + str(my_dog.age) + " лет. Я правильно понимаю?")

my_dog.sit()
my_dog.roll_over()
my_dog.say()

your_dog = Dog("нурик", 32)

print("\nТвоя собачка: " + your_dog.name.title())
print("Ему " + str(your_dog.age) + " лет")
your_dog.roll_over()

# Задания к уроку.

"""9.1. Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant должен содержать два атрибута: 
restaurant_name и cuisine_type. Создайте метод describe_restaurant(), который выводит два атрибута, 
и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт.
Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута по отдельности, 
затем вызовите оба метода."""

print("\n\n\n\t\t\t### <<< Здесь, значит, получается, начинается выполнение заданий 9.1 >>> ###")


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        self.number_served = 0

    def describe_restaurant(self):
        print("Ресторан, значит, называется " + "'" + self.restaurant_name.title() + "'." + " А тип ресторана: " +
              self.cuisine_type.title())

    def open_restaurant(self):
        print("Значит так. Получается, ресторанчик наш, открыт. Так, получается?")


restaurant = Restaurant("Del Mar", "Luxury", 65)

print("\n" + restaurant.restaurant_name)
print(restaurant.cuisine_type + "\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("Ресторан обслужил: " + str(restaurant.number_served) + " посетителей")

"""9.2. Три ресторана: начните с класса из упражнения 9.1. Создайте три разных экземпляра, вызовите для каждого 
экземпляра метод describe_restaurant()."""

fabrika = Restaurant("Fabrika", "lounge", 12)
pizzaHouse = Restaurant("pizza house", "Lux", 22)
indi = Restaurant("indi", "bistro", 8)

print("\n\n\n\t\t\t### <<< Здесь, значит, получается, начинается выполнение заданий 9.2 >>> ###")

fabrika.describe_restaurant()
pizzaHouse.describe_restaurant()
indi.describe_restaurant()

"""9.3. Пользователи: создайте класс с именем User. Создайте два атрибута first_name и last_ name, а затем еще 
несколько атрибутов, которые обычно хранятся в профиле пользователя. Напишите метод describe_user(), который выводит 
сводку с информацией о пользователе. Создайте еще один метод greet_user() для вывода персонального приветствия для 
пользователя.
Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба метода для каждого пользователя."""

print("\n\n\n\t\t\t### <<< Здесь, значит, получается, начинается выполнение задания 9.2 >>> ###\n")


class User():
    def __init__(self, first_name, last_name, age, dick, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dick = dick
        self.login_attempts = login_attempts

    def describe_user(self):
        print(
            "Имя: " + self.first_name.title() + "\nФамилия: " + self.last_name.title() + "\nВозраст: " + str(self.age) +
            "\nЧлен: " + str(self.dick) + "см")

    def greet_user(self):
        print("Ассаламу Алейкум, " + self.first_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


zalim = User("Залим", "Великолепный", 26, 15, 0)
vitalina = User("Виталик", "Давыдов", 27, 9, 0)
sabolch = User("Саболч", "Хусти", 35, 24, 0)

zalim.describe_user()
vitalina.greet_user()

zalim.increment_login_attempts()
zalim.increment_login_attempts()
zalim.increment_login_attempts()
zalim.increment_login_attempts()
zalim.increment_login_attempts()
zalim.increment_login_attempts()

print("Попыток входа: " + str(zalim.login_attempts))

zalim.reset_login_attempts()
print("<# reset login attempts #>".capitalize())
print("Попыток входа: " + str(zalim.login_attempts))

#
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 1000

    def get_descriptive(self):
        long_name = str(self.year) + " " + self.make.title() + " " + self.model.upper()
        return long_name

    def read_odometer(self):
        print("Пробег этой машины составляет: " + str(self.odometer_reading) + " км.")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading += mileage
        else:
            print("ERROR! Нельзя сбрасывать счётчик пробега!")


my_new_car = Car('mercedes', 'xxl', 2019)
print("\n\n" + my_new_car.get_descriptive())
my_new_car.update_odometer(2000)
my_new_car.read_odometer()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 90

    def describe_battery(self):
        print("Емкость аккумулятора: " + str(self.battery_size))

    def read_odometer(self):
        print("No odometer! This is Electric car")


my_tesla = ElectricCar('tesla', 'model S', 2020)
print(my_tesla.get_descriptive())
my_tesla.describe_battery()
my_tesla.read_odometer()
