sum= int(input("Сумма чисел:"))
pr= int(input("произведение: "))
D=sum**2-4*pr
y1 = (sum-D**0.5)/2
y2 = (sum+D**0.5)/2
x1=sum-y1
x2=sum-y2
print(x1,y1)
print(x2,y2)



    