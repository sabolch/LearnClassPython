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

your_dog = Dog("Нурик", 32)

print("\nТвоя собачка: " + your_dog.name)
print("Ему " + str(your_dog.age) + " лет")
your_dog.roll_over()