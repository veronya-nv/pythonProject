
def averageF(n,m):
    iterac = 0
    sum = 0
    for i in range(n, m):
        sum += i
        i += 1
        iterac += 1
    average = sum / iterac
    print("Cереднє арифметичне -", average)

averageF(1,100)
