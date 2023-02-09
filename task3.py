# Task3

def money(years, salary):
    if years > 1 and years < 3:
        salary = int(salary * 1.1)
        print("С прибавкой 10%:", salary)
    if years >= 3:
        salary = int(salary * 1.2)
    print("С прибавкой 20%:", salary)

    if salary < 4000:
        salary += 1000
        print("С прибавкой 1000:", salary)
    if salary >= 4000:
        salary += 500
        print("С прибавкой 500:", salary)


money(4, 10000)
