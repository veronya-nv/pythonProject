# Task3
def cash(salary):
    if salary < 4000:
        salary += 1000
        print("С прибавкой 1000:", salary)
    elif salary >= 4000:
        salary += 500
        print("С прибавкой 500:", salary)
def money(years, salary):
    if years >= 1 and years < 3:
        salary = int(salary * 1.1)
        print("С прибавкой 10%:", salary)
        cash(salary)
    elif years >= 3:
        salary = int(salary * 1.2)
        print("С прибавкой 20%:", salary)
        cash(salary)
    else:
        print("Держи шоколадку")

money(1.1, 4000)
