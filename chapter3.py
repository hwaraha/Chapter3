# LAB 3-1
game_score = int(input("score: "))
if game_score > 1000:
    print("You are a master!")

num_a = 100
num_b = 200
if num_a == num_b:
    print("Two values are equal")
num_a = 300
num_b = 300
if num_a == num_b:
    print("Two values are equal")

# LAB 3-2
n = int(input("Enter a number: "))
if n % 2 == 0:
    print(n, "is an even number")

x = int(input("Enter a number: "))
if x > 0:
    print(x, "은(는) 자연수입니다.")

# LAB 3-3
game_score = int(input("score: "))
if game_score > 1000:
    print("고수입니다")
else:
    print("입문자입니다")

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
if n1 == n2:
    print("두 값이 일치합니다")
else:
    print("두 값이 일치 않습니다")

adult = 1
minor = 0
question1 = int(input("Are you an adult? (Adult 1, minor 0): "))
if question1 == 1:
    print("You are an adult")
elif question1 == 0:
    print("You are a minor")
married = 1
single = 0
question2 = int(input("Are you married? (married 1, single 0): "))
if question2 == 1:
    print("You are married")
elif question2 == 0:
    print("You are single")

# LAB 3-4
num = 2
if num > 1 and num < 10:
        print(True)

age1 = int(input("age = "))
if age1 > 10 and age1 < 19:
    print("청소년입니다")

# LAB 3-5
speed = int(input("car speed(unit : km/h): "))
if speed > 100:
    print("High speed")
elif speed < 100 and speed > 60:
    print("medium speed")
elif speed < 60:
    print("low speed")

# LAB 3-6
for i in range(5):
    print("Hello, Python!")

for i in range(5):
    print(i)

# LAB 3-7
print(list(range(1, 101)))

print(list(range(0, 100, 2)))
print(list(range(1, 100, 2)))
print(list(range(-1, -100, -2)))

# LAB 3-8
s = 0
for i in range(1, 100):
    s = s + i
    print(i)
s = 1
for i in range(0, 100):
    s = s + i
    print(i)

for i in range(0, 100, 2):
    print(i, end = ' ')

# LAB 3-9
rows = int(input("Enter the number of rows: "))
for i in range(0, rows):
    print(' ' * i, "#")









