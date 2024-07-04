import random

ggs = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
o = int(input())
password = ""

for i in range(o):
    letter = random.randint(0, len(ggs) - 1)
    password += ggs[letter]
print("Сгенерированный пароль:", password)