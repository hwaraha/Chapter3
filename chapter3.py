# -*- coding: utf-8 -*-
"""chapter3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yMqy3JE3c21wdNJeiBSnPxSv70hLTF80
"""

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

for i in range(1, 101):
  print(i)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)

i = 0
while True:
    i += 1 
    if i > 5: break    
    print('*' * i)

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total += score   

average = total / len(A) 
print(average)