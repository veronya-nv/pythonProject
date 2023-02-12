def func(num):
    iterac =0
    if num < 50:
        print("Ви ввели надто маленьке число")
    else:
        while num > 50:
            num = num/2
            iterac = iterac+1
    print("Результат поділу -", num)
    print("Кількість ітерацій -", iterac)

func(100)