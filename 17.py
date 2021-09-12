from math import sqrt
a=int(input("entre a"))
b=int(input("entre b"))
c=int(input("entre c"))
delta= (b**2)- (4*a*c)
if delta>0:
    x1= -b+sqrt(delta)/2*a
    x2= -b-sqrt(delta)/2*a
    print(f'x1 = {x1} , x2 = {x2} ')
elif delta==0:
    print("x =-b/2*a")
else :
    print("theres no soulation in R ")   


