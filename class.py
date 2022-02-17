# 자료형
print(type('string'))
print(type(3))


# CLASS
# Class 명은 CamelCase로 작성
class TestClass:
    pass


# Instance(객체)
test_instance = TestClass()

# Instance 여러개 생성
test_1 = TestClass()
test_2 = TestClass()

print(type(test_instance))


# Class Variable(클래스 변수): 클래스 정의 시 변수를 정의하면 모든 인스턴스에서 동일한 변수 사용 가능
class Musician:
    title = "Idol"


drummer = Musician()
guitar = Musician()

print(drummer.title)
print(guitar.title)


# Methods(메소드): 클래스 안에서 정의된 함수
class Musician:
    title = "Idol"

    def introduction(self):
        print('I am a {}.'.format(self.title))  # 함수 안에서 클래스 변수 사용 시 self.variable 형태로


drummer = Musician()
drummer.introduction()


class Circle:
    pi = 3.14

    def area(self, radius):
        return (radius ** 2) * self.pi


circle = Circle()
pizza_area = circle.area(6)
print(pizza_area)
park_area = circle.area(100)
print(park_area)


# Constructor(생성자): __init__, 클래스 호출 시 자동으로 함수 실행하거나 값 호출할 때 사용
class Circle2:
    pi = 3.14

    def __init__(self, radius):
        print("New circle area: {}".format(radius ** 2 * self.pi))


pizza = Circle2(6)
print(pizza)


# Example
class AutoText:
    intro = '안녕하세요'

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "{intro} {name} 님".format(intro=self.intro, name=self.name)


mail_to_park = AutoText("Park")
mail_to_lee = AutoText("Lee")

print(mail_to_park.say_hello())
print(mail_to_lee.say_hello())
