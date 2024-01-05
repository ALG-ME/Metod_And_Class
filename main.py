class Person:
    name = ''
    age = ''

    #self - обращение к атрибуту конкретного объекта
    def show_info(self):  # Метод
        print(f'{self.name}, {self.age}')


p1 = Person()
p1.name = 'Петя'
p1.age = '20'
p1.show_info()

p1 = Person()
p1.name = 'гена'
p1.age = '222'
p1.show_info()

# __init__ - Конструктор класса
class Person:
    def __init__(self, id, name = 'Empty'):
        self.id = id
        self.name = name
        print(f'Объект ID: {self.id} создан')
        print(f'Имя: {self.name}')

    def say(self, text):
        print(f'{self.name}: {text}')

    def say_hello(self):
        self.say('hello')


p1 = Person(33)
pr2 = Person(2, 'Вася')

pr2.say_hello()
pr2.say('Ккукукукук')
