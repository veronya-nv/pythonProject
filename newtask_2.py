
def averageF(n,m):
    iterac = 0
    sum = 0
    for i in range(n, m+1):
        sum += i
        iterac += 1
    average = sum / iterac
    print("Cереднє арифметичне -", average)

averageF(1,3)
