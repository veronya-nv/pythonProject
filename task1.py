# Task1

def age(num):
    if num < 0:
        print("Невірний вік")
    elif num >= 0 and num < 18:
        print("Ви ще неповнолітній")
    else:
        print("Ви стали дорослим")


age(18)
