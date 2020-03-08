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
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Ресторан, значит, называется " + "'" + self.restaurant_name.title() + "'." + " А тип ресторана: " +
              self.cuisine_type.title())

    def open_restaurant(self):
        print("Значит так. Получается, ресторанчик наш, открыт. Так, получается?")


restaurant = Restaurant("Del Mar", "Luxury")

print("\n" + restaurant.restaurant_name)
print(restaurant.cuisine_type + "\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()

"""9.2. Три ресторана: начните с класса из упражнения 9.1. Создайте три разных экземпляра, вызовите для каждого 
экземпляра метод describe_restaurant()."""

fabrika = Restaurant("Fabrika", "lounge")
pizzaHouse = Restaurant("pizza house", "Lux")
indi = Restaurant("indi", "bistro")

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
    def __init__(self, first_name, last_name, age, dick):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dick = dick

    def describe_user(self):
        print("Имя: " + self.first_name.title() + "\nФамилия: " + self.last_name.title() + "\nВозраст: " + str(self.age) +
              "\nЧлен: " + str(self.dick) + "см")

    def greet_user(self):
        print("Ассаламу Алейкум, " + self.first_name + "!")


zalim = User("Залим", "Великолепный", 26, 15)
vitalina = User("Виталик", "Давыдов", 27, 9)
sabolch = User("Саболч", "Хусти", 35, 24)

zalim.describe_user()
vitalina.greet_user()