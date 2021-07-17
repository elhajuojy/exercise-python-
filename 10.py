import math
x1=int(input("please entre x1 :"))
x2=int(input("please entre x2 :"))
y1=int(input("please entre y1 :"))
y2=int(input("please entre y2 :"))

d=(x2-x1)**2+(y2-y1)**2
d=math.sqrt(d)

print(f"the distance betwen x and y is : ",format(d,".3f"))