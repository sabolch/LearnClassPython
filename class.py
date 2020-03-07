# Эрик Мэтиз, классы
class Dog():
    """Простая модель собачатины."""

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


my_dog = Dog('вадик', 6)

print("Собаку мою, получается, зовут " + my_dog.name.title() + ".")
print("Ей, значит, получается, уже " + str(my_dog.age) + " лет. Я правильно понимаю?")

my_dog.sit()
my_dog.roll_over()

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

print("\n\n\n\t\t\t### <<< Здесь, значит, получается, начинается выполнение заданий >>> ###")

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Ресторан, значит, называется " + "'" + self.restaurant_name.title() + "'." + " А тип ресторана: " +
              restaurant.cuisine_type)

    def open_restaurant(self):
        print("Значит так. Получается, ресторанчик наш, открыт. Так, получается?")


restaurant = Restaurant("Del Mar", "Luxury")

print("\n" + restaurant.restaurant_name)
print(restaurant.cuisine_type + "\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()
